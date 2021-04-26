class Parent:
    def display(self):
        print("test1")
class Child(Parent):
    def display(self):
        print("childis")

object1 = Parent()
object2 = Child()

object1.display()
object2.display()