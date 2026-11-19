import turtle

pen = turtle.Turtle() 

###
# Draw a square
#
def draw_square(length): # Przyjmujemy długość boku kwadratu.
    for i in range(4):       # Powtarzamy rysowanie cztery razy, po jednym razie na każdy bok.
        pen.forward(length) # 90 stopni
        pen.right(90) # Obracamy żółwia w prawo o 90 stopni.

#draw rectangle
def draw_rectangle(length_a, length_b):
    for i in range(2): # Dwa razy rysujemy parę boków, żeby otrzymać wszystkie cztery.
        pen.forward(length_a) # Rysujemy bok o długości length_a.
        pen.right(90) #90 st
        pen.forward(length_b) #rysujemy bok b
        pen.right(90) #90 st

#draw triangle
def draw_triangle(length): #trojkat rownoboczny
    for i in range (3): # rysujemy 3 razy
        pen.forward(length)  # Rysujemy bok o długości 
        pen.right(120) #skręt o 12 st, KĄT ZEWNĘTRZNY!!!! (wew. 60 st.)
