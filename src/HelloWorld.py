import math


class HelloWorld:
    def demo(self):
        a = int(input("a:"))
        b = 1
        if (a >= 0):
            disc = math.sqrt(a)
        else:
            disc = "error"
        print(disc*3,end='')
        print("end")


HelloWorld().demo()
