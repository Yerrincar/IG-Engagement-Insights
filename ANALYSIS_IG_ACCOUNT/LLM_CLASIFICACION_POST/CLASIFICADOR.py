import os
import requests
from dotenv import load_dotenv
from PROMPT import prompt_completo, prompt_simple 

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# Ajusta si tu modelo es 'gemini-1.5-flash' o el que corresponda
GEMINI_MODEL = "gemini-1.5-flash"

def clasifica_post(post_id, caption):
    """
    Llama a la API de PaLM/Gemini para clasificar UN SOLO post.
    Recibe:
      - post_id: identificador (int o string)
      - caption: texto de la publicación

    Devuelve un string con el formato:
      "id,tipo_de_publicacion,tipo_de_producto,caption"
    """

    if not GEMINI_API_KEY:
        print("ERROR: No se encontró la variable API_KEY en .env")
        # Puedes o devolver un error, o un string 'error' para tus columnas
        return f"{post_id},error,error,{caption}"

    # Prepara el prompt para un solo post
    prompt_text = f"""
Eres un especialista en clasificar publicaciones de Instagram.

Tengo una sola publicación con:
id: {post_id}
caption: "{caption}"

Debes devolverme en CSV una sola línea con 4 columnas:
id,tipo_de_publicacion,tipo_de_producto,caption

Reglas:
1. 'tipo_de_publicacion' puede ser: "proceso de creacion", "novedades", "promocion" o "libros" si habla acerca de libros en general etc.
2. 'tipo_de_producto' puede ser: "velas", "marcapaginas", "fundas", "sujetapaginas", "libros", "multitipo" (si hay varios productos a la vez o no se pudo clasificar).
3. Si la publicación habla de varias cosas, elige la categoría predominante.
4. Devuelve exclusivamente la línea CSV (sin texto adicional).
5. Si no puedes clasificar, pon "error" en esas columnas.

Ejemplo de salida para un post:
1,novedades,velas,"Esta es la descripción..."

Ahora, clasifica la publicación dada:
"""

    # Endpoint de la API de PaLM/Gemini
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt_text}
                ]
            }
        ]
    }
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            print("ERROR al llamar a la API:", response.status_code, response.text)
            # Si hay error, devolvemos algo en CSV con "error"
            return f"{post_id},error,error,{caption}"

        response_json = response.json()
        csv_line = response_json["candidates"][0]["content"]["parts"][0]["text"]

        # En caso de que no venga bien formateado, maneja la excepción
        if not csv_line.strip():
            return f"{post_id},error,error,{caption}"

        csv_line = csv_line.strip()

        return csv_line

    except Exception as e:
        print("ERROR al invocar la API de PaLM/Gemini:", str(e))
        return f"{post_id},error,error,{caption}"
