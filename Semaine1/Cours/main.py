import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fonction pour charger une image
def load_image():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img.thumbnail((400, 400))  # Redimensionner pour afficher dans Tkinter
    img_tk = ImageTk.PhotoImage(img)
    panel.config(image=img_tk)
    panel.image = img_tk
    return img

# Fonction pour sauvegarder l'image modifiée
def save_image(image):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg")])
    image.save(file_path)

# Fonction pour appliquer un négatif
def apply_negative():
    img_np = np.array(img)
    negative = 255 - img_np
    img_negative = Image.fromarray(negative)
    img_negative_tk = ImageTk.PhotoImage(img_negative)
    panel.config(image=img_negative_tk)
    panel.image = img_negative_tk

# Fonction pour binarisation
def binarize_image(threshold):
    img_np = np.array(img.convert('L'))  # Convertir en niveaux de gris
    _, binary = cv2.threshold(img_np, threshold, 255, cv2.THRESH_BINARY)
    img_binary = Image.fromarray(binary)
    img_binary_tk = ImageTk.PhotoImage(img_binary)
    panel.config(image=img_binary_tk)
    panel.image = img_binary_tk

# Interface Tkinter
root = tk.Tk()
root.title("Projet de Traitement d'Image")

# Ajouter les boutons
load_btn = tk.Button(root, text="Charger Image", command=load_image)
load_btn.pack()

negative_btn = tk.Button(root, text="Appliquer Négatif", command=apply_negative)
negative_btn.pack()

threshold_btn = tk.Button(root, text="Binariser", command=lambda: binarize_image(128))
threshold_btn.pack()

# Panel pour afficher l'image
panel = tk.Label(root)
panel.pack()

# Lancer l'interface
root.mainloop()
