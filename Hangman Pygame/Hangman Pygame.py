import pygame
import math
import random

# game initialization - 1. Set Up Display
pygame.init()

# window set
WIDTH = 1000
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
# game's title declaration
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = []
start_x = round((WIDTH - (RADIUS * 2 + GAP) *13) / 2)
start_y = 400
A = 65
for i in range(26):
    x = start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = start_y + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y, chr(A + i), True])


# fonts
LETTER_FONT = pygame.font.SysFont("Sans", 40)
WORD_FONT = pygame.font.SysFont("Sans", 60)
TITLE_FONT = pygame.font.SysFont("Sans", 70)

# load images
images = []
for i in range(6):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
words = ["WATER", "MELON", "SCIENCE", "MATHS", "COMPUTER", "STATISTICS", "PROGRAMMING", "LANGUAGE", "SCHOOL", "WORK", "WEEKEND", "PARK", "SUMMER", "CHRISTMAS"]
word = random.choice(words)
guessed = []


def draw():

    win.fill(WHITE)
    # draw title
    text = TITLE_FONT.render("HANGMAN GAME",  1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))


    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH - text.get_width() / 2, text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status
    # 2. Set Up Game Loop
    FPS = 60  # 60 Frames Per Second

    # Declares a clock object that is going to count 60 frames per second
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        draw()
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message("Congratulations!!! You Won!!!")
        if hangman_status == 6:
            display_message("Sorry... You Lost...")
            break

while True:
    main()
pygame.quit()

