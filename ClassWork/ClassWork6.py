class Figure:
    '''Створити батьківський клас Figure з методами init: ініціалізується колір, get_color: повертає колір фігури,
        info: надає інформацію про фігуру та колір,  
        від якого наслідуються такі класи як Rectangle, Square, які мають інформацію про ширину, висоту фігури,
        метод square, який знаходить площу фігури.'''
    def __init__(self,color_figure):
        self.color_figure=color_figure
        return self.color_figure

    def info_figure(self):
        if self.width==self.height:
            figure='square'
        else:
            figure='rectangle'
        print("The figure is {} (width={},height={}), color of the figure - {}".format(figure,self.width,self.height,self.color_figure))

class Rectangle(Figure):
    def __init__(self,width=0,height=0,color_figure='?'):
        self.width=width
        self.height=height
        super(Rectangle,self).__init__(color_figure)

    def square(self):
        print("The square of rectangle =",self.width * self.height)

class Square(Figure):
    def __init__(self,width=0,height=0,color_figure='?'):
        self.width=width
        self.height=height
        super(Square,self).__init__(color_figure)

    def square(self):
        print("The area of square =", self.width * self.height)


r=Rectangle(6.0, 5.0, "White")
s=Square(5.0, 5.0, "Black")

r.info_figure()
r.square()

s.info_figure()
s.square()
