from PIL import Image

print("Hello World!")
# Charger l'image du plateau d'échecs
image = Image.open("plateau.png")

# Convertir l'image en niveaux de gris
image_grayscale = image.convert("L")

# Seuils de couleur pour la détection des pièces
white_threshold = 200
black_threshold = 50

# Détection des pièces
piece_positions = []

# Définition des formes des pièces
piece_shapes = {
    'pion_blanc': (30, 30),
    'pion_noir': (30, 30),
    'tour_blanc': (40, 40),
    'tour_noir': (40, 40),
    'cavalier_blanc': (35, 35),
    'cavalier_noir': (35, 35),
    'fou_blanc': (35, 35),
    'fou_noir': (35, 35),
    'reine_blanc': (40, 40),
    'reine_noir': (40, 40),
    'roi_blanc': (40, 40),
    'roi_noir': (40, 40)
}


# Parcours de l'image pour détecter les pièces
for y in range(image.height):
    for x in range(image.width):
        pixel_value = image_grayscale.getpixel((x, y))
        # Détection des pièces blanches
        if pixel_value > white_threshold:
            # Vérification de la forme pour distinguer les pièces
            for piece, shape in piece_shapes.items():
                piece_width, piece_height = shape
                match = True
                for dy in range(piece_height):
                    for dx in range(piece_width):
                        if (x + dx >= image.width or y + dy >= image.height or
                            image_grayscale.getpixel((x + dx, y + dy)) < white_threshold):
                            match = False
                            break
                    if not match:
                        break
                if match:
                    piece_positions.append((piece, x + piece_width // 2, y + piece_height // 2))
        # Détection des pièces noires
        elif pixel_value < black_threshold:
            # Vérification de la forme pour distinguer les pièces
            for piece, shape in piece_shapes.items():
                piece_width, piece_height = shape
                match = True
                for dy in range(piece_height):
                    for dx in range(piece_width):
                        if (x + dx >= image.width or y + dy >= image.height or
                            image_grayscale.getpixel((x + dx, y + dy)) > black_threshold):
                            match = False
                            break
                    if not match:
                        break
                if match:
                    piece_positions.append((piece, x + piece_width // 2, y + piece_height // 2))

# Générer le FEN à partir des positions des pièces (exemple simplifié)
def generate_fen(piece_positions):
    fen = ''
    for y in range(8):
        empty_count = 0
        for x in range(8):
            piece_found = False
            for piece, piece_x, piece_y in piece_positions:
                if piece_x // (image.width // 8) == x and piece_y // (image.height // 8) == y:
                    fen += piece[0].upper() if piece[1] == 'b' else piece[0].lower()
                    piece_found = True
            if not piece_found:
                empty_count += 1
            if x == 7 or piece_found:
                if empty_count > 0:
                    fen += str(empty_count)
                    empty_count = 0
        if y < 7:
            fen += '/'
    return fen
print("Hello World 2!")

# Générer le FEN
fen = generate_fen(piece_positions)

# Afficher le FEN généré
print("FEN du plateau d'échecs : ", fen)
