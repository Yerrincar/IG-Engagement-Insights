import pandas as pd
import os
import time
from CLASIFICADOR import clasifica_post
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def main():
    # Cargamos el CSV con los datos
    df = pd.read_csv(r"C:\Users\Yeray\Desktop\DATA_SCIENCE_ML\IG-Engagemente-Insights\IG-Engagement-Insights\DATA\CT\CT_SOLO_PROMPT.csv")

    os.makedirs("output", exist_ok=True)
    output_path = os.path.join("output", "clasificacion_publicaciones.csv")

    classified_lines = []
    # Encabezado CSV
    header = "id,tipo_de_publicacion,tipo_de_producto,caption"

    for idx, row in df.iterrows():
        post_id = row["id"]
        caption = row["caption"]

        # Llamamos a la función de clasificación
        csv_line = clasifica_post(post_id, caption)
        classified_lines.append(csv_line)

        #Sleep para evitar sobrepasar el límite de solicitudes de la API
        time.sleep(4)
        
    # Guardamos todo en un CSV
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(header + "\n")
        for line in classified_lines:
            f.write(line + "\n")

    print(f"Archivo '{output_path}' generado con éxito.")

if __name__ == "__main__":
    #print("Mi API KEY es:", GEMINI_API_KEY)
    main()
