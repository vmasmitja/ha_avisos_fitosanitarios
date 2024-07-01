DOMAIN = "avisos_fitosanitarios"

PDF_URLS = {
    "catalunya": {
        "leñosos": "https://agricultura.gencat.cat/web/.content/03-agricultura/sanitat-vegetal/avisos-fitosanitaris/avisos_campanyes/07-juliol/enllacos-documents/fitxers-binaris/07-avisos-cultius-llenyosos.pdf",
        "hortícolas": "https://agricultura.gencat.cat/web/.content/03-agricultura/sanitat-vegetal/avisos-fitosanitaris/avisos_campanyes/07-juliol/enllacos-documents/fitxers-binaris/07-avisos-horticoles.pdf",
        "extensivos": "https://agricultura.gencat.cat/web/.content/03-agricultura/sanitat-vegetal/avisos-fitosanitaris/avisos_campanyes/07-juliol/enllacos-documents/fitxers-binaris/07-avisos-cultivos-extensivos.pdf",
        "espacios_verdes": "https://agricultura.gencat.cat/web/.content/03-agricultura/sanitat-vegetal/avisos-fitosanitaris/avisos_campanyes/07-juliol/enllacos-documents/fitxers-binaris/07-avisos-espacios-verdes.pdf"
    }
}

TIPOS_CULTIVOS = {
    "leñosos": ["Viña-Vinya (Vitis vinifera)", "Olivo-Olivera (Olea europaea)", "Almendro-Ametller (Prunus dulcis)"],
    "hortícolas": [
        "Tomate-Tomàquet (Solanum lycopersicum)", 
        "Pimiento-Pebroter (Capsicum annuum)", 
        "Calabacín-Carbassó (Cucurbita pepo)", 
        "Judía verde-Mongeta (Phaseolus vulgaris)", 
        "Puerro-Porro (Allium ampeloprasum var. porrum)", 
        "Col (Brassica oleracea var. capitata)", 
        "Coliflor (Brassica oleracea var. botrytis)", 
        "Patata-Patata (Solanum tuberosum)", 
        "Fresa-Maduixa (Fragaria x ananassa)"
    ],
    "extensivos": [
        "Maíz-Blat de moro (Zea mays)", 
        "Girasol-Gira-sol (Helianthus annuus)", 
        "Trigo-Blat (Triticum spp.)"
    ],
    "espacios_verdes": [
        "Plátano de sombra-Plataner (Platanus x hispanica)", 
        "Césped-Gespa (Poaceae)"
    ]
}
