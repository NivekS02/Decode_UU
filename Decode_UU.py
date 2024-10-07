import uu

# Ouvrir le fichier encodé et lire son contenu
with open("C:/Cybersecurity/Root_me/Decode_UU/ch1.txt", "r") as encoded_file:
    # Lire le contenu entier du fichier
    content = encoded_file.read()

# Écrire le contenu dans un fichier temporaire pour le décodage
with open("C:/Cybersecurity/Root_me/Decode_UU/decoded_output.txt", "wb") as decoded_file:
    # Utiliser le module uu pour décoder le contenu
    uu.decode("C:/Cybersecurity/Root_me/Decode_UU/ch1.txt", decoded_file)
