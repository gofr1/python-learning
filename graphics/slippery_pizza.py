from superwires import games
from random import randrange

path_to_images = '../../Pictures/img/'

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    '''Pan moving with mouse'''
    def update(self):
        '''Move object to mouse position'''
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()
    
    def check_collide(self):
        '''Checks if pizza and pan collide'''
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()
    
class Pizza(games.Sprite):
    '''Slippery pizza'''
    def handle_collide(self):
        '''Move pizza to a random position on a screen'''
        self.x = randrange(games.screen.width)
        self.y = randrange(games.screen.height)

def main():
    wall_image = games.load_image(path_to_images + "wall.jpg", transparent=False)
    games.screen.background = wall_image

    pizza_image = games.load_image(path_to_images + "pizza.png")
    pizza_x = randrange(games.screen.width)
    pizza_y = randrange(games.screen.height)
    the_pizza = Pizza(
        image=pizza_image, 
        x = pizza_x,
        y = pizza_y
    ) 
    games.screen.add(the_pizza)

    pan_image = games.load_image(path_to_images + "PizzaPan.png")
    the_pan = Pan(
        image = pan_image,
        x = games.mouse.x,
        y = games.mouse.y
    )
    games.screen.add(the_pan)
    games.mouse.is_visible = False # mouse pointer is invisible
    games.screen.mainloop()

# go!
main()