#coding:utf-8


class DrawingAPI1(object):
    def draw_circle(self, x, y, radius):
        print('API1.cricle at {}:{} radius {}'.format(x, y, radius))


class DrawingAPI2(object):
    def draw_circle(self, x, y ,radius):
        print('API2.cricle at {}:{} radius {}'.format(x, y, radius))


class CircleShape(object):
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api
    
    # low-level i.e. Implementation specific
    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y ,self._radius)
    
    # high-level i.e. Abstraction specific
    def scale(self, pct):
        self._radius *= pct


def main():
    shapes = (
        CircleShape(1, 2, 3, DrawingAPI1()),
        CircleShape(5, 7, 11, DrawingAPI2())
    )
    
    for shape in shapes:
        shape.scale(2.5)
        shape.draw()


if __name__ == '__main__':
    main()




