import gradio as gr
from PIL import Image
import numpy as np
import cv2
from skimage.color import rgb2gray
import PIL.ImageFilter
from scipy.ndimage import convolve
from skimage import morphology

# Fonctions de traitement d'image
#==========================================================================================
# 1. Charger l'image
def load_image(image):
    return image
#==========================================================================================

#==========================================================================================
# Transformer l'image en niveau de gris
def gray(image):
    image = np.array(image)
    image_gris = rgb2gray(image)
    return image_gris
#==========================================================================================

#==========================================================================================
# Transformer en blanc noir
def blanc_noir(image):
    image = np.array(image)
    image_gris = rgb2gray(image)
    image_blanc_noir = np.where(image_gris > 0.5, 0, 1)
    image = (image_blanc_noir * 255).astype(np.uint8)
    return Image.fromarray(image)
#==========================================================================================

#==========================================================================================
# 2. Application d'un négatif à l'image
def apply_negative(image):
    img_np = np.array(image)
    negative = 255 - img_np
    return Image.fromarray(negative)
#==========================================================================================

#==========================================================================================
# 3. Transformation en Rotation
def rotate_image(image, angle):
    return image.rotate(angle, expand=True)
#==========================================================================================

#==========================================================================================
# 4. Application des filtres
def filtrage_image(image, filter_name):
    # Récupérer le filtre en fonction du nom
    filtre_mapping = {
        'Floutage': PIL.ImageFilter.BLUR,
        'Détails': PIL.ImageFilter.DETAIL,
        'Netteté': PIL.ImageFilter.SHARPEN,
        'Effet 3D': PIL.ImageFilter.EMBOSS,
        'Contour': PIL.ImageFilter.FIND_EDGES, # Détecter les contours
        'Floutage Moyen': PIL.ImageFilter.BoxBlur(5),  # Spécifiez le rayon pour BoxBlur
        'Floutage Gaussien': PIL.ImageFilter.GaussianBlur(5)  # Spécifiez le rayon pour GaussianBlur
    }
    
    if filter_name in filtre_mapping:
        filtre = filtre_mapping[filter_name]
        # Appliquer le filtre à l'image
        return image.filter(filtre)
    else:
        raise ValueError(f"Le filtre '{filter_name}' n'existe pas dans les filtres définis.")

#==========================================================================================
# 5. Binarisation de l'image
def binarize_image(image, threshold):
    img_np = np.array(image.convert('L'))
    _, binary = cv2.threshold(img_np, threshold, 255, cv2.THRESH_BINARY)
    return Image.fromarray(binary)

#==========================================================================================
# 6. Redimensionnement de l'image
def resize_image(image, width, height):
    return image.resize((width, height))

#==========================================================================================
# 7. Détecter les contours avec canny:
def detect_contour(image):
    # Transformer l'image en niveau de gris
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    image = cv2.GaussianBlur(image, (5, 5), 0)
    edges = cv2.Canny(image, threshold1=50, threshold2=150)
    return Image.fromarray(edges)

#==========================================================================================
# 8. Détecter les contours avec Sobel:
def detect_contour_sobel(image):
    sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

    sobel_y = np.array([[-1,-2,-1],
                    [0, 0, 0],
                    [1, 2, 1]])


    # Convertir en niveaux de gris
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    # Appliquer les filtres sobel
    sobel_x_img = convolve(image, sobel_x)
    sobel_y_img = convolve(image, sobel_y)

    # Combiner les deux pour obtenir les contours
    sobel_combined = np.hypot(sobel_x_img, sobel_y_img)
    sobel_combined = (sobel_combined / sobel_combined.max()) * 255  # Normaliser
    
    return Image.fromarray(sobel_combined.astype(np.uint8))

#==========================================================================================
# 9. Transformation morphologique : erosion
def morphologies_erosion(image):
    # Convertir en niveaux de gris
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    erosion = morphology.binary_erosion(image = image,  footprint=morphology.disk(1))
    return Image.fromarray(erosion.astype(np.uint8))

#==========================================================================================
# 10. Transformation morphologique : dilatation
def morphologies_dilatation(image):
    # Convertir en niveaux de gris
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    dilation = morphology.binary_dilation(image=image,  footprint=morphology.disk(1))
    return Image.fromarray(dilation.astype(np.uint8))
    
#==========================================================================================
# Interface Gradio
def image_processing(image, operation, filter_name, threshold=128, width=100, height=100, angle=0):
    if operation == "Négatif":
        return apply_negative(image)
    elif operation == 'Niveau de Gris':
        return gray(image)
    elif operation == "Blanc Noir":
        return blanc_noir(image)
    elif operation == "Binarisation":
        return binarize_image(image, threshold)
    elif operation == "Redimensionner":
        return resize_image(image, width, height)
    elif operation == "Rotation":
        return rotate_image(image, angle)
    elif operation == "Filtrage":
        return filtrage_image(image, filter_name)
    elif operation == "Contour Pro (Canny)":
        return detect_contour(image)
    elif operation == "Contour Pro (Sobel)":
        return detect_contour_sobel(image)
    elif operation == "Erosion":
        return morphologies_erosion(image)
    elif operation == "Dilatation":
        return morphologies_dilatation(image)
    return image

#==========================================================================================
# Interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("## APPLICATION DE TRAITEMENT DES IMAGES")

    with gr.Row():
        image_input = gr.Image(type="pil", label="Charger Image")
        operation = gr.Radio(["Négatif", "Binarisation", "Redimensionner", 
                              "Rotation", "Niveau de Gris", "Blanc Noir", 
                              "Filtrage", "Contour Pro (Canny)", "Contour Pro (Sobel)",
                              "Erosion", "Dilatation"], label="Opération")
        dict_options = {
            'Floutage': 'Floutage', 
            'Détails': 'Détails', 
            'Netteté': 'Netteté', 
            'Effet 3D': 'Effet 3D',
            'Contour': 'Contour', 
            'Floutage Moyen': 'Floutage Moyen', 
            'Floutage Gaussien': 'Floutage Gaussien',
            
        }
        options = gr.Dropdown(choices=list(dict_options.keys()), label="Choisissez votre filtre", visible=True)
        threshold = gr.Slider(0, 255, 128, label="Seuil de binarisation", visible=False)
        width = gr.Number(value=100, label="Largeur", visible=False)
        height = gr.Number(value=100, label="Hauteur", visible=False)
        angle = gr.Number(value=360, label="Angle de Rotation", visible=True)

    image_output = gr.Image(label="Image Modifiée")

    submit_button = gr.Button("Appliquer")
    submit_button.click(image_processing, inputs=[image_input, operation, options, threshold, width, height, angle], outputs=image_output)

#==========================================================================================
# Lancer l'application Gradio
demo.launch()
