# On récupère le bruit de Perlin pour colorier la carte
import BruitPerlin
import matplotlib.pyplot as plt

taille = 512 # Taille de la carte
nbOctaves = 128 # Nombre d'octaves qui représente la fréquence du bruit
persistance = 1 # Persistance qui représente l'atténuation du bruit
lacunarite = 0 # Lacunarité qui représente l'augmentation de la fréquence du bruit

# On récupère le bruit de Perlin pour colorier la carte
bruit = BruitPerlin.BruitPerlin(taille, nbOctaves, persistance, lacunarite)

# On va colorier la carte en fonction du bruit

def coloriage(bruit):
    zone = 16
    # On va colorier la carte en fonction du bruit
    for x in range(len(bruit[0])):
        for y in range(len(bruit[1])):

            # On fait la moyenne des valeurs dans une zone de 32x32
            # On verifie que la zone est dans la carte (pas de débordement)
            if x + zone <= len(bruit[0]) and y + zone <= len(bruit[1]):
                valeur = 0
                for i in range(zone):
                    for j in range(zone):
                        valeur += bruit[x + i, y + j]
                valeur = valeur / (zone * zone)

            bruit[x,y] = valeur

    plt.imshow(bruit, cmap = 'viridis')
    plt.show()

# On colorie la carte
coloriage(bruit)