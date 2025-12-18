from openai import OpenAI
from app.config import OPENAI_MODEL

client = OpenAI()  # liest OPENAI_API_KEY aus der Umgebung

def correct_jir_description(payload: str) -> dict:
    resp = client.responses.create(
        model=OPENAI_MODEL,
        input="Korrigiere den Text auf Rechtschreibfehler. Liefere nur den korrigierten Text zurück.: " + payload
    )
    return resp.output_text
