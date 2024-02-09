import turtle


def draw_pythagorean_tree(size, factor):
    size = 150

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(90, -150)
    t.left(90)
    t.pendown()

    t.forward(size)
    draw_node(t, size / 5 * 3, factor - 1)
    t.back(size)
    t.stamp


def draw_node(t, size, level):
    if (level < 1):
        return
    else:
        t.left(30)
        t.forward(size)
        draw_node(t, size / 5 * 3, level - 1)
        t.back(size)

        t.right(60)
        t.forward(size)
        draw_node(t, size / 5 * 3, level - 1)
        t.back(size)
        t.left(30)


if __name__ == '__main__':
    draw_pythagorean_tree(150, 9)
    turtle.mainloop()
