import turtle

def draw_name():
	name = turtle.Turtle()
	surname = turtle.Turtle()
	window = turtle.Screen()

#Background
	window.bgcolor("blue")

#Drawing F
	name.left(90)
	name.forward(50)
	name.right(90)
	name.forward(50)
	name.backward(50)
	name.left(90)
	name.forward(50)
	name.right(90)
	name.forward(90)
#Drawing M
	surname.penup()
	surname.setpos(150,0)
	surname.pendown()
	surname.left(90)
	surname.forward(100)
	surname.left(20)
	surname.backward(100)
	surname.left(-30)
	surname.forward(100)
	surname.right(160)
	surname.forward(100)


	window.exitonclick()
draw_name ()
