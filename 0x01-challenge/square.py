#!/usr/bin/python3
'''
Module: 'square'
'''


class Square():
    '''Represents class Square'''

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        '''Instantiation of Square class'''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        '''Perimeter of the square'''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        '''Print representation of the square'''
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    '''Creating a Square object'''
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
