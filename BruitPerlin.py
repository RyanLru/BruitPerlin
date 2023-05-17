# On va coder le bruit de Perlin en 2D
# On va afficher le bruit de Perlin en 2D avec matplotlib

# Importation des modules
import numpy as np
import matplotlib.pyplot as plt
import random
import math

# Fonction de bruit de Perlin
def bruitPerlin2D(taille, nbOctaves, persistance, lacunarite):

    # Création de la matrice de bruit
    bruit = np.zeros((taille, taille))

    # On va générer les différentes fréquences de bruit
    for octave in range(nbOctaves):

        # On va générer une fréquence de bruit
        frequence = 2 ** octave

        # On va générer le bruit pour cette fréquence
        bruitFrequence = bruit2D(taille, frequence)

        # On va ajouter ce bruit à la matrice de bruit
        bruit += bruitFrequence * persistance ** octave

    # On retourne la matrice de bruit
    return bruit

# Fonction de bruit 2D
def bruit2D(taille, frequence):

        # Création de la matrice de bruit
        bruit = np.zeros((taille, taille))

        # On va générer le bruit pour chaque pixel
        for x in range(taille):
            for y in range(taille):

                # On va générer un bruit pour ce pixel
                bruit[x, y] = bruitPixel2D(x, y, taille, frequence)

        # On retourne la matrice de bruit
        return bruit

# Fonction de bruit de Perlin pour un pixel
def bruitPixel2D(x, y, taille, frequence):

        # On va générer un bruit pour ce pixel
        bruit = 0

        # On va générer les 4 coins du carré
        coin1 = bruitSimple2D(x, y, taille, frequence)
        coin2 = bruitSimple2D(x + 1, y, taille, frequence)
        coin3 = bruitSimple2D(x, y + 1, taille, frequence)
        coin4 = bruitSimple2D(x + 1, y + 1, taille, frequence)

        # On va interpoler les 4 coins
        bruit += interpolationBilineaire(coin1, coin2, coin3, coin4, x, y, taille)

        # On retourne le bruit
        return bruit

# Fonction de bruit simple 2D
def bruitSimple2D(x, y, taille, frequence):

            # On va générer un bruit pour ce pixel
            bruit = 0

            # On va générer un bruit pour ce pixel
            bruit = random.uniform(-1, 1)

            # On retourne le bruit
            return bruit

# Fonction d'interpolation bilinéaire
def interpolationBilineaire(coin1, coin2, coin3, coin4, x, y, taille):

        # On va calculer les coordonnées du point
        x = x / taille
        y = y / taille

        # On va calculer les valeurs interpolées
        valeur1 = coin1 * (1 - x) + coin2 * x
        valeur2 = coin3 * (1 - x) + coin4 * x
        valeur = valeur1 * (1 - y) + valeur2 * y

        # On retourne la valeur interpolée
        return valeur



# On code une fonction pour générer le bruit de Perlin en 2D
def BruitPerlin(taille, nbOctaves, persistance, lacunarite):
    # On affiche le bruit de Perlin
    taille = 100  # Taille de l'image
    nbOctaves = 4  # Nombre d'octaves qui représente la fréquence du bruit
    persistance = 0.5  # Persistance qui représente l'atténuation du bruit
    lacunarite = 1.5  # Lacunarité qui représente l'augmentation de la fréquence du bruit

    bruit = bruitPerlin2D(taille, nbOctaves, persistance, lacunarite)


    return bruit

