import random

couleurs =["R", "V", "B", "J", "M", "N"]
nb_tentatives = 12
nb_code = 4


def generer_code():

    code = []

    for i in range(nb_code):
        couleur = random.choice(couleurs)
        code.append(couleur)

    return code


def demander_proposition():
    while True:
        proposition = input(
            f"\nEntrez une combinaison de {nb_code} couleurs : "
        )

        if len(proposition) != nb_code:
            print(f"Veuillez entrer exactement {nb_code} couleurs.")
            continue

        if not all(couleur in couleurs for couleur in proposition):
            print("Veuillez entrer uniquement des lettres valides.")
            continue

        return list(proposition)


def comparer_codes(code_secret, proposition):
    bien_place = sum(
        1 for i in range(nb_code) if code_secret[i] == proposition[i]
    )

    mal_place = 0
    for couleur in proposition:
        if couleur in code_secret:
            mal_place += 1
    mal_place -= bien_place

    return bien_place, mal_place


def jouer_partie():
    code_secret = generer_code()
    tentatives = 0

    print("\n=== Nouvelle Partie ===")
    print("\nCouleurs disponibles :")
    print( 
    "\nR = Rouge",
    "\nV = Vert",
    "\nB = Bleu",
    "\nJ = Jaune",
    "\nM = Mauve",
    "\nN = Noir")

    while tentatives < nb_tentatives:
        proposition = demander_proposition()
        tentatives += 1

        bien_place, mal_place = comparer_codes(code_secret, proposition)

        print(
            f"{bien_place} bien placé(s), "
            f"{mal_place} mal placé(s)."
        )

        if bien_place == nb_code:
            score = nb_tentatives - tentatives
            print(f"Vous avez trouvé le code vous avez un score de {score} ")
           
    print(f"Vous avez utilisé toutes vos tentatives. Le code était : {''.join(code_secret)}")
    return 0


jouer_partie()

