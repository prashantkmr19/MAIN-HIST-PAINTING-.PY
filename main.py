###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)

#print(rgb_colors)
import turtle as turtle_module
import random

tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
turtle_module.colormode(255)
color_list = [(246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153)]
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100
for dot_counts in range(1,number_of_dots+ 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_counts % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(100)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()