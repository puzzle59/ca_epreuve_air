#10 Afficher le contenu
#Fichier à afficher : jedanselemia.txt
#################################"
import sys
url=sys.argv[1]
try: fichier=open(url,"r")
except FileNotFoundError:
    quit("Le fichier n'existe pas")
print(fichier.read())
fichier.close()
