import gradio as gr
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Fonctions de traitement d'image
def load_image(image):
    return image

def apply_negative(image):
    img_np = np.array(image)
    negative = 255 - img_np
    return Image.fromarray(negative)

def binarize_image(image, threshold):
    img_np = np.array(image.convert('L'))
    _, binary = cv2.threshold(img_np, threshold, 255, cv2.THRESH_BINARY)
    return Image.fromarray(binary)

def resize_image(image, width, height):
    return image.resize((width, height))

def rotate_image(image, angle):
    return image.rotate(angle)

# Ajoutez d'autres fonctions pour l'histogramme, le filtrage, Sobel, etc.

# Interface Gradio
def image_processing(image, operation, threshold=128, width=100, height=100, angle=0):
    if operation == "Négatif":
        return apply_negative(image)
    elif operation == "Binarisation":
        return binarize_image(image, threshold)
    elif operation == "Redimensionner":
        return resize_image(image, width, height)
    elif operation == "Rotation":
        return rotate_image(image, angle)
    # Ajouter d'autres conditions pour les autres opérations
    return image

# Interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("## Projet de Traitement d'Image")

    with gr.Row():
        image_input = gr.Image(type="pil", label="Charger Image")
        operation = gr.Radio(["Négatif", "Binarisation", "Redimensionner", "Rotation"], label="Opération")
        threshold = gr.Slider(0, 255, 128, label="Seuil de binarisation", visible=False)
        width = gr.Number(value=100, label="Largeur", visible=False)
        height = gr.Number(value=100, label="Hauteur", visible=False)
        angle = gr.Number(value=0, label="Angle de Rotation", visible=False)

    image_output = gr.Image(label="Image Modifiée")

    submit_button = gr.Button("Appliquer")
    submit_button.click(image_processing, inputs=[image_input, operation, threshold, width, height, angle], outputs=image_output)

# Lancer l'application Gradio
demo.launch()
