import turtle
import random

# 화면 설정
s = turtle.Screen()
s.setup(600, 600)
s.bgcolor("lightblue")
s.title("고양이 벽돌 피하기 게임")

# 고양이 캐릭터 설정
cat = turtle.Turtle()
cat.shape("turtle")
cat.color("gray")
cat.penup()
cat.goto(0, -250)
cat.speed(0)

# 벽돌 설정
brick = turtle.Turtle()
brick.shape("square")
brick.color("brown")
brick.shapesize(stretch_wid=1, stretch_len=3)
brick.penup()
brick.speed(0)
brick.goto(0, 250)

# 게임 설정
brick_speed = 5
cat_speed = 20
score = 0

# 왼쪽으로 이동
def move_left():
    x = cat.xcor()
    x -= cat_speed
    if x < -290:
        x = -290
    cat.setx(x)

# 오른쪽으로 이동
def move_right():
    x = cat.xcor()
    x += cat_speed
    if x > 290:
        x = 290
    cat.setx(x)

# 키보드 입력 연결
s.listen()
s.onkey(move_left, "Left")
s.onkey(move_right, "Right")

# 게임 루프
while True:
    # 벽돌을 아래로 이동
    y = brick.ycor()
    y -= brick_speed
    brick.sety(y)

    # 벽돌이 화면 아래로 떨어지면
    if y < -300:
        brick.goto(random.randint(-250, 250), 250)
        score += 1
        brick_speed += 0.5  # 벽돌 속도 증가
    
    # 충돌 체크
    if brick.distance(cat) < 50:
        print("Game Over! Score:", score)
        break

s.bye()  # 게임 종료
