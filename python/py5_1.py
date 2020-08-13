class Rect:
    def __init__(self, x, y, width, height):# (x,y)表示矩形的左下点的坐标，width为长，height为宽
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def intersect(self, rect: 'Rect') -> bool:
        # TODO: implement me
        Lx = abs((self.x + self.width / 2) - (rect.x + rect.width / 2))
        Ly = abs((self.y + self.height / 2) - (rect.y + rect.height / 2))
        if (Lx <= (self.width + rect.width) / 2) and (Ly <= (self.height + rect.height) / 2):
            return True
        else:
            return False