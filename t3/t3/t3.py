import turtle

bob = turtle.Turtle()
bob.getscreen().bgcolor("#994444")
bob.speed(100)




def star(turtle, size):
    if size <= 7:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
 
    

star(bob, 360)

turtle.done()


