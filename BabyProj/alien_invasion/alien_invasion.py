import sys

import pygame

class AlienInvasion:
    """Overall class"""
    def __init__(self):
        """Init the game"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invason")

    def run_game(self):
        """Start the main loop"""
        while True:
            # Watch fo keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    
                    sys.exit()

            # Make the mos recently drawn screen visible.
            pygame.display.flip()



if __name__ == '__main__':
    # Instanciaton
    ai = AlienInvasion()
    ai.run_game()

