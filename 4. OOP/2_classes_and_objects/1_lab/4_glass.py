class Glass:
    capacity = 250          # 250ml

    def __init__(self):
        self.content = 0

    def fill(self, quantity):
        if self.content + quantity > Glass.capacity:
            return f"Cannot add {quantity} ml"

        self.content += quantity
        return f"Glass filled with {quantity} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{(Glass.capacity - self.content)} ml left"
