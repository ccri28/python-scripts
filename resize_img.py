# script che data in ingresso una cartella di immagini, crea un'altra cartella con le immagini ridimensionate in base alle dimensione in px fornite
# conviene crearsi una venv e installare Pillow attraverso il comando "pip install pillow"

import os
from PIL import Image

# Imposta la cartella contenente le immagini da ridimensionare
cartella_in = ""  # Sostituisci con il percorso reale della tua cartella

# Imposta la cartella di destinazione per le immagini ridimensionate
cartella_out = ""  # Sostituisci con il percorso reale della tua cartella di output

# Verifica se la cartella di output esiste, se no creala
if not os.path.exists(cartella_out):
    os.makedirs(cartella_out)

# Cicla attraverso ogni file nella cartella di input
for filename in os.listdir(cartella_in):
    # Ottieni il percorso completo del file immagine
    filepath = os.path.join(cartella_in, filename)

    # Controlla se il file è un'immagine
    if os.path.isfile(filepath) and filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff')):
        # Apri l'immagine con PIL
        image = Image.open(filepath)

        # Ridimensiona l'immagine a 100x100 pixel mantenendo le proporzioni
        # Nelle versioni di Pillow successive alla 9.5.0, l'algoritmo di ridimensionamento antialias è stato integrato nella costante LANCZOS o Resampling.LANCZOS
        resized_image = image.resize((100, 100), Image.LANCZOS)

        # Salva l'immagine ridimensionata nella cartella di output con lo stesso nome del file originale
        resized_image.save(os.path.join(cartella_out, filename))

        print(f"Immagine ridimensionata: {filename}")