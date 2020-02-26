from superwires import games

path_to_images = '../../Pictures/img/'

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pan(games.Sprite):
    '''Pan moving with mouse'''
    def update(self):
        '''Move object to mouse position'''
        self.x = games.mouse.x
        self.y = games.mouse.y
    
def main():
    wall_image = games.load_image(path_to_images + "wall.jpg", transparent=False)
    games.screen.background = wall_image

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

