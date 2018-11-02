"""
    This is the main .py file for the interface
    framework. (PyGame)

    developed by Carlos Panganiban, 2018
    github.com/lickorice | @cgpanganiban
"""

import engine, pygame, json

with open('config/cfg_interface.json') as ofile:
    cfg_interface = json.load(ofile)

display_width = cfg_interface["DISPLAY_WIDTH"]
display_height = cfg_interface["DISPLAY_HEIGHT"]

screen = pygame.display.set_mode((display_width, display_height))
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
                pygame.quit()
        
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


def swipe(background_url):
    """
    This function sweeps a background in from the bottom, given its url.
    """

    img_background = pygame.image.load(background_url)
    aud_sound_effect = pygame.mixer.Sound('assets/aud_rustle-1.wav')

    aud_sound_effect.play()

    done, y = False, display_height

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
        
        screen.blit(img_background, (0, y))

        y -= 5

        if y < 0:
            screen.blit(img_background, (0, 0))
            done = True

        pygame.display.flip()
        clock.tick(60)


def splash_screen():
    """
    This function instantiates the intro splash screen.
    """

    fade('assets/img_splash.png', 'in', 1)
    fade('assets/img_splash.png', 'out', 3)
    fade('assets/img_main-menu.png', 'in', 0)


def add_button(x1, x2, y1, y2, select_state, button_action, audio_url = None, pointer_url = None):
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


def back_button(x1, x2, y1, y2, select_state, button_action, audio_url = None):
    """
    This function instantiates a button rectangle
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    aud_select = pygame.mixer.Sound(audio_url)

    if x1 <= mouse[0] <= x2 and y1 <= mouse[1] <= y2:
        img_pointer = pygame.image.load('assets/img_pointer-back.png')
        screen.blit(img_pointer, (325, 365))

        if not select_state:
            aud_select.play()

        if click[0] == 1:
            button_action()
        return True
    else:
        return False


def timer(count):

    img_loading_bar = pygame.image.load('assets/img_loading-bar.png')
    img_loading_bar_bg = pygame.image.load('assets/img_loading-bar-bg.png')

    if count >= 100:
        return True
    else:
        screen.blit(img_loading_bar, (135 - ((count/100) * 580), 375))
        screen.blit(img_loading_bar_bg, (0, 375))
        return False


def anagram_loading_screen():
    """
    This function instantiates the anagram game loading screen.
    """

    img_loading_bg = pygame.image.load('assets/img_loading-anagram.png')
    aud_page_flip = pygame.mixer.Sound('assets/aud_page-flip.wav')

    def text_objects(text, font):
        textSurface = font.render(text, True, (14, 12, 74))
        return textSurface, textSurface.get_rect()

    def word_display(text):
        text_font = pygame.font.Font('assets/fnt_handwriting.otf', 36)
        text_surface, text_rect = text_objects(text, text_font)
        text_rect.center = ((display_width//2), (display_height//2))
        screen.blit(text_surface, text_rect)

    display_word, answer_list = engine.anagram_init()
    while len(answer_list) < 3:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
        aud_page_flip.play(0, 0, 100)

        display_word, answer_list = engine.anagram_init()

        screen.blit(img_loading_bg, (0, 0))
        word_display(display_word)

        print(display_word, answer_list)

        pygame.display.update()
        clock.tick(60)

    # A word has been found!
    aud_ding = pygame.mixer.Sound('assets/aud_ding.wav')
    aud_ding.play()

    pygame.time.delay(500)

    swipe('assets/img_game-anagram.png')

    return display_word, answer_list


def anagram_screen():
    """
    This function instantiates the anagram game instance.
    """
    
    display_word, answer_list = anagram_loading_screen()
    original_list = answer_list.copy()

    def text_objects(text, font):
        textSurface = font.render(text, True, (14, 12, 74))
        return textSurface, textSurface.get_rect()

    def text_correct(text, font):
        textSurface = font.render(text, True, (80, 213, 66))
        return textSurface, textSurface.get_rect()

    def text_wrong(text, font):
        textSurface = font.render(text, True, (216, 38, 38))
        return textSurface, textSurface.get_rect()

    def word_display(text):
        text_font = pygame.font.Font('assets/fnt_handwriting.otf', 80)
        text_surface, text_rect = text_objects(text, text_font)
        text_rect.center = ((display_width//2), (display_height//2+35))
        screen.blit(text_surface, text_rect)

    def word_correct(text):
        text_font = pygame.font.Font('assets/fnt_handwriting.otf', 80)
        text_surface, text_rect = text_correct(text, text_font)
        text_rect.center = ((display_width//2), (display_height//2+35))
        screen.blit(text_surface, text_rect)

    def word_wrong(text):
        text_font = pygame.font.Font('assets/fnt_handwriting.otf', 80)
        text_surface, text_rect = text_wrong(text, text_font)
        text_rect.center = ((display_width//2), (display_height//2+35))
        screen.blit(text_surface, text_rect)

    def anagram_display(text):
        text_font = pygame.font.Font('assets/fnt_handwriting.otf', 80)
        text_surface, text_rect = text_objects(text, text_font)
        screen.blit(text_surface, (120, 90))

    def process_anagram(text):
        if text in answer_list:
            answer_list.remove(text)
            aud_ding.play()
            for i in range(3):
                word_correct(text)
                pygame.time.delay(100)
                pygame.display.update()
                word_display(text)
                pygame.time.delay(100)
                pygame.display.update()
                clock.tick(60)

            engine.anagram_correct()
            return True

            # put correct methods here

        else:
            aud_fail.play()
            for i in range(3):
                word_wrong(text)
                pygame.time.delay(100)
                pygame.display.update()
                word_display(text)
                pygame.time.delay(100)
                pygame.display.update()
                clock.tick(60)

            return False          

    img_anagram_background = pygame.image.load('assets/img_game-anagram.png')
    aud_keystroke = pygame.mixer.Sound('assets/aud_keystroke.wav')
    aud_ding = pygame.mixer.Sound('assets/aud_ding.wav')
    aud_fail = pygame.mixer.Sound('assets/aud_fail.wav')

    running_anagram_game, input_string, count = True, '', 0.0
    start_tick = pygame.time.get_ticks()

    while running_anagram_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_anagram_game = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_string = input_string[:-1]
                    aud_keystroke.play()
                elif event.key == pygame.K_RETURN:
                    if process_anagram(input_string):
                        input_string = ''
                elif pygame.K_a <= event.key <= pygame.K_z:
                    character = chr(event.key)
                    input_string += str(character).lower()
                    aud_keystroke.play()

        screen.blit(img_anagram_background, (0, 0))
        anagram_display(display_word)
        word_display(input_string)

        if timer(count) or len(answer_list) == 0:
            running_anagram_game = False
            aud_ding.play()
            print("Time's up!")

        count = (pygame.time.get_ticks() - start_tick)/1000

        pygame.display.update()
        clock.tick(60)

    # change this to the score end screen
    pygame.time.delay(1000)
    swipe('assets/img_score-bg.png')
    anagram_score_screen(original_list)


def combine_screen():
    """
    This function instantiates the combine game instance.
    """
    pass


def anagram_score_screen(answer_list):
    """
    This function instantiates the anagram score screen instance.
    """

    def text_objects(text, font):
        textSurface = font.render(text, True, (14, 12, 74))
        return textSurface, textSurface.get_rect()

    def word_display(text, height, size):
        text_font = pygame.font.Font('assets/fnt_handwriting.otf', size)
        text_surface, text_rect = text_objects(text, text_font)
        text_rect.center = ((display_width//2), (height))
        screen.blit(text_surface, text_rect)

    img_background = pygame.image.load('assets/img_score-bg.png')
    
    running_score_screen = True
    words_solved = engine.anagram_end()
    plurality = 's' if words_solved != 1 else ''

    answers = ''
    for answer in answer_list:
        answers += '{}, '.format(answer)
    answers = answers[:-2]

    but_1 = False

    while running_score_screen:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

        screen.blit(img_background, (0, 0))
        word_display("{} word{} solved".format(words_solved, plurality), 175, 60)
        word_display("The words were:".format(words_solved, plurality), 235, 40)
        word_display(answers, 310, 60)

        but_1 = add_button(355, 455, 345, 405, but_1, start_transition, 'assets/aud_select.wav')

        pygame.display.update()
        clock.tick(60)


def combine_score_screen():
    """
    This function instantiates the combine score screen instance.
    """
    pass


def start_transition():
    """
    This function acts as a bridging instance for the menu.
    """
    swipe('assets/img_main-menu.png')
    start_menu()


def start_menu():
    """
    This function instantiates the game menu.
    """

    global music_playing
    if not music_playing:
        pygame.mixer.music.load('assets/aud_bgm.mp3')
        pygame.mixer.music.play(-1)
        music_playing = True
    
    but_1, but_2, but_4 = False, False, False

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
        but_1 = add_button(120, 310, 145, 180, but_1, anagram_screen, aud_select, img_select)
        but_2 = add_button(120, 310, 200, 235, but_2, combine_screen, aud_select, img_select)
        but_4 = add_button(120, 310, 315, 350, but_4, pygame.quit, aud_select, img_select)

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
    engine.init_dictionary('assets/dictionary.txt')
    start_game()
                

if __name__ == '__main__':
    main()