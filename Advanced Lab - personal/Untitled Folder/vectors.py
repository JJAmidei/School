# vectors.py

import math 

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x=x
        self.y=y
        self.z=z
        
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
    # Allows for indexing
    def __getitem__(self, item): 
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2: 
            return self.z
        else:
            raise IndexError("There are only three elements in a classical vector.")

    # Allows addition         
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )

    # Allows subtraction 
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )
    
    # Allows scalar multiplication 
    def __mul__(self, other):
        if isinstance(other, Vector):  # Vector dot product
            return (
                self.x * other.x
                + self.y * other.y
                + self.z * other.z
            )
        elif isinstance(other, (int, float)): #scalar multiplication 
            return Vector(
                self.x * other, 
                self.y * other, 
                self.z * other,
            )
        else:
            raise TypeError('Operand must be Vector, int, or float.')
        
    # Needed to allow for reversed scalar multiplication    
    def __rmul__(self, other): 
        if isinstance(other, (int, float)): 
            return Vector(
                other * self.x, 
                other * self.y,
                other * self.z,
            )
        else:
            raise TypeError('Operand must be Vector, int, or float.')
        
    def __truediv__(self, other): 
        if isinstance(other, (int, float)): 
            return Vector(
                self.x / other, 
                self.y / other, 
                self.z / other, 
            )
        else: 
            raise TypeError("Operand must be a int or float.")
        
    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude, 
            self.y / magnitude, 
            self.z / magnitude, 
        )
                
#Test Vectors
test = Vector(3,5,9)
print(test.get_magnitude())
print(test.normalize())
print(test.normalize().get_magnitude())
