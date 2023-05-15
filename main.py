import turtle
screen = turtle.Screen()
screen.title('FIBINACCI')
turtle.goto(0,0)
all = [0, 1];
def fibi(w, s):
    lent = len(all) - 1
    w = all[lent-1]
    s = all[lent]
    g = w + s
    all.append(g)
for i in range(200):
    fibi(0,1)
for i in all:
    turtle.circle(radius=i*2, extent=90)