class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return vector(self.x+other.x,self.y+other.y)


    def __sub__(self, other):
        return vector(self.x - other.x, self.y -other.y)

    def __mul__(self, other):
        return vector(self.x * other, self.y * other)

    def __eq__(self, other):
        return self.x==other.x and self.y== other.y

    def __repr__(self):
        return f"Vactor({self.x},{self.y})"



#create object of vector class
v1=vector(2,3)
v2=vector(4,5)
print(v1+v2)
print(v1-v2)
print(v1*3)



