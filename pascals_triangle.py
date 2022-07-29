import turtle
import math 

SIDE_LENGTH = 50
WIDTH = SIDE_LENGTH * math.sqrt(3)
Y_OFFSET = SIDE_LENGTH / 2

BACKGROUND_COLOR = "white" # '#FFD8AC'
LINE_COLOR = "black"
ODD_FILL_COLOR = "grey90"
ODD_TEXT_COLOR = "black"
EVEN_FILL_COLOR = "white"
EVEN_TEXT_COLOR = "black"

turtle.setup()
turtle.screensize(3000, 3000, BACKGROUND_COLOR)

turtle.hideturtle()
turtle.speed(0)
# turtle.fillcolor("#FFE66E")

def hexagon(row, column, number):
  x = (column - row/2) * WIDTH
  y = row * -3/2*SIDE_LENGTH
  turtle.color(LINE_COLOR)
  turtle.penup()
  turtle.setpos(x, y)
  turtle.pendown()  
  turtle.setheading(30)

  if (number % 2 == 0):
    turtle.fillcolor(EVEN_FILL_COLOR)
  else:
    turtle.fillcolor(ODD_FILL_COLOR)
  
  turtle.begin_fill()

  for i in range(6):
    turtle.forward(SIDE_LENGTH)
    turtle.right(60)

  turtle.end_fill()
  
  turtle.penup()
  turtle.setpos(x+WIDTH/2, y-SIDE_LENGTH/2-16)
  turtle.pendown()  
  if (number % 2 == 0):
    turtle.color(EVEN_TEXT_COLOR)
  else:
    turtle.color(ODD_TEXT_COLOR)
  turtle.write(number, align="center", font=('Arial', 32, 'normal'))

def pascals(num_rows):
  rows = [[1], [1,1]]
  for i in range(2, num_rows):
    new_row = [1]
    prev_row = rows[i-1]
    for j in range(len(prev_row)-1):
      new_row.append(prev_row[j]+prev_row[j+1])
    new_row.append(1)
    rows.append(new_row)
  return rows


# hexagon(0,0)
# hexagon(-WIDTH, -3/2*SIDE_LENGTH)
# hexagon(WIDTH, -3/2*SIDE_LENGTH)

pascals_triangle = pascals(8)
for i, row in enumerate(pascals_triangle):
  for j, num in enumerate(row):
    hexagon(i, j, num)


turtle.done()