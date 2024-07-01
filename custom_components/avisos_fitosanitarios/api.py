import openai
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

def get_avisos(api_key, category, cultivos):
    openai.api_key = api_key
    url = f"https://agricultura.gencat.cat/ca/ambits/agricultura/dar_sanitat_vegetal_nou/avisos-fitosanitaris/{category}"
    text = extract_text_from_pdf(url)
    if not text:
        return {}

    avisos = {}
    for cultivo in cultivos:
        prompt = f"Busca información sobre {cultivo} en el siguiente texto: {text}"
        response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=50)
        result = response.choices[0].text.strip()
        avisos[cultivo] = result if result else "No hay avisos"
    
    return avisos
