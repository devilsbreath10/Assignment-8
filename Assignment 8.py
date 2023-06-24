class A:
    def __init__(self, a, b, c):
        self.__a = a
        self._b = b
        self.c = c
    
    def display_contents(self):
        print("Class A block!!")
        print("a:", self.__a)
        print("b:", self._b)
        print("c:", self.c)

class B(A):
    def display_contents(self):
        try:
            print("Class B block!!!")
            print("a:", self.__a)  # Raises exception!!!
        except AttributeError:
            print("Variable 'a'(private) cannot be accessed!!")
        print("b:", self._b)
        print("c:", self.c)

#Creating Objects!!
a=A(10,9,8)
a.display_contents()

b=B(7,6,5)
b.display_contents()