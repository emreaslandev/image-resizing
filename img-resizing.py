import os
from PIL import Image

MAX_SIZE = (300, 300)  # Maksimum genişlik ve yükseklik

folder = input("İşlem yapılacak klasörün tam yolunu girin: ").strip()
output_folder = os.path.join(folder, "resizing")
os.makedirs(output_folder, exist_ok=True)  # resizing klasörünü oluştur

def resize_and_save(input_path, output_path):
    with Image.open(input_path) as img:
        img.thumbnail(MAX_SIZE, Image.LANCZOS)
        if img.format == "JPEG":
            img.save(output_path, "JPEG", quality=75, optimize=True)
        elif img.format == "PNG":
            img.save(output_path, "PNG", optimize=True)
        else:
            img.save(output_path)

for filename in os.listdir(folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        name, ext = os.path.splitext(filename)
        output_filename = f"{name}-rsz{ext}"
        input_path = os.path.join(folder, filename)
        output_path = os.path.join(output_folder, output_filename)  # resizing klasörüne kaydet
        resize_and_save(input_path, output_path)
        print(f"{output_filename} kaydedildi.")

print("Tüm resimler yeniden boyutlandırıldı ve kaydedildi.")