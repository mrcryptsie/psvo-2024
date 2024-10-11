
# Application de traitement d'images

Ce projet est une application interactive de traitement d'images développée en utilisant **Gradio**, une bibliothèque Python permettant de créer facilement des interfaces utilisateur, ainsi que plusieurs bibliothèques de traitement d'images comme PIL, NumPy, OpenCV, et skimage. Elle permet d'appliquer différentes transformations et filtres sur les images téléchargées.

## Fonctionnalités

1. **Chargement d'une image**  
L'application permet de charger des images au format PIL depuis l'interface utilisateur, prêtes à être transformées par l'utilisateur.

2. **Traitement d'image en niveaux de gris**  
La fonction permet de convertir une image en niveaux de gris pour simplifier les analyses visuelles et réduire les informations de couleur.

3. **Transformation en noir et blanc**  
Une transformation en binaire qui convertit l'image en seulement deux couleurs : blanc et noir, en fonction d'un seuil prédéfini.

4. **Négatif de l'image**  
L'application permet d'appliquer un filtre de négatif, inversant les couleurs de l'image.

5. **Rotation de l'image**  
Cette fonctionnalité permet de faire pivoter une image selon un angle défini par l'utilisateur.

6. **Filtres d'image**  
L'application propose plusieurs filtres prédéfinis que l'utilisateur peut appliquer sur l'image, tels que :
    - **Floutage** : Applique un effet de flou pour lisser l'image.
    - **Détails** : Accentue les détails visibles.
    - **Netteté** : Améliore la clarté de l'image.
    - **Effet 3D** : Ajoute un effet d'embossage 3D.
    - **Contour** : Détecte les contours de l'image.

7. **Binarisation**  
Permet de convertir l'image en binaire (noir et blanc) à l'aide d'un seuil ajustable pour accentuer ou réduire les détails.

8. **Redimensionnement**  
Permet à l'utilisateur de redimensionner l'image en spécifiant la largeur et la hauteur souhaitées.

9. **Détection des contours**  
L'application offre deux méthodes pour détecter les contours dans une image :
    - **Canny** : Utilisation de l'algorithme de détection de contours de Canny.
    - **Sobel** : Utilisation de filtres Sobel pour la détection des contours horizontaux et verticaux.

10. **Transformations morphologiques**  
Deux types de transformations morphologiques sont disponibles :
    - **Érosion** : Permet de rétrécir les éléments blancs dans une image binaire.
    - **Dilatation** : Permet d'élargir les éléments blancs.

## Comment utiliser l'application

1. **Charger une image** : L'utilisateur doit sélectionner une image depuis son appareil.
2. **Choisir une opération** : L'utilisateur choisit l'opération qu'il souhaite appliquer à l'image via une interface conviviale.
3. **Appliquer les filtres** : Des filtres spécifiques peuvent être appliqués selon le type de transformation choisie (ex. : rotation, binarisation, etc.).
4. **Voir le résultat** : Une fois l'opération terminée, l'image transformée sera affichée dans l'interface.

## Technologies utilisées

- **Gradio** : Pour la création de l'interface utilisateur simple et interactive.
- **PIL** et **NumPy** : Pour la manipulation d'images.
- **OpenCV** : Pour les transformations avancées et la détection de contours.
- **skimage** : Pour les transformations morphologiques et le traitement en niveaux de gris.
