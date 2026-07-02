"""
Finance Tracker - Premier projet
Parcours vers la Data Science appliquée à la finance
"""

def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "="*30)
    print("     FINANCE TRACKER")
    print("="*30)
    print("1. Ajouter une dépense")
    print("2. Ajouter des revenus")
    print("3. Voir toutes les dépenses et le total")
    print("4. Voir toutes les recettes et le total")
    print("5. Faire le point sur le solde")
    print("6. Quitter")
    print("="*30)

def ajouter_montant(operations):
    """Ajoute une dépense à la liste selon la catégorie, le montant et la date"""
    print("\n--- Ajout d'un montant ---")
    categorie = input("Catégorie : ")
    while True:
        try:
            montant = float(input("Montant(en euros): "))
            if montant < 0:
                print(" Le montant ne peut pas être négatif. Veuillez entrer un nombre positif.")
                continue
            break
        except ValueError:
            print(" Montant invalide. Veuillez entrer un nombre.")
    date_operation = input("Date(DD/MM/YYYY): ")
    
    operation = {"categorie": categorie, "montant": montant, "date": date_operation}

    operations.append(operation)
    return operation

def calculer_total(operations):
    """Calcule le total des opérations"""
    if not operations:
        print(f"Aucune {type_operation} enregistrée.")
        return
    total = sum(operation["montant"] for operation in operations)
    return total

def afficher_operations(operations, type_operation):
    """Affiche les opérations et le total"""
    if not operations:
        print(f"Aucune {type_operation} enregistrée.")
        return
    print(f"\n--- Liste des {type_operation} ---")
    for operation in operations:
        print(f"Catégorie : {operation['categorie']}, Montant : {operation['montant']:.2f}€, Date : {operation['date']}")
    print(f"Total des {type_operation} : {calculer_total(operations):.2f}€")

def main():
    """Programme principal"""
    depenses = []  # Liste pour stocker les dépenses
    recettes = []  # Liste pour stocker les recettes
    print("Bienvenue dans le Finance Tracker !")
    print("Vous pouvez suivre vos dépenses et vos recettes facilement.")
    print("Veuillez choisir une option dans le menu ci-dessous :")
    while True:
        afficher_menu()
        
        choix = input("\nVotre choix (1-6) : ")
        
        if choix == "1":
            print(" Ajout d'une dépense ")
            depense = ajouter_montant(depenses)
            print(f"Dépense ajoutée : {depense['categorie']}, Montant : {depense['montant']:.2f}, Date : {depense['date']}")

        elif choix == "2":
            print(" Ajout d'un revenu ou d'une recette ")
            recette = ajouter_montant(recettes)
            print(f"Recette ajoutée : {recette['categorie']}, Montant : {recette['montant']:.2f}, Date : {recette['date']}")

        elif choix == "3":
            afficher_operations(depenses, "dépenses")
 
        elif choix == "4":
            afficher_operations(recettes, "recettes")

        elif choix == "5":
            total_depenses = calculer_total(depenses)
            total_recettes = calculer_total(recettes)
            solde = total_recettes - total_depenses
            print(f"Depenses totales : {total_depenses:.2f}€", f"Recettes totales : {total_recettes:.2f}€")
            print(f"Votre solde actuel : {solde:.2f}€")

        elif choix == "6":
            print("\n👋 Au revoir ! À bientôt !")
            break
            
        else:
            print("\n❌ Choix invalide. Veuillez entrer 1, 2, 3, 4, 5 ou 6.")
        
        input("\nAppuyez sur Entrée pour continuer...")

# Point d'entrée du programme
if __name__ == "__main__":
    main()