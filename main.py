import os
import random
import requests
from duckduckgo_search import DDGS
from time import sleep

# Palabras clave excluidas
excluded_keywords = ["pill", "pills", "medicine", "pharmacy", "drug", "capsule"]

# Categorías generales para buscar imágenes
search_terms = [
    "landscape", "car", "dog", "cat", "building", "technology", "robot",
    "space", "forest", "ocean", "mountain", "city", "airplane", "flowers",
    "food", "sports", "bicycle", "animal", "nature", "sunset"
]

# Crear carpeta de destino
output_dir = "no_deteccion"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"📂 Carpeta '{output_dir}' creada.")
else:
    print(f"📂 Carpeta '{output_dir}' ya existe.")

downloaded = 0
max_images = 400
tries = 0

print("🚀 Iniciando descarga de imágenes...")

with DDGS() as ddgs:
    while downloaded < max_images and tries < max_images * 4:
        term = random.choice(search_terms)
        print(f"🔍 Buscando imágenes de: {term}")
        try:
            results = ddgs.images(term, max_results=30)
            results = list(results)  # convertir generator a lista
            if not results:
                print(f"⚠️ No se encontraron imágenes para '{term}'. Reintentando...")
                tries += 1
                continue
            for result in results:
                url = result.get("image", "")
                if not url:
                    continue
                if any(word in url.lower() for word in excluded_keywords):
                    continue
                try:
                    response = requests.get(url, timeout=10)
                    if response.status_code != 200:
                        raise Exception(f"HTTP {response.status_code}")
                    img_data = response.content
                    filename = os.path.join(output_dir, f"img_{downloaded+1}.jpg")
                    with open(filename, "wb") as f:
                        f.write(img_data)
                    downloaded += 1
                    print(f"[{downloaded}/{max_images}] ✅ Imagen guardada: {filename}")
                    if downloaded >= max_images:
                        break
                except Exception as e:
                    print(f"❌ Error descargando {url}: {e}")
                sleep(0.1)
        except Exception as e:
            print(f"❌ Error buscando imágenes para '{term}': {e}")
        tries += 1

print(f"\n✅ Proceso completado. {downloaded} imágenes guardadas en '{output_dir}'.")
