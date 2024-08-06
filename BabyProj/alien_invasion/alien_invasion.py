import sys

import pygame

from settings import Settings

from ship import Ship

class AlienInvasion:
    """Overall class"""
    def __init__(self):
        """Init the game"""
        pygame.init()
        self.settings = Settings()
  
    

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invason")
        
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop"""
        while True:
            # Watch fo keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    
                    sys.exit()
            

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the mos recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Instanciaton
    ai = AlienInvasion()
    ai.run_game()

