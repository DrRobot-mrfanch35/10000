# Créé par François Costard
import random

# Définissez le nombre de joueurs et le score cible pour gagner
nombre_joueurs = 2
score_cible = 10000

# Créez une liste de joueurs avec leur nom et leur score
joueurs = []
for i in range(nombre_joueurs):
    nom = input(f"Entrez le nom du joueur {i + 1}: ")
    score = 0
    joueurs.append({"nom": nom, "score": score})


# Définissez les règles du jeu
def calculer_points(des):
    points = 0
    if len(set(des)) == 1:
        # Si tous les dés sont identiques, ajoutez le triple de la valeur de chaque dé
        points = des[0] * 3
    elif len(set(des)) == 2:
        # Si deux dés sont identiques, ajoutez le double de la valeur de chaque dé
        points = des[0] * 2
    elif len(set(des)) == 3:
        # Si trois dés sont identiques, ajoutez la valeur de chaque dé
        points = des[0]
    return points


# Créez une boucle qui permet à chaque joueur de jouer à son tour
tour = 0
while True:
    # Récupérez le joueur courant
    joueur = joueurs[tour % nombre_joueurs]

    # Demandez au joueur s'il souhaite lancer les dés
    lancer = input(f"{joueur['nom']}, souhaitez-vous lancer les dés? (o/n) ")
    if lancer == "n":
        # Si le joueur ne veut pas lancer les dés, passer au joueur suivant
        tour += 1
        continue

    # Simulez le lancer de dés et récupérez la combinaison obtenue
    des = [random.randint(1, 6) for _ in range(6)]
    print(f"Vous avez obtenu: {des}")

    # Calculer les points obtenus avec la combinaison de dés
    points = calculer_points(des)
    print(f"Vous avez obtenu {points} points.")
    joueur["score"] += points

    # Demandez au joueur s'il souhaite rejouer
    rejouer = input(f"{joueur['nom']}, souhaitez-vous rejouer? (o/n) ")
    while rejouer == "o":
        # Demandez au joueur quels dés il souhaite rejouer
        dés_à_rejouer = input(f"{joueur['nom']}, quels dés souhaitez-vous rejouer? (exemple: 1 3 4) ")
        dés_à_rejouer = [int(dé) for dé in dés_à_rejouer.split()]

        # Rejouez les dés sélectionnés et mettez à jour la combinaison
        for i, dé in enumerate(dés_à_rejouer):
            des[dé - 1] = random.randint(1, 6)

        # Affichez la nouvelle combinaison obtenue
        print(f"Vous avez obtenu: {des}")

        # Calculer les points obtenus avec la nouvelle combinaison de dés
        points = calculer_points(des)
        print(f"Vous avez obtenu {points} points.")

        # Si le joueur atteint ou dépasse le score cible, il a gagné
        if joueur["score"] + points >= score_cible:
            print(f"Félicitations {joueur['nom']}, vous avez gagné!")
            break

        # Demandez au joueur s'il souhaite rejouer
        rejouer = input(f"{joueur['nom']}, souhaitez-vous rejouer? (o/n) ")

    # Ajoutez les points au score du joueur
    joueur["score"] += points

    # Passer au joueur suivant
    tour += 1
