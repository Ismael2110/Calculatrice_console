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


