class Sphere:
    Pi = 3.1415

    def __init__(self, radius):
         self.radius = radius
         self.volume = round((4/3 * self.Pi * (radius ** 3)), 2)
