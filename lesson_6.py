import turtle

def draw_turtles():
    window = turtle.Screen()
    window.bgcolor("pink")

    draw_square()
      
    window.exitonclick()
    
def draw_square(): 
    pari = turtle.Turtle()
    pari.shape("turtle")
    pari.color("red")
    pari.speed(1)

    for i in range(0,4):
        pari.forward(100)
        pari.right(90)

draw_turtles()


import turtle

def draw_turtles():
    window = turtle.Screen()
    window.bgcolor("pink")

    draw_square()
    draw_circle()
    draw_triangle()
    
    window.exitonclick()
def draw_square(): 
    pari = turtle.Turtle()
    pari.shape("turtle")
    pari.color("red")
    pari.speed(1)

    for i in range(0,4):
        pari.forward(100)
        pari.right(90)

def draw_circle():
    siri = turtle.Turtle()
    siri.shape("circle")
    siri.color("blue")
    siri.speed(1)
    siri.circle(100)

def draw_triangle():
    tri = turtle.Turtle()
    tri.shape("triangle")
    tri.color("green")
    tri.speed(1)
    tri.left(180)

    for j in range(0,3):
        tri.forward(200)
        tri.right(120)
    


draw_turtles()
