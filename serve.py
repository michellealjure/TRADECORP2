#!/usr/bin/env python3
"""Local preview server for the TradeCorp site — with caching disabled.

Plain `python3 -m http.server` sends Last-Modified and no Cache-Control, so the
browser keeps serving an old copy of index.html after an edit. That is why a
change can look like it "didn't apply". This sends no-store on everything.

    python3 serve.py            # serves docs/ on 8090
    python3 serve.py 8091 src   # or pick a port and folder
"""
import http.server, os, socket, socketserver, sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8090
root = sys.argv[2] if len(sys.argv) > 2 else "docs"
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), root))

class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    # SimpleHTTPRequestHandler ignores Range, so <video> reports seekable=[0,0]
    # and setting currentTime is silently ignored. Real hosts support Range, so
    # without this a seek bug only shows up locally — and looks like broken JS.
    def send_head(self):
        rng = self.headers.get("Range")
        if not rng or not rng.startswith("bytes="):
            return super().send_head()
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            return super().send_head()
        try:
            f = open(path, "rb")
        except OSError:
            self.send_error(404, "File not found")
            return None
        size = os.fstat(f.fileno()).st_size
        first, _, last = rng[6:].partition("-")
        try:
            start = int(first) if first else 0
            end = int(last) if last else size - 1
        except ValueError:
            f.close()
            self.send_error(400, "Bad Range")
            return None
        end = min(end, size - 1)
        if start > end:
            f.close()
            self.send_response(416)
            self.send_header("Content-Range", f"bytes */{size}")
            self.end_headers()
            return None
        f.seek(start)
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(end - start + 1))
        self.send_header("Accept-Ranges", "bytes")
        self.end_headers()
        return _Slice(f, end - start + 1)


class _Slice:
    """Reads at most `remaining` bytes, so copyfile stops at the range end."""
    def __init__(self, f, remaining):
        self.f, self.remaining = f, remaining

    def read(self, n=-1):
        if self.remaining <= 0:
            return b""
        if n is None or n < 0 or n > self.remaining:
            n = self.remaining
        data = self.f.read(n)
        self.remaining -= len(data)
        return data

    def close(self):
        self.f.close()

class Quiet(NoCache):
    """Video makes the browser abort connections constantly (it stops a download the
    moment it has buffered enough). Unhandled, each abort raises and leaves noise —
    and enough of them can wedge the server. Swallow them and move on."""

    # Sin esto un cliente que abre conexión y no manda una petición completa se queda
    # con un hilo y un descriptor de archivo PARA SIEMPRE. El navegador abre conexiones
    # especulativas y aborta rangos de vídeo a cada rato, así que se acumulan: a los
    # dos días el proceso agota su límite de descriptores, accept() empieza a fallar y
    # el servidor queda escuchando pero sin atender a nadie. Ese es exactamente el
    # síntoma que se vio dos veces. 30s es de sobra para una petición local.
    timeout = 30

    def handle_one_request(self):
        try:
            super().handle_one_request()
        except (BrokenPipeError, ConnectionResetError):
            self.close_connection = True

    def copyfile(self, source, outputfile):
        try:
            super().copyfile(source, outputfile)
        except (BrokenPipeError, ConnectionResetError):
            pass


class Server(socketserver.ThreadingTCPServer):
    daemon_threads = True       # no dejar hilos colgados de descargas abortadas
    allow_reuse_address = True  # reiniciar sin esperar a que el puerto se libere

    # Escuchar solo en IPv4 rompe el navegador sin dar ninguna pista: muchos resuelven
    # "localhost" a ::1 primero y la conexión se rechaza, aunque curl (que va por IPv4)
    # responda 200. Un socket IPv6 con V6ONLY=0 atiende las dos familias.
    address_family = socket.AF_INET6

    def server_bind(self):
        try:
            self.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        except (AttributeError, OSError):
            pass
        super().server_bind()

    def handle_error(self, request, client_address):
        # El manejador por defecto escupe un traceback por cada aborto de vídeo.
        # Solo interesa lo que no sea una desconexión normal del cliente.
        exc = sys.exc_info()[1]
        if isinstance(exc, (BrokenPipeError, ConnectionResetError, socket.timeout)):
            return
        super().handle_error(request, client_address)


# Segundo cinturón: subir el límite de descriptores todo lo que deje el sistema.
# El techo por defecto en macOS (256) se alcanza rápido sirviendo cuatro vídeos.
try:
    import resource
    _soft, _hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    resource.setrlimit(resource.RLIMIT_NOFILE, (min(4096, _hard), _hard))
except Exception:
    pass


print(f"serving {root}/ at http://localhost:{port}  (caching disabled, Range on)")
with Server(("::", port), Quiet) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nbye")
