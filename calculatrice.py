import math

def addition(a, b):
  "Fonction pour l'addition"
  return a + b

def soustraction(a, b):
  "Fonction pour la soustraction"
  return a - b

def multiplication(a, b):
  "Fonction pour la multiplication"
  return a * b

def division(a, b):
  "Fonction pour la division"
  return a / b
def main():
  "Fonction principale"
  # Afficher un message d'accueil
  print("Calculatrice Console Python")

  while True:
    # Demander à l'utilisateur de choisir une opération
    operation = input("Choisissez une opération (+, -, *, /, q pour quitter): ")

    # Quitter l'application si l'utilisateur saisit "q"
    if operation == "q":
      break

# Demander à l'utilisateur de saisir les nombres
    nombre_1 = float(input("Entrez le premier nombre: "))
    nombre_2 = float(input("Entrez le deuxième nombre: "))

    # Déterminer l'opération et afficher le résultat
    if operation == "+":
      resultat = addition(nombre_1, nombre_2)
      print(f"{nombre_1} + {nombre_2} = {resultat}")
    elif operation == "-":
      resultat = soustraction(nombre_1, nombre_2)
      print(f"{nombre_1} - {nombre_2} = {resultat}")
    elif operation == "*":
      resultat = multiplication(nombre_1, nombre_2)
      print(f"{nombre_1} * {nombre_2} = {resultat}")
    elif operation == "/":
      resultat = division(nombre_1, nombre_2)
      print(f"{nombre_1} / {nombre_2} = {resultat}")
    else:
      print("Opération invalide!")

# Appeler la fonction principale
if __name__ == "__main__":
  main()
