from PIL import Image
import os

# TODO 1: Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
# path gambar background yang sesuai
background_image = Image.open("C:/Users/dimas/OneDrive/Documents/Matkul sem 5/Prak Fungsi/Modul 6/Kegiatan2/Background/Atas_umm.JPG")  
overlay_image = Image.open("C:/Users/dimas/OneDrive/Documents/Matkul sem 5/Prak Fungsi/Modul 6/Kegiatan2/Overlay/logo_umm.png")

# TODO 2: Periksa apakah overlay image memiliki alpha channel (transparency)
if 'A' in overlay_image.getbands():
    # Buat mask dari alpha channel dan gunakan sebagai alpha channel pada gambar overlay
    alpha = overlay_image.split()[3]
    overlay_image = overlay_image.convert('RGB')
    overlay_image.putalpha(alpha)

# TODO 3: (optional) Perkecil ukuran gambar overlay menggunakan method resize()
max_size = (300, 300)
overlay_image.thumbnail(max_size)

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (background_image.width - overlay_image.width) // 2
y_center = 10

# TODO 4: Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center), overlay_image)

# TODO 5: Simpan gambar hasil edit ke dalam file
  # create the output folder if it doesn't exist
output_file_path = ("hasil_edit.jpg")
background_image.save(output_file_path)

# TODO 6: Tampilkan gambar dari file
os.system(output_file_path)
