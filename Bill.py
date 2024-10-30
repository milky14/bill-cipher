import pygame
import random
import time

pygame.init()

# Window size
X = 326
Y = 494

# Make window
screen = pygame.display.set_mode((X, Y))

pygame.mouse.set_visible(False)

my_font = pygame.font.SysFont('Times New Roman', 30, True)

# Bill Cipher sprites
billBody = pygame.image.load("BillBody.png").convert_alpha()
billPupil = pygame.image.load("BillPupil.png").convert_alpha()

# Bill Cipher sprites scaled down
billPupil = pygame.transform.scale(billPupil, (100, 100))

# Initial states for pupil
pupilVisible = True
pupilMode = 3
pupilX = 0
pupilY = 0

# Initialize text_surface with default empty text
text_surface = my_font.render("", False, (0, 0, 0))

def manualPupil(mouseX, mouseY):
    global pupilVisible, pupilX, pupilY
    # Eye pupil position
    pupilVisible = True
    pupilX = mouseX - 50
    pupilY = mouseY - 50

    # Clamp pupil position to the allowed boundaries
    pupilX = max(75, min(pupilX, 150))
    pupilY = max(170, min(pupilY, 200))

def randomPupil():
    global pupilVisible, pupilX, pupilY
    # Eye pupil position
    pupilVisible = True
    pupilX = random.randint(80, 140)
    pupilY = random.randint(170, 200)

def whitePupil():
    global pupilVisible
    # Hide pupil
    pupilVisible = False

# Main loop
running = True
while running:
    # Quit the program when Quit (X) button pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            for i in range(30):
                text_surface = my_font.render(("NO "*10), False, (255, 0, 0))
                screen.blit(text_surface, (0, 30*i))
            pygame.display.flip()
            time.sleep(0.5)


            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # On mouse click, change pupil mode
            pupilMode += 1

    # Get mouse position
    (mouseX, mouseY) = pygame.mouse.get_pos()

    # Determine pupil mode
    if pupilMode % 3 == 0:
        manualPupil(mouseX, mouseY)
        # Window title
        pygame.display.set_caption('Bill Cipher')
    elif pupilMode % 3 == 1:
        randomPupil()
        # Window title
        pygame.display.set_caption('B1LL C1PH3R')
    elif pupilMode % 3 == 2:
        whitePupil()
        # Window title
        pygame.display.set_caption('R3HP1C LL1B')

    # Clear the screen with a color (white)
    screen.fill((255, 255, 255))

    # Draw Bill Cipher
    if pupilVisible:
        screen.blit(billPupil, (pupilX, pupilY))
    screen.blit(billBody, (0, 0))
    screen.blit(text_surface, (0, 0))

    # Update the display
    pygame.display.flip()
