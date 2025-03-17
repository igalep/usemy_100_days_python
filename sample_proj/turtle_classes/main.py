from turtle import Turtle,Screen
from prettytable import PrettyTable


# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(150)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()


table = PrettyTable()
table.field_names = ['Pokemon Name' , 'Type']
table.add_row(['Pikachu', 'Electric'])
table.add_row(['AAA', 'BBBB'])
table.add_row(['123', '456'])
print(table)
