from v2d.core import Point, Vector

# Nokta:
p1 = Point(1, 1)
p2 = Point(2, 2)
# Vektör
v1 = Vector(p1)
v2 = Vector(p2)

# Nokta çarpım
print(v1.dot(v2))
