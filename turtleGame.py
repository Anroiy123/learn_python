import turtle
import time
import random

# Thiết lập màn hình
wn = turtle.Screen()
wn.title("Game Rùa Qua Đường")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)
 
# Tạo rùa (nhân vật chính)
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, -250)
player.setheading(90)

# Tạo danh sách ô tô
cars = []

# Tạo lớp ô tô
class Car(turtle.Turtle):
    def __init__(self, y_position):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(["red", "blue", "yellow", "purple"]))
        self.penup()
        self.goto(400, y_position)
        self.speed = random.uniform(0.1, 0.2)

# Hàm kiểm tra xem y có quá gần với ô tô hiện có không
def is_too_close(y, cars, min_distance=50):
    for car in cars:
        if abs(car.ycor() - y) < min_distance:
            return True
    return False

# Hàm điều khiển rùa
def move_up():
    y = player.ycor()
    if y < 250:
        player.sety(y + 20)

def move_down():
    y = player.ycor()
    if y > -250:
        player.sety(y - 20)

# Gắn phím điều khiển
wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")

# Tạo điểm số
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Điểm: 0", align="center", font=("Courier", 24, "normal"))

# Biến đếm để kiểm soát tần suất tạo ô tô
car_spawn_counter = 0
car_spawn_interval = 50

# Biến để kiểm tra chiến thắng
game_won = False

# Vòng lặp chính của game
game_over = False
while not game_over and not game_won:
    wn.update()
    
    # Tạo ô tô mới với tần suất được kiểm soát
    car_spawn_counter += 1
    if car_spawn_counter >= car_spawn_interval:
        attempts = 0
        max_attempts = 10
        while attempts < max_attempts:
            y = random.randint(-200, 200)
            if not is_too_close(y, cars, min_distance=50):
                car = Car(y)
                cars.append(car)
                car_spawn_counter = 0
                break
            attempts += 1
    
    # Di chuyển ô tô và kiểm tra va chạm
    for car in cars[:]:
        car.goto(car.xcor() - car.speed, car.ycor())
        
        # Xóa ô tô khi ra khỏi màn hình
        if car.xcor() < -400:
            cars.remove(car)
            car.hideturtle()
            score += 1
            score_pen.clear()
            score_pen.write(f"Điểm: {score}", align="center", font=("Courier", 24, "normal"))
        
        # Kiểm tra va chạm với rùa
        if player.distance(car) < 20:
            game_over = True
    
    # Kiểm tra nếu rùa đến đích
    if player.ycor() > 240:
        game_won = True  # Đặt cờ chiến thắng

# Hiển thị thông báo kết quả
if game_over:
    game_over_pen = turtle.Turtle()
    game_over_pen.speed(0)
    game_over_pen.color("red")
    game_over_pen.penup()
    game_over_pen.hideturtle()
    game_over_pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
    # Hiển thị điểm cuối cùng
    score_pen.goto(0, 220)
    score_pen.write(f"Điểm cuối: {score}", align="center", font=("Courier", 24, "normal"))

elif game_won:
    win_pen = turtle.Turtle()
    win_pen.speed(0)
    win_pen.color("green")
    win_pen.penup()
    win_pen.hideturtle()
    win_pen.write("CHÚC MỪNG! BẠN ĐÃ THẮNG!", align="center", font=("Courier", 36, "bold"))
    # Hiển thị điểm cuối cùng
    score_pen.clear()
    score_pen.goto(0, -40)
    score_pen.write(f"Điểm: {score}", align="center", font=("Courier", 24, "normal"))

# Giữ cửa sổ mở
wn.mainloop()