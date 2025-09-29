import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spanish Vocabulary Adventure")
clock = pygame.time.Clock()
FPS = 60

# Fonts
font_title = pygame.font.SysFont("comicsansms", 72)
font_word = pygame.font.SysFont("arial", 48)
font_desc = pygame.font.SysFont("verdana", 36)
font_main = pygame.font.SysFont("comicsansms", 80)
font_sub = pygame.font.SysFont("arial", 50)
font_spanish = pygame.font.SysFont("comicsansms", 80)
font_english = pygame.font.SysFont("arial", 50)

# Level vocabularies
levels = [
    {
        "name": "Level 1: Basics",
        "bg": (255, 255, 255),
        "text_color": (0, 0, 0),
        "font_word": font_word,
        "font_desc": font_desc,
        "vocab": [
            ("el hombre", "A man in Spanish", (70, 130, 180)),
            ("el niño", "A boy in Spanish", (34, 139, 34)),
            ("la niña", "A girl in Spanish", (220, 20, 60)),
            ("la mujer", "A woman in Spanish", (138, 43, 226)),
            ("uno", "One in Spanish", (70, 130, 180)),
            ("dos", "Two in Spanish", (34, 139, 34)),
            ("tres", "Three in Spanish", (220, 20, 60)),
            ("cuatro", "Four in Spanish", (138, 43, 226)),
            ("cinco", "Five in Spanish", (70, 130, 180)),
            ("seis", "Six in Spanish", (34, 139, 34)),
            ("siete", "Seven in Spanish", (220, 20, 60)),
            ("ocho", "Eight in Spanish", (138, 43, 226)),
            ("nueve", "Nine in Spanish", (70, 130, 180)),
            ("diez", "Ten in Spanish", (34, 139, 34)),
        ]
    },
    {
        "name": "Level 2: Food",
        "bg": (30, 30, 30),
        "text_color": (255, 255, 255),
        "font_word": font_main,
        "font_desc": font_sub,
        "vocab": [
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
            ("el almuerzo", "Lunch in Spanish"),
            ("la cena", "Dinner in Spanish"),
            ("el postre", "Dessert in Spanish")
        ]
    },
    {
        "name": "Level 3: Phrases & Verbs",
        "bg": (25, 25, 112),
        "text_color": (255, 215, 0),
        "font_word": font_spanish,
        "font_desc": font_english,
        "vocab": [
            ("mucho gusto", "Nice to meet you"),
            ("buenos dias", "Good morning"),
            ("buenas tardes", "Good afternoon"),
            ("buenas noches", "Good night"),
            ("por favor", "Please"),
            ("gracias", "Thank you"),
            ("de nada", "You're welcome"),
            ("lo siento", "I'm sorry"),
            ("salud", "Bless you"),
            ("adios", "Goodbye"),
            ("hasta luego", "See you later"),
            ("hasta manana", "See you tomorrow"),
            ("que tengas un buen dia", "Have a nice day"),
            ("aprender", "To learn"),
            ("jugar", "To play"),
            ("leer", "To read"),
            ("escribir", "To write"),
            ("escuchar", "To listen"),
            ("hablar", "To speak"),
            ("comprender", "To understand"),
            ("practicar", "To practice"),
            ("estudiar", "To study")
        ]
    }
]

def fade_text(word, meaning, font_word, font_desc, color_word, color_desc, bg_color):
    alpha = 0
    fade_in = True
    timer = 0
    display_time = 120

    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
                    break

        spanish_text = font_word.render(word, True, color_word)
        english_text = font_desc.render(meaning, True, color_desc)

        spanish_text.set_alpha(alpha)
        english_text.set_alpha(alpha)

        spanish_rect = spanish_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
        english_rect = english_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))

        screen.blit(spanish_text, spanish_rect)
        screen.blit(english_text, english_rect)

        pygame.display.flip()
        clock.tick(FPS)

def run_level(level):
    screen.fill(level["bg"])
    title = font_title.render(level["name"], True, level["text_color"])
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
    pygame.display.update()
    time.sleep(2)

    for item in level["vocab"]:
        if len(item) == 3:
            word, meaning, color = item
        else:
            word, meaning = item
            color = level["text_color"]
        fade_text(word, meaning, level["font_word"], level["font_desc"], color, level["text_color"], level["bg"])

def main():
    for level in levels:
        run_level(level)

    screen.fill((0, 100, 0))
    congrats = font_title.render("¡Felicidades! You've completed all levels!", True, (255, 255, 255))
    screen.blit(congrats, (WIDTH // 2 - congrats.get_width() // 2, HEIGHT // 2 - 50))
    pygame.display.update()
    time.sleep(4)
    pygame.quit()
    sys.exit()

main()