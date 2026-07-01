"""
Finance Tracker - Premier projet
Parcours vers la Data Science appliquée à la finance
"""

def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "="*30)
    print("    FINANCE TRACKER")
    print("="*30)
    print("1. Ajouter une dépense")
    print("2. Voir toutes les dépenses")
    print("3. Voir le total")
    print("4. Quitter")
    print("="*30)

def main():
    """Programme principal"""
    while True:
        afficher_menu()
        
        choix = input("\nVotre choix (1-4) : ")
        
        if choix == "1":
            print("➜ Ajout d'une dépense (à venir)")
            # On ajoutera la fonction plus tard
            
        elif choix == "2":
            print("➜ Liste des dépenses (à venir)")
            # On ajoutera la fonction plus tard
            
        elif choix == "3":
            print("➜ Total des dépenses (à venir)")
            # On ajoutera la fonction plus tard
            
        elif choix == "4":
            print("\n👋 Au revoir ! À bientôt !")
            break
            
        else:
            print("\n❌ Choix invalide. Veuillez entrer 1, 2, 3 ou 4.")
        
        input("\nAppuyez sur Entrée pour continuer...")

# Point d'entrée du programme
if __name__ == "__main__":
    main()