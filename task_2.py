import turtle

def koch_snowflake(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, depth-1)
        t.left(60)
        koch_snowflake(t, length, depth-1)
        t.right(120)
        koch_snowflake(t, length, depth-1)
        t.left(60)
        koch_snowflake(t, length, depth-1)

def draw_snowflake(length, depth):
    # Створення вікна та черепашки
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-length/2, length/3)
    t.pendown()

    # Малювання 3 відрізків для створення сніжинки
    for _ in range(3):
        koch_snowflake(t, length, depth)
        t.right(120)

    # Закриття вікна при кліку
    screen.exitonclick()

if __name__ == "__main__":
    length = 300
    depth = int(input("Введіть глибину рекурсії: "))
    draw_snowflake(length, depth)
