import os  # Importă modulul pentru lucrul cu sistemul de operare
import numpy as np  # Importă NumPy pentru lucrul cu matrice și vectori
from PIL import Image, ImageEnhance, ImageFilter  # Importă modulele din PIL (Python Imaging Library) pentru manipularea imaginilor
import random  # Importă modulul pentru lucrul cu numere aleatoare

input_dir = r"B:\LICENTA\img"  # Directorul de intrare pentru imagini
output_dir = r"B:\LICENTA\img_output"  # Directorul de ieșire pentru imagini procesate

if not os.path.exists(output_dir):  # Verifică dacă directorul de ieșire nu există
    os.makedirs(output_dir)  # Dacă nu există, creează-l

def save_image(image, base_name, augmentation_type, index):
    """Funcție pentru salvarea imaginii procesate în directorul de ieșire."""
    output_path = os.path.join(output_dir, f"{base_name}_{augmentation_type}_{index}.jpg")
    image.save(output_path)

def resize_image(image, base_name):
    """Funcție pentru redimensionarea imaginii."""
    for i in range(1):  # Iterează de 1000 de ori pentru a genera multiple imagini redimensionate
        resized_image = image.resize((640, 640))  # Redimensionează imaginea la dimensiunea specificată
        save_image(resized_image, base_name, "resize", i)  # Salvează imaginea redimensionată

def adjust_hue(image, base_name):
    """Funcție pentru ajustarea nuanței imaginii."""
    for i in range(1):  # Iterează de 1000 de ori pentru a genera multiple imagini cu nuanțe ajustate
        hue_factor = random.uniform(-0.03, 0.03)  # Factorul de ajustare al nuanței
        hsv_image = image.convert('HSV')  # Convertă imaginea în modul de culoare HSV
        np_hsv = np.array(hsv_image)  # Convertă imaginea HSV într-un array NumPy
        np_hsv[..., 0] = (np_hsv[..., 0] + hue_factor * 255) % 255  # Ajustează canalul H (nuanța)
        new_image = Image.fromarray(np_hsv, 'HSV').convert('RGB')  # Convertă array-ul NumPy înapoi la imagine RGB
        save_image(new_image, base_name, "hue", i)  # Salvează imaginea cu nuanța ajustată

def adjust_saturation(image, base_name):
    """Funcție pentru ajustarea saturației imaginii."""
    for i in range(1):  # Iterează de 1000 de ori pentru a genera multiple imagini cu saturație ajustată
        enhancer = ImageEnhance.Color(image)  # Obține un obiect pentru ajustarea saturației
        saturation_factor = random.uniform(0.75, 1.25)  # Factorul de ajustare al saturației
        new_image = enhancer.enhance(saturation_factor)  # Aplică ajustarea saturației
        save_image(new_image, base_name, "saturation", i)  # Salvează imaginea cu saturația ajustată

def adjust_brightness(image, base_name):
    """Funcție pentru ajustarea luminozității imaginii."""
    for i in range(1):  # Iterează de 1000 de ori pentru a genera multiple imagini cu luminozitate ajustată
        enhancer = ImageEnhance.Brightness(image)  # Obține un obiect pentru ajustarea luminozității
        brightness_factor = random.uniform(0.85, 1.15)  # Factorul de ajustare al luminozității
        new_image = enhancer.enhance(brightness_factor)  # Aplică ajustarea luminozității
        save_image(new_image, base_name, "brightness", i)  # Salvează imaginea cu luminozitatea ajustată

def apply_blur(image, base_name):
    """Funcție pentru aplicarea blur-ului (încețosării) imaginii."""
    for i in range(1):  # Iterează de 1000 de ori pentru a genera multiple imagini cu blur aplicat
        blur_radius = random.uniform(0, 0.5)  # Raza blur-ului
        new_image = image.filter(ImageFilter.GaussianBlur(blur_radius))  # Aplică filtrul Gaussian Blur
        save_image(new_image, base_name, "blur", i)  # Salvează imaginea cu blur aplicat

def add_noise(image, base_name):
    """Funcție pentru adăugarea de zgomot la imagine."""
    for i in range(1):  # Iterează de 1000 de ori pentru a genera multiple imagini cu zgomot adăugat
        np_image = np.array(image)  # Convertă imaginea într-un array NumPy
        noise_factor = random.uniform(0, 93 )  # Factorul de zgomot
        noise = np.random.normal(0, noise_factor, np_image.shape)  # Generează zgomot Gaussian
        noisy_image = np.clip(np_image + noise, 0, 255).astype(np.uint8)  # Aplică zgomotul și ajustează la valori între 0 și 255
        new_image = Image.fromarray(noisy_image)  # Convertă array-ul NumPy înapoi la imagine
        save_image(new_image, base_name, "noise", i)  # Salvează imaginea cu zgomot adăugat

def process_images():
    """Funcție principală pentru procesarea imaginilor din directorul de intrare."""
    for file_name in os.listdir(input_dir):  # Iterează prin fișierele din directorul de intrare
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):  # Verifică dacă fișierul este o imagine
            image_path = os.path.join(input_dir, file_name)  # Construiește calea completă către imagine
            image = Image.open(image_path)  # Deschide imaginea folosind PIL
            base_name = os.path.splitext(file_name)[0]  # Extrage numele de bază al fișierului (fără extensie)
            resize_image(image, base_name)  # Aplică funcția de redimensionare
            adjust_hue(image, base_name)  # Aplică funcția de ajustare a nuanței
            adjust_saturation(image, base_name)  # Aplică funcția de ajustare a saturației
            adjust_brightness(image, base_name)  # Aplică funcția de ajustare a luminozității
            apply_blur(image, base_name)  # Aplică funcția de aplicare a blur-ului
            add_noise(image, base_name)  # Aplică funcția de adăugare de zgomot

if __name__ == "__main__":
    process_images()  # Începe procesarea imaginilor atunci când scriptul este rulat
