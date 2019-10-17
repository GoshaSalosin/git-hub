import turtle

def Square(x,y,size,color,angel):
    turtle.pendown ()
    turtle.color (color)
    turtle.penup ()
    turtle.setx ( x )
    turtle.sety ( y )
    turtle.begin_fill ()
    turtle.pendown ( )
    turtle.right(angel)
    turtle.forward (size)
    turtle.right(90)
    turtle.forward ( size )
    turtle.right (90)
    turtle.forward ( size )
    turtle.right (90)
    turtle.forward ( size )
    turtle.end_fill ()
def Parallelogram(x,y,size,color,angel):
    turtle.pendown ()
    turtle.color (color)
    turtle.penup ()
    turtle.setx ( x )
    turtle.sety ( y )
    turtle.begin_fill ()
    turtle.pendown ( )
    turtle.right(angel)
    turtle.forward (size)
    turtle.right(60)
    turtle.forward ( size )
    turtle.right (120)
    turtle.forward ( size )
    turtle.right ( 60 )
    turtle.forward ( size )
    turtle.end_fill ()
def Triangle(x,y,size,color,angel):
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(angel)
    turtle.forward(size)
    turtle.right(60)
    turtle.forward(size)
    turtle.end_fill()

Square(100,100,150,"red",90)
Parallelogram(-100,-100,150,"blue",90)
Triangle(200,200,150,"green",90)

turtle.mainloop()