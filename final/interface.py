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

music_playing = False


def fade(background_url, fade_type = "out", time_delay=3):
    """
    This function fades a background in or out, given its url and type.
    """

    img_background = pygame.image.load(background_url)
    img_background = img_background.convert()
    background = pygame.Surface((screen.get_rect().width, screen.get_rect().height))
    background.fill((255, 255, 255))

    done = False
    started = True

    if fade_type == "out":
        alpha = 255
    else:
        alpha = 0

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        img_background.set_alpha(alpha)
        screen.blit(background, (0, 0))
        screen.blit(img_background, (0, 0))
        pygame.display.flip()

        if started:
            pygame.time.delay(time_delay*1000)
            started = False

        if fade_type == "out" and alpha < 0:
            done = True
        elif fade_type == "in" and alpha > 255:
            done = True

        if fade_type == "out":
            alpha -= 4
        else:
            alpha += 4

        clock.tick(60)
    

def splash_screen():
    """
    This function instantiates the intro splash screen.
    """

    fade('assets/img_splash.png', 'in', 1)
    fade('assets/img_splash.png', 'out', 3)


def button(x1, x2, y1, y2, select_state, button_action, audio_url = None, pointer_url = None):
    """
    This function instantiates a button rectangle
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    aud_select = pygame.mixer.Sound(audio_url)

    if x1 <= mouse[0] <= x2 and y1 <= mouse[1] <= y2:
        if pointer_url != None:
            img_pointer = pygame.image.load('assets/img_pointer.png')
            screen.blit(img_pointer, (x2, y1))
        if not select_state:
            aud_select.play()

        if click[0] == 1:
            button_action()
        return True
    else:
        return False


def start_menu():
    """
    This function instantiates the game menu.
    """

    global music_playing
    if not music_playing:
        pygame.mixer.music.load('assets/aud_bgm.mp3')
        pygame.mixer.music.play(-1)
    
    but_1, but_2, but_3, but_4 = False, False, False, False

    fade('assets/img_main-menu.png', 'in', 0)

    running_start_menu = True

    while running_start_menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_start_menu = False
                pygame.quit()

        mouse = pygame.mouse.get_pos()
        img_background = pygame.image.load('assets/img_main-menu.png')
        screen.blit(img_background, (0, 0))

        # This interacts with the menu items
        aud_select, img_select = 'assets/aud_select.wav', 'assets/img_pointer.png'
        but_1 = button(120, 310, 145, 180, but_1, None, aud_select, img_select)
        but_2 = button(120, 310, 200, 235, but_2, None, aud_select, img_select)
        but_3 = button(120, 310, 260, 295, but_3, None, aud_select, img_select)
        but_4 = button(120, 310, 315, 350, but_4, pygame.quit, aud_select, img_select)

        pygame.display.flip()
        
        clock.tick(60)


def start_game():
    """
    This function starts the whole game.
    """
    pygame.init()

    running = True
    game_intro = True
    game_start_menu = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        if game_intro:
            splash_screen()
            game_intro = False
            game_start_menu = True

        if game_start_menu:
            start_menu()
            game_start_menu = False


        
            # print(event)

        pygame.display.flip()

        clock.tick(60)


def main():
    start_game()
                

if __name__ == '__main__':
    main()