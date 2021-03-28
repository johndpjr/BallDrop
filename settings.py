class Settings:
    """Models the app settings"""

    def __init__(self):
        # Screen settings
        self.screen_width = 500
        self.screen_height = 800
        self.FPS = 500

        # White background
        self.screen_bg_color = (255, 255, 255)

        self.GRAVITATIONAL_CONSTANT = 2300
        self.ELASTIC_CONSTANT = 0.8