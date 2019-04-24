# graphicsandsound.py
# Made by Matt W
# April 9th, 2019

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "<Deep space>"

def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOAD ASSETS
    background_img = pygame.image.load("saturn_family1.jpg")
    player_img = pygame.image.load("player.png")
    laser_snd = pygame.mixer.Sound("laser5.ogg")

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    x_cord = 0
    y_cord = 0
    pygame.mouse.set_visible(False)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                laser_snd.play()

        # ----- LOGIC
        player_position = pygame.mouse.get_pos()
        x_coord = player_position[0]
        y_coord = player_position[1]
        if x_coord < 0:
            x_coord = 0
        if y_coord > HEIGHT - 80:
            y_coord = HEIGHT - 80
        if x_coord > WIDTH - 100:
            x_coord = WIDTH - 100

        # ----- DRAW
        # Blits or places the background at the top-left most part of the screen
        screen.blit(background_img, [0, 0])
        screen.blit(player_img, (x_coord, y_coord))

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
