
import turtle
turtle.bgcolor("black")
p=turtle.Pen()
#        0       1       2       3       4        5       6        7     8       9
cores=["red","orange","blue","green","yellow","purple","white","brown","gray","pink"]

#           0         1        2           3         4        5        6         7      8         9
animais=["gato","cachorro","tartaruga","peixe","elefante","macaco","ovelha","camelo","cavalo","passaro"]

for x in range(100):
    
    p.penup()
    p.forward(x*5)
    resto=x%len(animais)
    p.pencolor(cores[resto])
    animal=animais[resto]
    p.write(animal,font=("Arial",int(x*0.6),"bold"))
    p.left(360/(len(animais)+2))
    
