import turtle

# 화면과 터틀 만들기
s = turtle.Screen()
s.setup(650, 800)
s.bgcolor("lightblue")

t = turtle.Turtle()
t.pensize(5)
t.speed(5)

# 얼굴 그리기
t.penup()
t.goto(0, -50)
t.pendown()
t.begin_fill()
t.color("black", "gray")
t.circle(100)  # 얼굴 원
t.end_fill()

# 왼쪽 귀 그리기
t.penup()
t.goto(-70, 70)
t.pendown()
t.begin_fill()
t.color("black", "gray")
t.setheading(120)
t.circle(-50, 60)
t.goto(-70, 70)
t.goto(-100, 130)
t.goto(-130, 70)
t.end_fill()

# 오른쪽 귀 그리기
t.penup()
t.goto(70, 70)
t.pendown()
t.begin_fill()
t.color("black", "gray")
t.setheading(60)
t.circle(50, 60)
t.goto(70, 70)
t.goto(100, 130)
t.goto(130, 70)
t.end_fill()

# 왼쪽 눈 그리기
t.penup()
t.goto(-35, 20)
t.pendown()
t.begin_fill()
t.color("black")
t.circle(10)  # 왼쪽 눈
t.end_fill()

# 오른쪽 눈 그리기
t.penup()
t.goto(35, 20)
t.pendown()
t.begin_fill()
t.circle(10)  # 오른쪽 눈
t.end_fill()

# 코 그리기
t.penup()
t.goto(0, 0)
t.pendown()
t.begin_fill()
t.color("pink")
t.setheading(0)
t.circle(7)  # 코
t.end_fill()

# 입 그리기
t.penup()
t.goto(0, -10)
t.pendown()
t.setheading(-90)
t.circle(20, 60)
t.penup()
t.goto(0, -10)
t.pendown()
t.setheading(-90)
t.circle(-20, 60)

# 수염 그리기
t.penup()
t.goto(-30, -10)
t.pendown()
t.setheading(0)
t.forward(50)  # 왼쪽 수염

t.penup()
t.goto(-30, -20)
t.pendown()
t.setheading(0)
t.forward(50)  # 왼쪽 수염 아래

t.penup()
t.goto(-30, 0)
t.pendown()
t.setheading(0)
t.forward(50)  # 왼쪽 수염 위

t.penup()
t.goto(30, -10)
t.pendown()
t.setheading(180)
t.forward(50)  # 오른쪽 수염

t.penup()
t.goto(30, -20)
t.pendown()
t.setheading(180)
t.forward(50)  # 오른쪽 수염 아래

t.penup()
t.goto(30, 0)
t.pendown()
t.setheading(180)
t.forward(50)  # 오른쪽 수염 위

t.hideturtle()
s.update()
s.mainloop()
