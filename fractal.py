import turtle
import time

t = turtle.Turtle()
t.speed(100)

def koch(ln, n):
    if n == 0:
        t.fd(ln)
    else:
        koch(ln / 3, n - 1)
        t.left(60)
        koch(ln / 3, n - 1)
        t.right(120)
        koch(ln / 3, n - 1)
        t.left(60)
        koch(ln / 3, n - 1)

print("Введите длину сегмента:")
ln = int(input())
print("Введите глубину рекурсии:")
n = int(input())
start = time.time()
koch(ln, n)
print("Время : ", (time.time() - start))

turtle.done()