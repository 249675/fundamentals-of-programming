import turtle

import figures_10_5_4 as figures # Importujemy pierwszy plik pod krótszą nazwą „figures”.

# Set up the screen
window = turtle.Screen() # Pobieramy okno, w którym pojawią się figury.
window.bgcolor("lightgreen") #kolor tła

# Create the turtle
pen = figures.pen # Pobieramy tego samego żółwia, którego używają funkcje rysujące.
pen.speed(5) #szybkość rysowania

# Side length
side_length = 100 # Ustalamy długość boku obu kwadratów.

# Draw a square
figures.draw_square(side_length) # Rysujemy pierwszy kwadrat w pozycji początkowej żółwia.

#move pen
pen.penup()  #Podnosimy pisak, żeby podczas przesuwania nie powstała linia.
pen.goto(-200, 100) # miejsce na planszy
pen.pendown() #kładziemy pisak

#draw a rectangle
figures.draw_rectangle(length_a=150, length_b=80) # Rysujemy pierwszy prostokąt o bokach 150 i 80.

#move pen
pen.penup() # podnosimy pisak
pen.goto(100, 150) # przesuwamy na takie pozycje
pen.pendown() #kładziemy

#draw triangle
figures.draw_triangle(length=100) # rysujemy trójkąt o boku 100

#move pen
pen.penup() #podnmsimy
pen.goto(-200, -100) # przesuwamy
pen.pendown() #kładziemy

# Draw a square
figures.draw_square(side_length) # nast. kwadrat

#move pen
pen.penup()
pen.goto(30, -130)
pen.pendown()

#draw a rectangle
figures.draw_rectangle(length_a=150, length_b=80) # nast prostokat

#move pen
pen.penup()
pen.goto(-200, 250)
pen.pendown()

#draw triangle
figures.draw_triangle(length=100) # nast trojkat

# Hide the turtle and finish
pen.hideturtle()  # Ukrywamy żółwia po zakończeniu rysowania.
window.mainloop() # Utrzymujemy okno otwarte do momentu, aż użytkownik je zamknie.