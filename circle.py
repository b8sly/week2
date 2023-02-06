class circle:
    def findCircleCircum(self, radius):
        return 2 * 3.14159 * radius
print("Enter the radius ", end = ":")

r = float(input())

ob = circle()
c = ob.findCircleCircum(r)
print("\nArea of a Circle = {:.2f}".format(c))