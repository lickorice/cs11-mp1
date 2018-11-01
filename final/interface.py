"""
    This is the main .py file for the interface
    framework. (PyGame)

    developed by Carlos Panganiban, 2018
    github.com/lickorice | @cgpanganiban
"""

import pygame, json

with open('config/cfg_interface.json') as ofile:
    cfg_interface = json.load(ofile)

display_width = cfg_interface["DISPLAY_WIDTH"]
display_height = cfg_interface["DISPLAY_HEIGHT"]

screen = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption("Test")

clock = pygame.time.Clock()

def splash_screen():
    """
    This function instantiates the intro splash screen.
    """
    img_splash_screen = pygame.image.load('assets/img_splash.png')
    img_splash_screen = img_splash_screen.convert()
    background = pygame.Surface((screen.get_rect().width, screen.get_rect().height))
    background.fill((255, 255, 255))

    done = False
    alpha = 255

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        img_splash_screen.set_alpha(alpha)
        screen.blit(background, (0, 0))
        screen.blit(img_splash_screen, (0, 0))
        pygame.display.flip()

        if alpha == 255:
            pygame.time.delay(3000)

        if alpha < 0:
            done = True

        alpha -= 4
        print(alpha)

        clock.tick(60)
        

def start_game():
    pygame.init()

    running = True
    game_intro = True

    while running:

        if game_intro:
            splash_screen()
            game_intro = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            # print(event)

        pygame.display.flip()

        clock.tick(60)


def main():
    start_game()
                

if __name__ == '__main__':
    main()