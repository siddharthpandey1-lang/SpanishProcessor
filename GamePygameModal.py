import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spanish Learning Game")
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
GREEN = (34, 139, 34)
RED = (220, 20, 60)
PURPLE = (138, 43, 226)

# Fonts
title_font = pygame.font.SysFont("comicsansms", 72)
word_font = pygame.font.SysFont("arial", 48)
desc_font = pygame.font.SysFont("verdana", 36)

# Vocabulary list
vocab = [
    ("el hombre", "A man in Spanish", BLUE),
    ("el niño", "A boy in Spanish", GREEN),
    ("la niña", "A girl in Spanish", RED),
    ("la mujer", "A woman in Spanish", PURPLE),
    ("uno", "One in Spanish", BLUE),
    ("dos", "Two in Spanish", GREEN),
    ("tres", "Three in Spanish", RED),
    ("cuatro", "Four in Spanish", PURPLE),
    ("cinco", "Five in Spanish", BLUE),
    ("seis", "Six in Spanish", GREEN),
    ("siete", "Seven in Spanish", RED),
    ("ocho", "Eight in Spanish", PURPLE),
    ("nueve", "Nine in Spanish", BLUE),
    ("diez", "Ten in Spanish", GREEN),
]

def fade_in_text(text, font, color, y_pos):
    for alpha in range(0, 256, 5):
        screen.fill(WHITE)
        rendered = font.render(text, True, color)
        rendered.set_alpha(alpha)
        screen.blit(rendered, (WIDTH // 2 - rendered.get_width() // 2, y_pos))
        pygame.display.update()
        clock.tick(FPS)

def show_message(text, font, color, y_pos, delay=1.5):
    rendered = font.render(text, True, color)
    screen.fill(WHITE)
    screen.blit(rendered, (WIDTH // 2 - rendered.get_width() // 2, y_pos))
    pygame.display.update()
    time.sleep(delay)

# Main loop
def main():
    screen.fill(WHITE)
    fade_in_text("Welcome to the Spanish Learning Game!", title_font, BLACK, 100)
    show_message("Let's learn some basic Spanish vocabulary!", desc_font, BLUE, 200)

    for word, meaning, color in vocab:
        fade_in_text(word, word_font, color, 400)
        show_message(meaning, desc_font, BLACK, 500)

    fade_in_text("Great job!", title_font, GREEN, 600)
    show_message("Keep practicing and have fun!", desc_font, BLUE, 700)

    # Wait before exit
    time.sleep(3)
    pygame.quit()
    sys.exit()

main()