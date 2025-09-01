import os
import tempfile

# Crée un fichier temporaire avec le texte
chemin = os.path.join(tempfile.gettempdir(), "note.txt")
with open(chemin, "w", encoding="utf-8") as f:
    f.write("Bonjour Léopold")

# Ouvre ce fichier directement dans le Bloc-notes
os.system(f'notepad "{chemin}"')
