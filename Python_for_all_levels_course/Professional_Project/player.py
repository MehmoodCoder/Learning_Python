class player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self._lives = 3
        self._level = 1

    def _get_lives(self):
        return self._lives
    def _set_lives(self, lives):
        if lives > 0:
            self._lives = lives
        else:
            print("Lives cannot be negative.")
            self._lives = 0

    lives = property(_get_lives, _set_lives)

    def _get_level(self):
        return self._level
    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self.score += delta * 100
            self._level = level
        else:
            print("Level cannot be negative.")
            self._level = 1

    level = property(_get_level, _set_level)

    def __str__(self):
        return f"Player: {self.name}, Score: {self.score}, Lives: {self.lives}, Level: {self.level}"



