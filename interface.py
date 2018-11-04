"""
    This is the .py file for the interface
    framework. (PyGame)
"""

import engine, pygame, json

with open('config/cfg_interface.json') as ofile:
    cfg_interface = json.load(ofile)

display_width = cfg_interface["DISPLAY_WIDTH"]
display_height = cfg_interface["DISPLAY_HEIGHT"]

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Unscramble")

# assign colors for shorter code lines:
clr_dkb = cfg_interface["COLOR_DARK-BLUE"]
clr_red = cfg_interface["COLOR_RED"]
clr_grn = cfg_interface["COLOR_GREEN"]
clr_av1 = cfg_interface["COLOR_AVAILABLE"]
clr_av2 = cfg_interface["COLOR_UNAVAILABLE"]

fnt_hnd = cfg_interface["FONT_HANDWRITING"]
fnt_tpw = cfg_interface["FONT_TYPEWRITER"]

x_cnt = display_width//2
y_cnt = display_height//2

clock = pygame.time.Clock()

music_playing = False

def fade(background_url, fade_type = "out", time_delay=3):
    """
    This function fades a background in or out, given its url and fade type.

    :param background_url: path for background image.
    :type background_url: string
    
    :param fade_type: [``"out"`` /``"in"``] for fade out or fade in, respectively.
    :type fade_type: string
    
    :param time_delay: delay in seconds before fading.
    :type time_delay: int
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
    
    :param background_url: path for background image.
    :type background_url: string
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
    """This function instantiates the splash screen."""

    fade('assets/img_splash.png', 'in', 1)
    fade('assets/img_splash.png', 'out', 3)
    fade('assets/img_main-menu.png', 'in', 0)


def text_blit(text, font_size, font_url, rgb, center=True, x=None, y=None):
    """
    This renders given text onto the game screen.
    
    :param text: literal string of text to be rendered.
    :type text: string
    
    :param font_size: font size (in pixels) of text.
    :type font_size: int
    
    :param font_url: path for the font file `(.ttf/.otf)` of the font.
    :type font_url: string
    
    :param rgb: [``red``, ``green``, ``blue``] int tuple/list for the RGB color.
    :type rgb: list/tuple
    
    :param center: if coordinates are aligned according to text's geometric center.
    :type center: bool
    
    :param x: coordinates of render location on the x-axis.
    :type x: int
    
    :param y: coordinates of render location on the y-axis.
    :type y: int

    If `x` and `y` are both left `None`, the text is automatically rendered on the center of the screen.

    If `center` is on `False`, the text is rendered with `x` and `y` as its top-right orientation.
    """
    def text_objects(text, font, r, g, b):
        textSurface = font.render(text, True, (r, g, b))
        return textSurface, textSurface.get_rect()

    def word_display(text, font_size, font_url, r, g, b, x, y, center):
        text_font = pygame.font.Font(font_url, font_size)
        text_surface, text_rect = text_objects(text, text_font, r, g, b)
        if center:
            if x != None and y != None:
                text_rect.center = (x, y)
            else:
                text_rect.center = ((x_cnt), (y_cnt))
            screen.blit(text_surface, text_rect)
        else:
            screen.blit(text_surface, (x, y))

    r, g, b = rgb

    word_display(text, font_size, font_url, r, g, b, x, y, center)


def add_button(x1, x2, y1, y2, select_state, button_action, audio_url = None, pointer_url = None):
    """
    This function instantiates a button rectangle. It returns a Boolean whether or not the mouse
    is hovering over it. The Boolean value is to be passed again into ``select_state`` in order to
    avoid recursive effects (such as the hover audio playing again).

    :returns: (`bool`) ``select_state``.
    
    :param x1: coordinates on the x-axis where the rectangle starts.
    :type x1: int
    
    :param x2: coordinates on the x-axis where the rectangle ends.
    :type x2: int
    
    :param y1: coordinates on the y-axis where the rectangle starts.
    :type y1: int
    
    :param y2: coordinates on the y-axis where the rectangle ends.
    :type y2: int
    
    :param select_state: if the button is currently hovered on by the mouse.
    :type select_state: bool
    
    :param button_action: the function to be performed on button click.
    :type button_action: function
    
    :param audio_url: path for the audio file to be played on hover.
    :type audio_url: string
    
    :param pointer_url: path for the pointer image to be rendered on hover.
    :type pointer_url: string

    By default, `audio_url` and `pointer_url` are assigned `None`, and will not play any audio
    and show any pointers on button hover.
    """

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if audio_url != None:
        aud_select = pygame.mixer.Sound(audio_url)

    if x1 <= mouse[0] <= x2 and y1 <= mouse[1] <= y2:
        if pointer_url != None:
            img_pointer = pygame.image.load('assets/img_pointer.png')
            screen.blit(img_pointer, (x2, y1))
        if not select_state and audio_url != None:
            aud_select.play()

        if click[0] == 1:
            if audio_url != None:
                aud_select.play()
            button_action()
        return True
    else:
        return False


def back_button(x1, x2, y1, y2, select_state, button_action, audio_url = None):
    """
    This function instantiates a back button rectangle.
    
    Functionality is the same with ``interface.add_button``.
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
    """
    This function instantiates a timer on the screen. By default, the timer runs for **100 seconds**.

    :returns: (`bool`) `True` if timer has ended and `False` if otherwise.

    :param count: current count in seconds.
    :type count: float
    """

    img_loading_bar = pygame.image.load('assets/img_loading-bar.png')
    img_loading_bar_bg = pygame.image.load('assets/img_loading-bar-bg.png')

    if count >= 100:
        return True
    else:
        screen.blit(img_loading_bar, (135 - ((count/100) * 580), 375))
        screen.blit(img_loading_bar_bg, (0, 375))
        return False


def mistakes(count):
    """
    This function instantiates a mistakes counter on the screen. By default, this renders for a maximum of three
    mistakes per game. The boolean returned by this function indicates if the user has already made three mistakes.

    :returns: (`bool`) `True` if mistakes reach three, `False` if otherwise.

    :param count: number of mistakes by the player
    :type count: int
    """
    try:
        img_cross_true = pygame.image.load('assets/img_cross_true.png')
        img_cross_false = pygame.image.load('assets/img_cross_false.png')
        coords = [(710, 20), (710, 120), (710, 220)]
        for x in range(count, 3):
            screen.blit(img_cross_false, coords[x])
        for x in range(count):
            screen.blit(img_cross_true, coords[x])
    except IndexError:
        return True
    
    if count >= 3:
        return True
    else:
        return False


def anagram_loading_screen():
    """
    This function instantiates the anagram game loading screen.

    This is called by `interface.anagram_screen` and **should not be called directly**.
    """

    img_loading_bg = pygame.image.load('assets/img_loading-anagram.png')
    aud_page_flip = pygame.mixer.Sound('assets/aud_page-flip.wav')

    display_word, answer_list = engine.anagram_init()
    while len(answer_list) < 3:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
        aud_page_flip.play(0, 0, 100)

        display_word, answer_list = engine.anagram_init()

        screen.blit(img_loading_bg, (0, 0))
        text_blit(display_word, 36, fnt_hnd, clr_dkb, True)

        pygame.display.update()
        clock.tick(60)

    aud_ding = pygame.mixer.Sound('assets/aud_ding.wav')
    aud_ding.play()

    pygame.time.delay(500)

    swipe('assets/img_game-anagram.png')

    return display_word, answer_list


def anagram_screen():
    """
    This function instantiates the anagram game instance.

    This function is called directly from `interface.start_menu` through a button click.
    """
    
    display_word, answer_list = anagram_loading_screen()
    original_list = answer_list.copy()
    wrong_count = 0

    def process_anagram(text):
        if text in answer_list:
            answer_list.remove(text)
            aud_ding.play()
            for i in range(3):
                text_blit(text, 80, fnt_hnd, clr_grn, True, x_cnt, y_cnt+35)
                pygame.time.delay(100)
                pygame.display.update()
                text_blit(text, 80, fnt_hnd, clr_dkb, True, x_cnt, y_cnt+35)
                pygame.time.delay(100)
                pygame.display.update()
                clock.tick(60)

            engine.anagram_correct()
            return True

        else:
            aud_fail.play()
            for i in range(3):
                text_blit(text, 80, fnt_hnd, clr_red, True, x_cnt, y_cnt+35)
                pygame.time.delay(100)
                pygame.display.update()
                text_blit(text, 80, fnt_hnd, clr_dkb, True, x_cnt, y_cnt+35)
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
                    else:
                        wrong_count += 1
                        mistakes(wrong_count)
                elif pygame.K_a <= event.key <= pygame.K_z:
                    character = chr(event.key)
                    input_string += str(character).lower()
                    aud_keystroke.play()

        screen.blit(img_anagram_background, (0, 0))
        text_blit(display_word, 80, fnt_hnd, clr_dkb, False, 120, 90)
        text_blit(input_string, 80, fnt_hnd, clr_dkb, True, x_cnt, y_cnt+35)
        
        if timer(count) or len(answer_list) == 0:
            running_anagram_game = False
            aud_ding.play()

        if mistakes(wrong_count):
            running_anagram_game = False
            aud_ding.play()

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

    This function is called directly from `interface.start_menu` through a button click.
    """
    
    swipe('assets/img_game-combine.png')

    letter_string, max_points = engine.combine_init()
    answer_list = []
    current_points, wrong_count = 0, 0
    combine_list = [[x, True] for x in letter_string]
    available_letters = [x[0] for x in combine_list if x[1] == True]

    def combine_display(letter_list):
        combine_coordinates = [(i, 280) for i in range(190, 620, 60)] + [(i, 340) for i in range(190, 620, 60)]

        i = 0
        for entry in letter_list:
            _x, _y = combine_coordinates[i][0], combine_coordinates[i][1]
            if entry[1] == True:
                pass
                text_blit(entry[0].upper(), 50, fnt_tpw, clr_av1, True, _x, _y)   
            else:
                text_blit(entry[0].upper(), 50, fnt_tpw, clr_av2, True, _x, _y)
            i += 1

    def process_combine(text):
        if text not in answer_list and engine.combine_correct(text, letter_string):
            answer_list.append(text)
            aud_ding.play()
            for i in range(3):
                text_blit(text, 80, fnt_hnd, clr_grn, True, x_cnt, y_cnt-85)
                pygame.time.delay(100)
                pygame.display.update()
                text_blit(text, 80, fnt_hnd, clr_dkb, True, x_cnt, y_cnt-85)
                pygame.time.delay(100)
                pygame.display.update()
                clock.tick(60)

            current_points = engine.combine_points()

            return True

        else:
            aud_fail.play()
            for i in range(3):
                text_blit(text, 80, fnt_hnd, clr_red, True, x_cnt, y_cnt-85)
                pygame.time.delay(100)
                pygame.display.update()
                text_blit(text, 80, fnt_hnd, clr_dkb, True, x_cnt, y_cnt-85)
                pygame.time.delay(100)
                pygame.display.update()
                clock.tick(60)
            return False

    img_combine_background = pygame.image.load('assets/img_game-combine.png')
    aud_keystroke = pygame.mixer.Sound('assets/aud_keystroke.wav')
    aud_key_error = pygame.mixer.Sound('assets/aud_key-error.wav')
    aud_ding = pygame.mixer.Sound('assets/aud_ding.wav')
    aud_fail = pygame.mixer.Sound('assets/aud_fail.wav')

    running_combine_game, input_string, count = True, '', 0.0
    start_tick = pygame.time.get_ticks()

    while running_combine_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_combine_game = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(input_string) > 0:
                        index = combine_list.index([input_string[-1], False])
                        combine_list[index][1] = True
                        input_string = input_string[:-1]
                        aud_keystroke.play()
                elif event.key == pygame.K_RETURN:
                    if process_combine(input_string):
                        input_string = ''
                        combine_list = [[x[0], True] for x in combine_list]
                    else:
                        wrong_count += 1
                        mistakes(wrong_count)
                elif pygame.K_a <= event.key <= pygame.K_z:
                    character = chr(event.key)
                    if character in available_letters:
                        input_string += str(character).lower()
                        aud_keystroke.play()
                        index = combine_list.index([character, True])
                        combine_list[index][1] = False
                    else:
                        aud_key_error.play()

        screen.blit(img_combine_background, (0, 0))

        available_letters = [x[0] for x in combine_list if x[1] == True]
        combine_display(combine_list)
        text_blit(input_string, 80, fnt_hnd, clr_dkb, True, x_cnt, y_cnt-85)
                
        if timer(count) or current_points == max_points:
            running_combine_game = False
            aud_ding.play()

        if mistakes(wrong_count):
            running_combine_game = False
            aud_ding.play()

        count = (pygame.time.get_ticks() - start_tick)/1000

        pygame.display.update()
        clock.tick(60)

    # change this to the score end screen
    pygame.time.delay(1000)
    swipe('assets/img_score-bg.png')
    combine_score_screen(letter_string, max_points)
    

def anagram_score_screen(answer_list):
    """
    This function instantiates the anagram score screen instance.

    This is called by `interface.anagram_screen` and **should not be called directly**.
    
    :param answer_list: a list of words the user has correctly answered.
    :type answer_list: list
    """

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
        s1, s2, = "{} word{} solved".format(words_solved, plurality), "The words were:"
        text_blit(s1, 60, fnt_hnd, clr_dkb, True, x_cnt, 175)
        text_blit(s2, 40, fnt_hnd, clr_dkb, True, x_cnt, 235)
        text_blit(answers, 50, fnt_hnd, clr_dkb, True, x_cnt, 310)

        but_1 = back_button(355, 455, 345, 405, but_1, start_transition, 'assets/aud_select.wav')

        pygame.display.update()
        clock.tick(60)


def combine_score_screen(letter_string, max_points):
    """
    This function instantiates the combine score screen instance.

    This is called by `interface.combine_screen` and **should not be called directly**.

    :param letter_string: the randomly generated string used in the game mode.
    :type letter_string: string
    
    :param max_points: the maximum number of points achievable with the string.
    :type max_points: int
    """

    img_background = pygame.image.load('assets/img_score-bg.png')
    
    running_score_screen = True
    points = engine.combine_end()
    plurality = 's' if points != 1 else ''

    but_1 = False

    while running_score_screen:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

        screen.blit(img_background, (0, 0))
        s1, s3 = "{} total point{}".format(points, plurality),  str(max_points)
        s2 = "The maximum achievable points for {} was:".format(letter_string)
        text_blit(s1, 60, fnt_hnd, clr_dkb, True, x_cnt, 175)
        text_blit(s2, 40, fnt_hnd, clr_dkb, True, x_cnt, 235)
        text_blit(s3, 50, fnt_hnd, clr_dkb, True, x_cnt, 310)

        but_1 = back_button(355, 455, 345, 405, but_1, start_transition, 'assets/aud_select.wav')

        pygame.display.update()
        clock.tick(60)


def start_transition():
    """
    This function acts as a bridging instance for the menu.

    This is called when a game ends and **should not be called directly**.
    """
    swipe('assets/img_main-menu.png')
    start_menu()


def start_menu():
    """
    This function instantiates the game menu.

    This is called when a game ends or when the splash screen ends 
    and **should not be called directly**.
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
        but_4 = add_button(120, 190, 315, 350, but_4, pygame.quit, aud_select, img_select)

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

        pygame.display.flip()

        clock.tick(60)
                

if __name__ == '__main__':
    main()