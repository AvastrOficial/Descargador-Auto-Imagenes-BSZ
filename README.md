📂 Proyecto: Descargador Automático de Imágenes — no_deteccion
Este script en Python permite buscar y descargar automáticamente hasta 400 imágenes aleatorias desde DuckDuckGo (motor de búsqueda de imágenes), excluyendo resultados relacionados con medicamentos.
Las imágenes se almacenan en una carpeta llamada no_deteccion.

✨ Características
✅ Descarga hasta 400 imágenes únicas automáticamente.

🖼️ Utiliza palabras clave aleatorias de categorías como naturaleza, tecnología, animales, ciudades y más.

🚫 Filtra y evita imágenes relacionadas con medicamentos o farmacias.

🗂️ Crea automáticamente la carpeta de descarga si no existe.

🌍 Usa DuckDuckGo como fuente de búsqueda de imágenes (sin rastreo, más privacidad).

🛠️ Requisitos
Python 3.7 o superior

Librerías de Python:

bash
Copiar
Editar
pip install duckduckgo-search requests
O crea un requirements.txt:

sql
Copiar
Editar
duckduckgo-search
requests
🚀 ¿Cómo usarlo?
Clona este repositorio o copia el script en tu equipo.

Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecuta el script:

bash
Copiar
Editar
python main.py
Las imágenes se guardarán en la carpeta:

bash
Copiar
Editar
/no_deteccion
📋 ¿Qué hace el script paso a paso?
Paso	Acción
1️⃣	Crea la carpeta no_deteccion si no existe
2️⃣	Selecciona una palabra clave aleatoria (por ejemplo: dog, space, city)
3️⃣	Busca hasta 30 imágenes usando DuckDuckGo
4️⃣	Filtra las URLs que contengan palabras relacionadas a medicamentos
5️⃣	Descarga las imágenes válidas y las guarda como img_1.jpg, img_2.jpg, etc.
6️⃣	Repite hasta llegar a 400 imágenes o hasta que se agoten los intentos

⚠️ Notas
Se realizan pausas de 0.1 segundos entre cada descarga para evitar sobrecarga o bloqueo.

El script reintenta varias veces si alguna búsqueda no arroja resultados.

