import turtle

# Khởi tạo màn hình turtle
t = turtle.Turtle()

# Vẽ thân mèo
t.fillcolor('gray')
t.begin_fill()
t.circle(100)
t.end_fill()

# Vẽ đầu mèo
t.fillcolor('white')
t.begin_fill()
t.circle(50)
t.end_fill()

# Vẽ tai mèo
t.fillcolor('gray')
t.begin_fill()
t.setheading(45)
t.circle(40, 90)
t.setheading(135)
t.circle(40, 90)
t.end_fill()

# Vẽ mũi mèo
t.fillcolor('black')
t.begin_fill()
t.penup()
t.setpos(20, 40)
t.pendown()
t.circle(15)
t.end_fill()

# Vẽ mắt mèo
t.fillcolor('green')
t.begin_fill()
t.penup()
t.setpos(35, 70)
t.pendown()
t.circle(10)
t.end_fill()

# Vẽ móng chân mèo
t.pensize(20)
t.pencolor('white')
t.penup()
t.setpos(-40, -110)
t.pendown()
t.setheading(180)
t.forward(50)
t.penup()
t.setpos(40, -110)
t.pendown()
t.setheading(0)
t.forward(50)

# Ẩn con trỏ turtle
t.hideturtle()

# Đợi người dùng đóng màn hình
turtle.done()
