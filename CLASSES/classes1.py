class cookie:
    def __init__(self,color):
        self.color=color
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color=color
cookie_one=cookie("green")
cookie_two=cookie("blue")
print("cookie one is",cookie_one.get_color())
print("cookie two is",cookie_two.get_color())
cookie_one.set_color("yellow")
print("cookie one is now",cookie_one.get_color())
print("cookie two is still",cookie_two.get_color())
