class GameConfig(object):
    '''
    Contains basic information about how the game should run.
    Includes things like SCREEN_SIZE, FRAMES_PER_SECOND, etc.
    '''
    SCREEN_SIZE = 800, 400
    CAPTION = 'Hello World'
    CLEAN_SCREEN = (255, 255, 255)
    FRAMES_PER_SECOND = 60

    # User Defined Controls
    UP = 273
    DOWN = 274
    RIGHT = 275
    LEFT = 276
