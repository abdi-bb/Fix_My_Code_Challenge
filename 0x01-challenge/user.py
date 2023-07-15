#!/usr/bin/python3
"""
User class
"""


class User():
    """Represents class User """

    def __init__(self):
        """Instantiation of the class User """
        self.__email = None

    @property
    def email(self):
        """Gets email attribute"""
        return self.__email

    @email.setter
    def email(self, value):
        """ Sets email attribute """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
