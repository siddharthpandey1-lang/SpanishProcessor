import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spanish Vocabulary Adventure")
clock = pygame.time.Clock()
FPS = 60

# Colors
BG_COLOR = (25, 25, 112)  # Midnight blue
SPANISH_COLOR = (255, 215, 0)  # Gold
ENGLISH_COLOR = (173, 216, 230)  # Light blue

# Fonts
font_spanish = pygame.font.SysFont("comicsansms", 80)
font_english = pygame.font.SysFont("arial", 50)
font_intro = pygame.font.SysFont("verdana", 60)

# Vocabulary pairs
vocab = [
    ("Glad to see you back!", "Let's learn some more Spanish words together!"),
    ("mucho gusto", "Nice to meet you in Spanish"),
    ("buenos dias", "Good morning in Spanish"),
    ("buenas tardes", "Good afternoon in Spanish"),
    ("buenas noches", "Good night in Spanish"),
    ("por favor", "Please in Spanish"),
    ("gracias", "Thank you in Spanish"),
    ("de nada", "You're welcome in Spanish"),
    ("lo siento", "I'm sorry in Spanish"),
    ("salud", "Bless you in Spanish"),
    ("adios", "Goodbye in Spanish"),
    ("hasta luego", "See you later in Spanish"),
    ("hasta manana", "See you tomorrow in Spanish"),
    ("que tengas un buen dia", "Have a nice day in Spanish"),
    ("aprender", "To learn in Spanish"),
    ("jugar", "To play in Spanish"),
    ("leer", "To read in Spanish"),
    ("escribir", "To write in Spanish"),
    ("escuchar", "To listen in Spanish"),
    ("hablar", "To speak in Spanish"),
    ("comprender", "To understand in Spanish"),
    ("practicar", "To practice in Spanish"),
    ("estudiar", "To study in Spanish")
]

# Animation variables
index = 0
alpha = 0
fade_in = True
timer = 0
display_time = 120  # ~2 seconds

# Main loop
while True:
    screen.fill(BG_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fade logic
    if fade_in:
        alpha += 5
        if alpha >= 255:
            alpha = 255
            fade_in = False
    else:
        timer += 1
        if timer > display_time:
            alpha -= 5
            if alpha <= 0:
                alpha = 0
                fade_in = True
                timer = 0
                index = (index + 1) % len(vocab)

    # Render text
    spanish_text = font_spanish.render(vocab[index][0], True, SPANISH_COLOR)
    english_text = font_english.render(vocab[index][1], True, ENGLISH_COLOR)

    spanish_text.set_alpha(alpha)
    english_text.set_alpha(alpha)

    # Positioning
    spanish_rect = spanish_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
    english_rect = english_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))

    # Draw
    screen.blit(spanish_text, spanish_rect)
    screen.blit(english_text, english_rect)

    pygame.display.flip()
    clock.tick(FPS)