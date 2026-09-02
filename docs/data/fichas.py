# -*- coding: utf-8 -*-
"""Que PDF le corresponde a cada VARIANTE del catalogo.

Por variante y no por producto: el colageno y la moringa tienen una ficha
distinta para cada graduacion, mientras que Ashwagandha, Guggul, Karela, Arjuna,
Tribulus, Triphala, Bromelain y Shilajit comparten una sola entre sus dos.

La clave es (nombre del producto, grado). Un grado None significa "todas las
variantes de este producto usan la misma ficha".
"""

# Nombre del archivo original en la carpeta de Michelle -> nombre limpio publicado
FICHAS = {
 # producto                    grado            archivo original
 ('Hydrolyzed Bovine Collagen','Granular'): 'Technical Specifications Granular Hydrolyzed Colagen (1).pdf',
 ('Hydrolyzed Bovine Collagen','Instant'):  'Technical Specifications Instant Hydrolyzed Collagen.pdf',
 ('Shatavari',            None): 'ASPARAGUS RACEMOSUS SHATAVARI) DRY EXTRACT-60_ (BY - LC-230217 - HC_HE_F_2023_O0217.pdf',
 ('Neem',                 None): 'AZADIRACHTA INDICA (NEEM) DRY EXTRACT.pdf',
 ('Bacopa Monnieri',      None): 'BACOPA MONNIERI DRY EXTRACT.pdf',
 ('Berberis Aristata',    None): 'BERBERIS ARISTATA DRY EXTRACT.pdf',
 ('Boswellia Serrata',    None): 'BOSWELLIA SERRATA (SALAI GUGGAL) DRY EXTRACT.pdf',
 ('Green Tea',            None): 'CAMELLIA SINENSIS (GREEN TEA) DRY EXTRACT.pdf',
 ('Centella Asiatica',    None): 'CENTELLA ASIATICA (BRAHMI_GOTU KOLA) DRY EXTRACT.pdf',
 ('Cissus Quadrangularis',None): 'CISSUS QUADRANGULARIS DRY EXTRACT.pdf',
 ('Guggul',               None): 'COMMIPHORA MUKUL (GUGGUL) DRY EXTRACT.pdf',
 ('Amla',            '45% Tannins'): 'EMBLICA OFFICINALIS (AMLA) DRY EXTRACT-45_ BY TITRATION - LC-230236 - HC_HE_F_2023_O0236.pdf',
 ('Fenugreek',            None): 'FENUGREEK DRY EXTRACT.pdf',
 ('Garcinia Cambogia',    None): 'GARCINIA CAMBOGIA (VILAYTI IMLI) DRY EXTRACT.pdf',
 ('Licorice',             None): 'GLYCYRRHIZA GLABRA (MULETHI ) DRY EXTRACT.pdf',
 ('Karela',               None): 'MOMORDICA CHARANTIA (KARELA) DRY EXTRACT.pdf',
 ('Moringa',       '10% Saponins'): 'MORINGA OLEIFERA DRY EXTRACT - 10_ - LC-230288 - HC_HE_F_2023_O0288.pdf',
 ('Moringa',       '25% Saponins'): 'MORINGA EXTRACT DRY EXTRACT - 25_ - LC-230289 - HC_HE_F_2023_O0289.pdf',
 ('Nano Curcumin',        None): 'NANO CURCUMIN DRY EXTRACT-5_ - LC-230271 - HC_HE_F_2023_O0271.pdf',
 ('Tulsi',                None): 'OCIMUM SANCTUM (TULSI) DRY EXTRACT.pdf',
 ('Shilajit',             None): 'SHILAJIT (ASPHALTUM) DRY EXTRACT.pdf',
 ('Arjuna',               None): 'TERMINALIA ARJUNA (ARJUNA) DRY EXTRACT.pdf',
 ('Tribulus Terrestris',  None): 'TRIBULUS TERRESTRIS (GOKHRU) DRY EXTRACT.pdf',
 ('Triphala',             None): 'TRIPHALA DRY EXTRACT.pdf',
 ('Ashwagandha',          None): 'WITHANIA SOMNIFERA (ASHWAGANDHA) DRY EXTRACT.pdf',
 ('Bromelain',            None): 'BROMELAIN DRY EXTRACT.pdf',
}

# DELIBERADAMENTE SIN FICHA:
#   Amla 30%  -> el unico PDF que le tocaria ('PHYLLANTHUS EMBLICA (AMLA)') se
#                contradice a si mismo: se titula "Amla 30% by titration" pero
#                por dentro es Phyllanthus niruri, bitters 5% — o sea, Bhumi Amla.
#                No se publica un documento incoherente.
#   Bhumi Amla-> por lo mismo: su ficha esta archivada con el nombre del Amla.
#   Los aminoacidos, minerales, creatina, clara de huevo, cacao y polidextrosa:
#                el proveedor no ha mandado sus fichas.
