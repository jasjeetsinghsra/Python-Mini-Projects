import turtle

def draw_flower():
    playground=turtle.Screen()
    playground.bgcolor("white")
    pen1=turtle.Turtle()
    pen1.shape("arrow")
    pen1.color("blue")
    pen1.pencolor("blue")
    pen1.speed(0)
    for j in range(4):
        for i in range(9):
            pen1.forward(50)
            pen1.right(60)
            pen1.forward(50)
            pen1.right(120)
            pen1.forward(50)
            pen1.right(60)
            pen1.forward(50)
            pen1.right(160)
        pen1.right(10)
    pen2=turtle.Turtle()
    pen2.shape("turtle")
    pen2.color("blue")
    pen2.pencolor("blue")
    pen2.right(90)
    pen2.forward(200)
    
 
            
        
        
    playground.exitonclick()

draw_flower()
                            
                  
               
