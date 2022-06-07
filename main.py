import pygame
from checkers.constants import WIDTH, HEIGHT

# set up a pygame display
# check for basic event loop (ex: mouse pressed)
# set up basic drawing (board + pieces)

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_Caption('Checkers')

def main():
    #create event loop
    run = True
    #have it run at a constant rate --> ensure it doesnt run too fast/slow
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        
        # check to see if any events have occured in time frame
        for event in pygame.event.get():
            # hit red button at top of screen
            if event.type == pygame.QUIT:
                # end loop
                run = False

                
    pygame.quit()

main()
