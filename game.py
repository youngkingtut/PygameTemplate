import pygame
from gameconfig import GameConfig
from layer import Layer
from control import EventControl


class State(object):
    """
    Default State class. The StateHandler depends on each state having a run
    method. Contains state_vars for communicating across states.
    """
    def __init__(self, state_vars):
        self.state_vars = state_vars

    def run(self):
        return None


class StateHandler(object):
    """
    Manages the game state, hands off arguments between game states, and
    initializes pygame.
    """
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
        self.state_vars["MENU"] = self
        self.surface = None
        self.clock = None
        self.controls = None
        self.font = None
        self.exit = False
        self.buttons = None
        self.setup()

    def setup(self):
        self.surface = Layer(GameConfig.SCREEN_SIZE)
        self.surface.fill(GameConfig.MENU_COLOR)
        self.clock = pygame.time.Clock()
        self.controls = EventControl({
            pygame.QUIT: self.quit,
            pygame.MOUSEMOTION: self.mouse_movement_event
        })
        self.font = pygame.font.Font(None, GameConfig.MENU_FONT_SIZE)
        self.buttons = [
            self.font.render("Start", True, GameConfig.MENU_TEXT_COLOR),
            self.font.render("Options", True, GameConfig.MENU_TEXT_COLOR),
            self.font.render("Exit", True, GameConfig.MENU_TEXT_COLOR)
        ]

    def run(self):
        while not self.exit:
            self.clock.tick(GameConfig.FRAMES_PER_SECOND)
            self.controls.poll_event()
            self.draw_menu()
            Layer.update()

        return None

    def draw_menu(self):
        offset = 0
        for button in self.buttons:
            self.surface.blit(button, ((self.surface.get_width() - button.get_width()) / 2,
                                       (self.surface.get_height() - button.get_height()) / 2 + offset))
            offset += button.get_height() + GameConfig.MENU_TEXT_OFFSET

    def mouse_movement_event(self, event):
        for button in self.buttons:
            if button.get_rect(left=self.surface.get_width() - 100).collidepoint(event.pos):
                print button

    def quit(self, event):
        self.exit = True

