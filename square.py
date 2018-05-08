import turtle

def draw_turtles():
    window = turtle.Screen()
    window.bgcolor("pink")

    draw_square(pari)
    
    window.exitonclick()
    
def draw_square(flower): 
    pari = turtle.Turtle()
    pari.shape("turtle")
    pari.color("blue")
    pari.speed(10)

    for j in range(0,72):
        
        pari.forward(100)
        pari.right(45)
        pari.forward(100)
        pari.right(135)
        pari.forward(100)
        pari.right(45)
        pari.forward(100)
        pari.left(20)
    pari.right(90)
    pari.forward(300)
        

draw_turtles()

