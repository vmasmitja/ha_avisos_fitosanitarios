import requests
from PyPDF2 import PdfFileReader
import io
import logging

_LOGGER = logging.getLogger(__name__)

def extract_text_from_pdf(url):
    response = requests.get(url)
    if response.status_code == 200:
        pdf = PdfFileReader(io.BytesIO(response.content))
        text = ""
        for page_num in range(pdf.getNumPages()):
            page = pdf.getPage(page_num)
            text += page.extract_text()
        return text
    else:
        _LOGGER.error("Error al recuperar el PDF: %s", response.status_code)
        return None

def get_avisos(url, cultivos):
    text = extract_text_from_pdf(url)
    avisos = {}
    nuevos_cultivos = []
    if text:
        for cultivo in cultivos:
            if cultivo.split("-")[0].lower() in text.lower() or cultivo.split("-")[1].split(" ")[0].lower() in text.lower():
                avisos[cultivo] = "Aviso encontrado"
            else:
                avisos[cultivo] = "No hay avisos"

        # Buscar nuevos cultivos
        all_cultivos = re.findall(r'\b[A-Za-zÀ-ÿ]+(?:\s[A-Za-zÀ-ÿ]+)*\b', text)
        for nuevo_cultivo in all_cultivos:
            cultivo_normalizado = nuevo_cultivo.strip().lower().capitalize()
            if cultivo_normalizado not in TIPOS_CULTIVOS.values() and len(cultivo_normalizado) > 3:
                nuevos_cultivos.append(cultivo_normalizado)
                avisos["nuevos_cultivos"] = nuevos_cultivos
    return avisos, url
