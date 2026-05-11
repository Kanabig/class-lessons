import turtle as t

def draw(length, n):
    t.shape

    for i in range(n):
        t.forward(length)
        t.left(360/n)

length = 40
appendLength = 10
angleCount = 12
direction = 90
padding = 3

t.speed(0)
t.goto(-length/2, -300)

while(True):
    t.setheading(direction)
    draw(length, angleCount)
    length += appendLength
    t.forward(padding)

