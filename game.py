import pygame
from gameconfig import GameConfig
from layer import Layer
from control import menu_events


class State(object):
    '''
    Default State class. The StateHandler depends on each state having a run
    method. If a new state does not redefine the run method, then the default
    run method will return none and StateHandler.run_game will exit. Also,
    contains state_vars for communicating across states.
    '''
    def __init__(self, state_vars):
        self.state_vars = state_vars

    def run(self):
        return None


class StateHandler(object):
    '''
    Manages the game state, hands off arguments between game states, and
    initializes pygame.
    '''
    def __init__(self):
        self.screen = None
        self.current_state = None
        self.state_vars = {}

    def setup(self):
        pygame.init()
        pygame.display.set_caption(GameConfig.CAPTION)
        self.current_state = GameMenu(self.state_vars)

    def run_game(self):
        while self.current_state:
            current_state_object = self.current_state.run()
            if not hasattr(current_state_object, '__call__'):
                self.current_state = current_state_object
            else:
                self.current_state = current_state_object(self.screen, self.state_vars)

    @staticmethod
    def teardown():
        pygame.quit()


class GameMenu(State):
    def __init__(self, *args, **kwargs):
        State.__init__(self, *args, **kwargs)
        self.clock = None
        self.controls = None
        self.setup()

    def setup(self):
        '''
        Creates a screen to blit images to and a clock for this
        instance of play.
        '''
        # TODO: Add support for SCREEN_SIZE and other config options
        # changing while the game is running
        self.surface = Layer(GameConfig.SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.controls = {
            pygame.KEYDOWN: {
                GameConfig.UP: self.keydown_up,
                GameConfig.DOWN: self.keydown_down,
            }
        }

    def run(self):
        for _ in range(180):
            self.clock.tick(GameConfig.FRAMES_PER_SECOND)
            for event in pygame.event.get():
                if event.type in self.controls:
                    self.controls[event.type].get(event.key, lambda: None)()
            self.surface.clear()
            Layer.update()

        # Handle completed status
        return None

    def keydown_up(self):
        print 'U'

    def keydown_down(self):
        print 'D'
