class Settings():
    def set_basic_params(self):
        """Return the basic parameters"""
        self.FS:int = 20e3
        self.CHS:int = 64
        self.DURATION:int = 100e-3  # in s

        return self.FS, self.CHS, self.DURATION