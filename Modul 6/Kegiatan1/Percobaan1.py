from PIL import Image, ImageDraw, ImageFont

gambarku = Image.open("C:/Users/dimas/OneDrive/Documents/Matkul sem 5/Prak Fungsi/Modul 6/Kegiatan1/Background/Dome_umm.JPG")
gambarBW = gambarku.convert("L")

draw = ImageDraw.Draw(gambarBW)
font_path = r"C:/Users/dimas/OneDrive/Documents/Matkul sem 5/Prak Fungsi/Modul 6/Kegiatan1/Arial.ttf"
font_size = 50

# Try to load the font
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    # Handle the case where the font file cannot be loaded
    print(f"Error loading font from {font_path}")
    font = ImageFont.load_default()

text = "Nama: Dimas Dzaki Adani \nNIM: 202110370311003"

# Get the size of the text bounding box using the font object
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

# Calculate the center position
center_x = (gambarku.width - text_width) // 2
center_y = (gambarku.height - text_height) // 2

draw.text((center_x, center_y), text, font=font)

gambarBW.save("percobaan_satu.jpg")
gambarBW.show()
