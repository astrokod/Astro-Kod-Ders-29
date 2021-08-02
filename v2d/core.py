import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __repr__(self):
        return self.__str__()

    def __neg__(self):
        return self.mult(-1)

    def __pos__(self):
        return self

    def __abs__(self):
        return Point(abs(self.x), abs(self.y))

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, other):
        return self.mult(other)

    def __rmul__(self, other):
        return self.mult(other)

    def __truediv__(self, other):
        return self.div(other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def add(self, other):
        if not isinstance(other, Point):
            raise ValueError("other must be a point")
        return Point(self.x + other.x, self.y + other.y)

    def sub(self, other):
        if not isinstance(other, Point):
            raise ValueError("other must be a point")
        return self.add(-other)

    def mult(self, scalar):
        if not isinstance(scalar, (float, int)):
            raise ValueError("scalar must be a numeric")
        return Point(scalar * self.x, scalar * self.y)

    def div(self, scalar):
        if not isinstance(scalar, (float, int)):
            raise ValueError("scalar must be a numeric")
        return self.mult(1 / scalar)

    def dist(self, other=None):
        other = other if other is not None else Point()
        if not isinstance(other, Point):
            raise ValueError("other must be a point or None")
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

    def to_polar(self):
        return self.dist(), math.degrees(math.atan2(self.y, self.x))

    def from_polar(self, r, theta):
        if not isinstance(r, (float, int)):
            raise ValueError("r must be a numierc")

        if not isinstance(theta, (float, int)):
            raise ValueError("theta must be a numierc")

        return Point(r * math.cos(math.radians(theta)), r * math.sin(math.radians(theta)))


class Vector:
    def __init__(self, point):
        self.point = point

    def __str__(self):
        return f"Vector({self.point})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __neg__(self):
        return self.mult(-1)

    def __pos__(self):
        return self

    def __abs__(self):
        return Vector(abs(self.point))

    def __mul__(self, other):
        return self.mult(other)

    def __rmul__(self, other):
        return self.mult(other)

    def __truediv__(self, other):
        return self.div(other)

    def __eq__(self, other):
        return self.point == other.point

    def mag(self):
        r, _ = self.point.to_polar()
        return r

    def dot(self, other):
        if not isinstance(other, Vector):
            raise ValueError("other must be a vector")
        return self.point.x * other.point.x + self.point.y * other.point.y

    def mult(self, scalar):
        if not isinstance(scalar, (float, int)):
            raise ValueError("scalar must be a numeric")
        return Vector(scalar * self.point)

    def div(self, scalar):
        if not isinstance(scalar, (float, int)):
            raise ValueError("scalar must be a numeric")
        return Vector(self.point / scalar)

    def add(self, other):
        if not isinstance(other, Vector):
            raise ValueError("other must be a vector")
        return Vector(self.point + other.point)

    def sub(self, other):
        if not isinstance(other, Vector):
            raise ValueError("other must be a vector")
        return Vector(self.point - other.point)

    def heading(self):
        _, theta = self.point.to_polar()
        return theta

    def angle_between(self, other):
        if not isinstance(other, Vector):
            raise ValueError("other must be a vector")
        theta = math.atan2(other.point.y * self.point.x - other.point.x * self.point.y,
                           other.point.x * self.point.x + other.point.y * self.point.y)

        return math.degrees(theta)

    def unit(self):
        return self / self.mag()

    def rotate(self, angle):
        if not isinstance(angle, (float, int)):
            raise ValueError("Angle must be numeric")
        r, theta = self.point.to_polar()
        new_theta = theta + angle
        return Vector(Point().from_polar(r, new_theta))

    def is_perpendicular(self, other):
        if not isinstance(other, Vector):
            raise ValueError("other must be a vector")
        return self.dot(other) < 0.000001

    def is_parallel(self, other):
        if not isinstance(other, Vector):
            raise ValueError("other must be a vector")
        return self.heading() % 180 == other.heading() % 180
