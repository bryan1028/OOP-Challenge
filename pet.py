class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
    
    def _adjust_attribute(self, attr, change, min_val=0, max_val=10):
        """adjust attributes"""
        current = getattr(self, attr)
        setattr(self, attr, max(min_val, min(max_val, current + change)))
    
    def eat(self):
        self._adjust_attribute('hunger', -3)
        self._adjust_attribute('happiness', 1)
        print(f"{self.name} says YUM!")
    
    def sleep(self):
        self._adjust_attribute('energy', 5)
        print(f"{self.name} time to catch some zzzZZZ...")
    
    def play(self):
        if self.energy >= 2:
            self._adjust_attribute('energy', -2)
            self._adjust_attribute('happiness', 2)
            self._adjust_attribute('hunger', 1)
            print(f"{self.name} plays ;moving up and down, and all over the place!")
        else:
            print(f"{self.name} is .")
    
    def get_status(self):
        print(f"\n{self.name}'s Status:")
        for attr in ['hunger', 'energy', 'happiness']:
            value = getattr(self, attr)
            print(f"{attr.capitalize()}: {'▮' * value}{'▯' * (10 - value)} {value}/10")
    
    # Bonus methods
    def train(self, trick):
        if trick.lower() in [t.lower() for t in self.tricks]:
            print(f"{self.name} already knows '{trick}'!")
        else:
            self.tricks.append(trick)
            self._adjust_attribute('happiness', 1)
            print(f"{self.name} learned '{trick}'! Good job!")
    
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} hasn't learned any tricks yet.")
        else:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")
