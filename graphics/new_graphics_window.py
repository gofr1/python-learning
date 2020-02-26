from superwires import games, color

# create a graphic screen 640x480 with 50 fps
games.init(screen_width = 640, screen_height = 480, fps = 50)

# add background
wall_image = games.load_image("../../Downloads/wall.jpg", transparent=False)
games.screen.background = wall_image

# add pizza (sprite)
pizza_image = games.load_image("../../Downloads/pizza.png")
pizza = games.Sprite(
        image=pizza_image, 
        # put it in left up corner
        # x = 60, 
        # y = 60
        # or make it move
        x = games.screen.width/2,
        y = games.screen.height/2,
        dx = 1,
        dy = 1
    ) 
games.screen.add(pizza)

# add scores (text)
score = games.Text(
        value = 1753296,
        size = 60,
        # color = (0, 0, 0), # RGBA
        color = color.black, # or use color module
        x = 550,
        y = 30
    )
games.screen.add(score)

# add message
won_message = games.Message(
        value = "You win!",
        size = 100,
        color = color.red,
        x = games.screen.width/2,
        y = games.screen.height/2,
        lifetime = 250, 
        after_death = games.screen.quit
    )
games.screen.add(won_message)
# main
games.screen.mainloop()