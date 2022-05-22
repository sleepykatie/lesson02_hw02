class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'starting rendering'


class Pen(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Starting rendering with a red pen'

class Pensil(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Starting rendering with a blue pensil'


class Handle(Stationary):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Starting rendering with a yellow handle'


draw_object_with_pen = Pen('Small round')
print(f'{draw_object_with_pen.title}: {draw_object_with_pen.draw()}')

draw_object_with_handle = Handle('Long line')
print(f'{draw_object_with_handle.title}: {draw_object_with_handle.draw()}')

draw_object_with_pensil = Pensil('Horizontal rectangle')
print(f'{draw_object_with_pensil.title}: {draw_object_with_pensil.draw()}')
