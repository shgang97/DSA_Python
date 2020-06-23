import turtle


def drawTree(branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(19)
        drawTree(branch_len - 12)
        t.left(38)
        drawTree(branch_len - 16)
        t.right(19)
        t.backward(branch_len)


t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
drawTree(75)
t.hideturtle()
turtle.done()
