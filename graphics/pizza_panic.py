from superwires import games, color
from random import randrange

path_to_images = '../../Pictures/img/'

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    '''Pan to catch pizza'''
    pan_image = games.load_image(path_to_images + "PizzaPan.png")

    def __init__(self):
        '''Initialize Pan and create text counter'''
        super(Pan, self).__init__(
            image = Pan.pan_image,
            x = games.mouse.x,
            bottom= games.screen.height
        )
        self.score = games.Text(
            value = 0,
            size = 25,
            color = color.black,
            top=5,
            right=games.screen.width - 10
        )
        games.screen.add(self.score)
     
        self.player_level = games.Text(
            value = Chef.level,
            size = 25,
            color = color.black,
            top=5,
            right=20
        )
        games.screen.add(self.player_level)

    def update(self):
        '''Move object to mouse position'''
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()

    
    def check_catch(self):
        '''Check if pizza is catched'''
        for pizza in self.overlapping_sprites:
            self.score.value +=10
            self.score.right = games.screen.width - 10
            pizza.handle_caught()
            f = self.score.value % 100

            Chef.level += 1 if f == 0 else 0
            self.player_level.value = Chef.level
    
class Pizza(games.Sprite):
    '''Falling pizza!'''
    pizza_image = games.load_image(path_to_images + "pizza.png")
    speed = 1

    def __init__(self, x, y = 90):
        '''Initialize pizza'''
        super(Pizza, self).__init__(
            image = Pizza.pizza_image,
            x = x,
            y = y,
            dy = Pizza.speed
        )
    
    def update(self):
        '''Checks if Pizza touched the bottom of screen'''
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()
    
    def handle_caught(self):
        '''Destroys catched pizza'''
        self.destroy()
    
    def end_game(self):
        '''Game over'''
        end_message = games.Message(
            value = 'Game Over',
            size = 90,
            color = color.red,
            x = games.screen.width/2,
            y = games.screen.height/2,
            lifetime= 5 * games.screen.fps,
            after_death= games.screen.quit
        )
        games.screen.add(end_message)
    
class Chef(games.Sprite):
    '''The chef that throws pizza'''
    chef_image = games.load_image(path_to_images + "TheChef.png")
    level = 1

    def __init__(self, y = 115, speed = 2, odds_change = 200):
        '''Initialize Chef'''
        super(Chef, self).__init__(
            image = Chef.chef_image,
            x = games.screen.width/2,
            y = y,
            dx = speed
        )
        self.odds_change = odds_change
        self.time_til_drop = 0
    
    def update(self):
        '''Changes speed vectors when Chef comes to the screen edge'''
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy
        self.check_drop()
    
    def check_drop(self):
        '''Decrease interval of waiting or throws pizza and restart interval'''
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
            self.time_til_drop = int(new_pizza.height * 1.3 /Pizza.speed) - self.level

def main():
    '''Gameplay'''
    wall_image = games.load_image(path_to_images + "wall.jpg", transparent=False)
    games.screen.background = wall_image

    the_chef = Chef()
    games.screen.add(the_chef)

    the_pan = Pan()
    games.screen.add(the_pan)

    games.mouse.is_visible = False
    games.screen.mainloop()

# go!
main()