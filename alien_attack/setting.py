blue = (0, 0, 255)
grey = (128, 128, 128)
silver = (192, 192, 192)
white = (255, 255, 255)
iron = (60, 60, 60)

class Setting():
    """store all setting classes here"""
    def __init__(self):
        """initiall game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = white
        self.ship_speed_factor = 1.5
        self.caption = 'Alien Invasion'

        #bullet setting
        self.bullet_speed_factor = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = iron
        self.bullet_max = 3

        