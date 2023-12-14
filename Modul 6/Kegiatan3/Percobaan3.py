from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan Pillow
image = Image.open("C:/Users/dimas/OneDrive/Documents/Matkul sem 5/Prak Fungsi/Modul 6/Kegiatan3/Background/UMM.jpg")  # Ganti dengan path gambar yang sesuai

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
brightness_factor = 1.5
contrast_factor = 1.2

enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(brightness_factor)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(contrast_factor)

# TODO 3: Simpan gambar hasil edit
final_image.save("brightness_contrast_image.jpg")

# TODO 4: Tampilkan
final_image.show()


