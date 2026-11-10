
def afficher_menu():
    print("=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("0. Quitter")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")


def lancer_application():
    taches = []

    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            titre = input("Titre de la tâche : ").strip()

            if titre == "":
                print("Erreur : Le titre ne peut pas être vide.")
            else:
                taches.append(titre)
                print("Tâche ajoutée avec succès.")

        elif choix == "2":
            if not taches:
                print("La liste des tâches est vide.")
            else:
                print("--- Liste des tâches ---")
                for index, tache in enumerate(taches, start=1):
                    print(f"{index}. {tache}")
        elif choix == "3":
            mot_cle = input("Mot-clé à rechercher : ").strip()
            trouve = False

            for index, tache in enumerate(taches, start=1):
                if mot_cle.lower() in tache.lower():
                    print(f"{index}. {tache}")
                    trouve = True

            if not trouve:
                print("Aucune tâche trouvée.")

        elif choix == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")


lancer_application()
