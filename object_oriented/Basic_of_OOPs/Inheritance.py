class Polygon:
    __height=None
    __width=None
    def set_values(self,height,width):
        self.__heigth=height
        self.__width=width

    def get_height(self):
        return self.__heigth
    def get__width(self):
        return self.__width

class Rectangle(Polygon):
    def area(self):
        return self.get_height() * self.get__width()

class Triangle(Polygon):
    def area(self):
        return self.get_height() * self.get__width()/2

rect=Rectangle()
tri=Triangle()
rect.set_values(40, 50)
tri.set_values(40, 50)
print(rect.area())
print(tri.area())
