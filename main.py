#
# Chaque exercice est codé dans un ficher Python séparé
# La fonction main() permet de choisir l'exercice
#
#####  Ne pas modifier ce fichier  #####
#

import subprocess  # module permettant des appels système

def main():
  print("# Programmation événementielle avec Python et Tkinter :")
  print("    1. Exemple 1 : fenêtre et un bouton")
  print("    2. Exemple 2 : fenêtre et un bouton actif")
  print("    3. Exemple 3 : fenêtre avec des sliders")
  print("    4. Exercice ")

  while True :
    choix = input("\nVotre choix > ")
    if choix == '1':
      subprocess.call(['python', 'exemple_1.py'])
    elif choix == '2':
      subprocess.call(['python', 'exemple_2.py'])
    elif choix == '3':
      subprocess.call(['python', 'exemple_3.py'])
    elif choix == '4':
      subprocess.call(['python', 'exercice.py'])
    elif choix == '0' or choix == '':
      break
    else :
      print("Choix invalide")

    # À partir de Python 3.10, on peut utiliser 'match' et 'case'
    # (Structural Pattern Matching)
    # au lieu de la structure conditionnelle if ... elif ... else

##########################################################################################
# Programme principal

main()
