import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spanish Vocabulary Showcase")
clock = pygame.time.Clock()
FPS = 60

# Colors
BACKGROUND = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
HIGHLIGHT = (255, 100, 100)

# Fonts
font_main = pygame.font.SysFont("comicsansms", 80)
font_sub = pygame.font.SysFont("arial", 50)

# Vocabulary list
vocab = [
    ("la manzana", "An apple in Spanish"),
    ("la leche", "Milk in Spanish"),
    ("el queso", "Cheese in Spanish"),
    ("el pan", "Bread in Spanish"),
    ("el arroz", "Rice in Spanish"),
    ("el pollo", "Chicken in Spanish"),
    ("el pescado", "Fish in Spanish"),
    ("las verduras", "Vegetables in Spanish"),
    ("las frutas", "Fruits in Spanish"),
    ("el desayuno", "Breakfast in Spanish"),
    ("come on you can do it", ""),
    ("el almuerzo", "Lunch in Spanish"),
    ("la cena", "Dinner in Spanish"),
    ("el postre", "Dessert in Spanish")
]

# Animation settings
index = 0
alpha = 0
fade_in = True
timer = 0
display_time = 120  # frames to display each word (~2 seconds)

# Main loop
while True:
    screen.fill(BACKGROUND)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle animation
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
    spanish_text = font_main.render(vocab[index][0], True, HIGHLIGHT)
    english_text = font_sub.render(vocab[index][1], True, TEXT_COLOR)

    # Apply alpha
    spanish_text.set_alpha(alpha)
    english_text.set_alpha(alpha)

    # Center text
    spanish_rect = spanish_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    english_rect = english_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    # Draw text
    screen.blit(spanish_text, spanish_rect)
    screen.blit(english_text, english_rect)

    pygame.display.flip()
    clock.tick(FPS)