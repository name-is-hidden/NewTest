class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, a):
        self.x = a

    def set_y(self, b):
        self.y = b

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"
