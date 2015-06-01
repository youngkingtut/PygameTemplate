class GameConfig(object):
    """
    Contains basic information about how the game should run.
    Includes things like SCREEN_SIZE, FRAMES_PER_SECOND, etc.
    """
    SCREEN_SIZE = 800, 400

    MENU_FONT_SIZE = 50
    MENU_COLOR = (0, 0, 0)
    MENU_TEXT_COLOR = (125, 124, 10)
    MENU_TEXT_OFFSET = 10

    CAPTION = 'Hello World'
    CLEAN_SCREEN = (255, 255, 255)
    FRAMES_PER_SECOND = 60

    # User Defined Controls
    UP = 273
    DOWN = 274
    RIGHT = 275
    LEFT = 276
