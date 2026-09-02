# -*- coding: utf-8 -*-
"""Extrae la columna ESPECIFICACION de los COA. No el resultado del lote:
la especificacion es lo estable, el resultado caduca con el lote."""
import re, zlib, os, json

def texto(path):
    d=open(path,'rb').read(); out=[]
    for m in re.finditer(rb'stream\r?\n(.*?)endstream', d, re.S):
        try: s=zlib.decompress(m.group(1))
        except Exception: continue
        for t in re.findall(rb'\((?:\\.|[^()\\])*\)', s):
            out.append(re.sub(rb'\\([()\\])', rb'\1', t[1:-1]).decode('latin1'))
    return re.sub(r'\s+',' ',''.join(out))

def uno(pat, t, g=1):
    m=re.search(pat, t)
    return m.group(g).strip() if m else None

def limpia(v):
    if not v: return None
    v=v.replace('0C','°C').replace('1050C','105°C')
    # el proveedor escribe en ingles britanico; el sitio es americano
    v=v.replace('coloured','colored')
    v=re.sub(r'(\d+)\s*[°º]?\s*C\b', r'\1 °C', v)   # 105C / 105 C / 105ºC -> 105 °C
    v=re.sub(r'\s+',' ',v).strip(' .,')
    return v or None

def parse(t):
    d={}
    d['descripcion']  = limpia(uno(r'Description([A-Za-z ]+?powder)', t))
    # El patron antiguo exigia un parentesis de cierre. El COA del Shilajit no
    # lo trae, asi que la captura se comia las filas siguientes de la tabla.
    d['secado']       = limpia(uno(r'Loss on drying(Not more than [\d.]+ ?% ?w/w(?: \(dried at [^)]*\))?)', t))
    d['densidad']     = limpia(uno(r'Tapped bulk density(Between [\d.]+ ?g/ ?ml and [\d.]+ ?g/ ?ml)', t))
    d['cenizas']      = limpia(uno(r'Ash Content(Not more than [\d.]+ ?% ?w/w)', t))
    d['solubilidad']  = limpia(uno(r'Water soluble \([^)]*\)(Not less than [\d.]+ ?% ?w/w)', t))
    # malla: la fila mas fina con su minimo
    mallas=re.findall(r'(\d+) mesh(?:Not less than|NLT) ([\d.]+) ?% ?w/w', t)
    d['malla'] = f'{mallas[-1][0]} mesh, min. {mallas[-1][1]}%' if mallas else None
    # Ensayo quimico. Diez maquetas distintas para lo mismo en los 24 COA:
    # "Content of X", "X Content", con y sin metodo entre parentesis, "ByGravimetric"
    # pegado, "NLT" o "Not less than", y unidades % o GDU (bromelina). Por eso el
    # patron general en vez de uno por formato.
    m=re.search(r'Chemical Assay(.{0,90}?)(?:Not less than|NLT) ?([\d.]+) ?(%|GDU)', t)
    if m:
        bruto=m.group(1)
        met=re.search(r'By[- ]?([A-Za-z ]{3,20}?)\s*\)', bruto) or re.search(r'By[- ]?([A-Za-z]+)', bruto)
        metodo=met.group(1).strip() if met else None
        analito=re.sub(r'\(?\s*By[- ]?[A-Za-z ]*\)?','',bruto)
        analito=re.sub(r'^Content of\s*','',analito)
        analito=re.sub(r'\s*Content$','',analito.strip(' .,()')).strip(' .,()')
        d['ensayo']=(f'{analito} min. {m.group(2)}{m.group(3)}'
                     + (f' ({metodo})' if metodo else ''))
    else:
        d['ensayo']=None
    d['botanico']     = limpia(uno(r'Botanical name([A-Za-z .()]+?)Plant Part', t))
    d['parte']        = limpia(uno(r'Plant Part([A-Za-z ]+?)Standardization', t))
    d['metales']      = limpia(uno(r'Total heavy metals(Not more than \d+ ?ppm)', t))
    d['pesticidas']   = 'Complies with USP' if re.search(r'Residual pesticidesTo comply as per USP', t) else None
    d['disolventes']  = 'Complies with USP' if re.search(r'Residual solventsTo comply as per USP', t) else None
    d['categoria']    = 'Nutraceutical and cosmeceutical' if 'Neutraceutical' in t or 'Nutraceutical' in t else None
    return d

if __name__ == '__main__':
    D=os.path.expanduser('~/Desktop/Tradecorp/Technical Sheets')
    salida={}
    for f in sorted(os.listdir(D)):
        if not f.lower().endswith('.pdf'): continue
        t=texto(os.path.join(D,f))
        if 'CERTIFICATE OF ANALYSIS' not in t.upper(): continue
        salida[f]=parse(t)
    json.dump(salida, open(os.path.join(os.path.dirname(__file__),'coa.json'),'w'),
              ensure_ascii=False, indent=1)
    # informe de cobertura
    campos=['botanico','parte','ensayo','descripcion','malla','solubilidad',
            'densidad','secado','cenizas','metales','pesticidas','disolventes']
    print(f'{len(salida)} COA procesados\n')
    print(f'{"campo":<14} {"con dato":>9}')
    for c in campos:
        n=sum(1 for v in salida.values() if v.get(c))
        print(f'{c:<14} {n:>4}/{len(salida)}')
