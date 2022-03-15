#espiral1.py

import turtle
p=turtle.Pen()
p.speed(555)

turtle.bgcolor("black")
cores=["red","yellow","blue","green","orange","purple"]
lados=int(turtle.numinput("Escolha entre 2 e 6","Numeros de lados"))

for x in range(1000):
    resto=x%6
    cor=cores[resto]
    p.pencolor(cor)
    p.forward(x*3)
    p.left(360/(lados+1))
    p.width(x*lados/200)
    
