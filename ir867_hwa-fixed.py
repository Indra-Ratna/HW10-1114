"""
CS-UY 1114
Homework A
starter code
"""

import math
import turtle

class Point:
    def __init__(self, x, y):
        # sig: Point, float, float -> NoneType
        # Construct a new Point from coordinates
        self.x = x
        self.y = y
    def move(self, horiz, vert):
        # sig: Point, float, float -> NoneType
        # Move the point by some amount in both axes
        self.x += horiz
        self.y += vert
    def draw(self):
        # sig: Point -> NoneType
        # Use turtle to draw the point as a dot on the screen
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.down()
        turtle.dot(5)
    def distance(self, other):
        # sig: Point, Point -> float
        # Calculate the distance between the point and
        # another point
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

class Rectangle:
    def __init__(self, upperleft, lowerright):
        # sig: Rectangle, Point, Point -> NoneType
        # Construct a new Rectangle from two points
        self.upperleft = upperleft
        self.lowerright = lowerright
    def diagonal_length(self):
        # sig: Rectangle -> float
        # Return the distance between the upper left point
        # and the lower right point
        d = Point.distance(self.upperleft,self.lowerright)
        return d
    def draw(self):
        # sig: Rectangle -> NoneType
        # Use turtle to draw the rectangle on the screen
        turtle.up()
        turtle.goto(self.upperleft.x,self.upperleft.y)
        turtle.down()
        turtle.goto(self.lowerright.x,self.upperleft.y)
        turtle.goto(self.lowerright.x,self.lowerright.y)
        turtle.goto(self.upperleft.x,self.lowerright.y)
        turtle.goto(self.upperleft.x,self.upperleft.y)
           
    def width(self):
        # sig: Rectangle -> float
        # Return the (positive) width of the rectangle
        width =  self.lowerright.x - self.upperleft.x
        if(width<0):
            width*=-1
        return width
    def height(self):
        # sig: Rectangle -> float
        # Return the (positive) height of the rectangle
        height =  self.upperleft.y - self.lowerright.y
        if(height<0):
            height*=-1
        return height
    def area(self):
        # sig: Rectangle -> float
        # Return the area of the rectangle
        return self.width()*self.height()

    def move(self, horiz, vert):
        # sig: Rectangle, float, float -> NoneType
        # Move the rectangle in both axes
        self.upperleft.x += horiz
        self.lowerright.x +=horiz
        self.upperleft.y +=vert
        self.lowerright.y+=horiz
    
    def overlaps(self, other):
        # sig: Rectangle, Rectangle -> bool
        # Determine if the two rectangles overlap
        if(self.lowerright.x < other.upperleft.x):
            return False
        elif(self.upperleft.x > other.lowerright.x):
            return False
        elif(self.lowerright.y > other.upperleft.y):
            return False
        elif(self.upperleft.y < other.lowerright.y):
            return False
        else:
            return True
           
    def intersection(self, other):
        # sig: Rectangle, Rectangle -> Rectangle:
        # If the two rectangles overlap, return a rectangle
        # that identifies their intersection (i.e. a rectangle
        # containing all the area contained in both of them).
        # If the rectangles don't intersect (i.e.. there is not
        # overlap), return an "empty" rectangle identified by
        # points 0,0 and 0,0.
        if not self.overlaps(other):
            return Rectangle(Point(0.0, 0.0), Point(0.0, 0.0))
        else:
            right_corner_x = min(self.lowerright.x,other.lowerright.x)
            left_corner_x= max(self.upperleft.x,other.upperleft.x)
            right_corner_y = max(self.lowerright.y,other.lowerright.y)
            left_corner_y = min(self.upperleft.y,other.upperleft.y)
            upper_left = Point(left_corner_x,left_corner_y)
            lower_right = Point(right_corner_x,right_corner_y)
            return Rectangle(upper_left,lower_right)

class Line:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def draw(self):
        turtle.up()
        turtle.goto(self.first.x,self.first.y)
        turtle.down()
        turtle.goto(self.second.x,self.second.y)
    def slope(self):
        try:
            numerator = self.first.y-self.second.y
            denominator = self.first.x-self.second.x
            slope = numerator/denominator
            return slope
        except ValueError:
            print("line has no slope")
        
def line_slope_test():
    l1 = Line(Point(1.0, 1.0),Point(3.0, 3.0))
    l2 = Line(Point(1.0, 1.0),Point(-3.0, 3.0))
    print("l1 has slope " + str(l1.slope()))
    print("l2 has slope " + str(l2.slope()))

def point_move_test():
    turtle.hideturtle()
    p1 = Point(50.0, 40.0)
    turtle.color("black")
    for _ in range(20):
        p1.draw()
        p1.move(5.0, 5.0)

def rectangle_area_test():
    r1 = Rectangle(Point(50.0, 260.0), Point(160.0, 150.0))
    print("r1 has width " + str(r1.width()))
    print("r1 has height " + str(r1.height()))
    print("r1 has area " + str(r1.area()))
    print("r1 has diagonal length: " + str(r1.diagonal_length()))

def rectangle_move_test():
    turtle.hideturtle()
    r1 = Rectangle(Point(50.0, 260.0), Point(160.0, 150.0))
    for i in range(20):
        turtle.color(["black", "green", "red"][i % 3])
        r1.draw()
        r1.move(5.0, 5.0)

def rectangle_draw_test():
    turtle.hideturtle()
    r1 = Rectangle(Point(10.0, 300.0),Point(90.0, 100.0))
    r2 = Rectangle(Point(70.0, 180.0), Point(200.0, 150.0))
    turtle.color("black")
    r1.draw()
    r2.draw()

def overlap_test():
    r1 = Rectangle(Point(10.0, 300.0),Point(90.0, 100.0))
    r2 = Rectangle(Point(70.0, 180.0), Point(200.0, 150.0))
    print("r1 and r2 overlap? " + str(r1.overlaps(r2)))    

    r3 = Rectangle(Point(10.0, 300.0),Point(90.0, 100.0))
    r4 = Rectangle(Point(100.0, 180.0), Point(200.0, 150.0))
    print("r3 and r4 overlap? " + str(r3.overlaps(r4)))    

def intersection_test():
    turtle.hideturtle()
    r1 = Rectangle(Point(10.0, 300.0),Point(90.0, 100.0))
    r2 = Rectangle(Point(70.0, 180.0), Point(200.0, 150.0))
    turtle.color("black")
    r1.draw()
    r2.draw()
    turtle.color("red")
    theintersection = r1.intersection(r2)
    theintersection.draw()
    print("Area of interesection: " + str(theintersection.area()))
