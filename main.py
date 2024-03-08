#NEW:
## work with image file with py turtle
## EVENT LISTENER: The turtle module allows us to detect when the user has hit certain keys on the keyboard or moved/clicked the mouse. Whenever the user performs an action as such it is called an event. We can listen for events and trigger functions to run if we "hear" the event.


FONT = ('Arial', 8, 'normal')

from turtle import Turtle,Screen
import pandas

#TODO set up the screen: turtle = U.S. picture
screen = Screen()
screen.screensize(800,600)
turtle = Turtle() ## instance_1
screen.title('Name the State')


## turtle.addshape(name, shape=None) OR  turtle.register_shape()
## 将一个海龟形状加入 TurtleScreen 的形状列表。
## i.e. screen.register_shape("turtle.gif") -- name 为一个 gif 文件的文件名， shape 为 None: 安装相应的图像形状
image = 'blank_states_img.gif'
screen.addshape(image)  ## add the image.gif to the screen
turtle.shape(image)  ## now the image is usable for turtle.



#TODO: Get mouse-click coordinates in py turtle, to get the location of each State on map relative to Turtlescreen
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

## turtle.onscreenclick(fun, btn=1, add=None) -- an event listener!!!!
## fun: 一个函数，调用时将传入两个参数表示在画布上点击的坐标。(只接受函数？？）
## i.e. screen.onclick(turtle.goto) # Subsequently clicking into the TurtleScreen will make the turtle move to the clicked point.
## Event Listener: The turtle module allows us to detect when the user has hit certain keys on the keyboard or moved/clicked the mouse. Whenever the user performs an action as such it is called an event. We can listen for events and trigger functions to run if we "hear" the event.

## turtle.mainloop()
## 开始事件循环 - 调用 Tkinter 的 mainloop 函数。必须作为一个海龟绘图程序的结束语句。
## 约等于screen.exisonclick: 为了保持screen不消失






# START THE GAME
data = pandas.read_csv('50_states.csv')
states_list = data.state.to_list()
coor_x_list = data.x.to_list()
coor_y_list = data.y.to_list()

pen = Turtle()
pen.hideturtle()
state_guessed = 0
while state_guessed < 50:

    # TODO: add a pop-up for user answer collection
    user_answer = screen.textinput(title='Guess the State', prompt="Guess a State's Name").title()
    ## turtle.textinput(title, prompt)¶
    ## 参数: title -- string; prompt -- string

    for state in states_list:
        # TODO check if the answer exists; Type out the name on pic if guessed right
        if user_answer == state:
            state_index = states_list.index(state) ##  list. index() function returns the index of the first occurrence of an item in a list.
            x = coor_x_list[state_index]
            y = coor_y_list[state_index]
            # print(f'item={state}  state_index={state_index} coor=({x},{y})')  ## test

            pen.penup()
            pen.color('black')
            pen.goto(x,y)
            pen.pendown()
            pen.write(f"{state}", align="center", font=FONT)

            #TODO score: record the correct answer in list -> track the score: i.e. 4/50
            ## list.remove (elements) OR list.pop (index)
            state_list = states_list.remove(state)
            coor_x_list.pop(state_index)
            coor_y_list.pop(state_index) ##1. 怕有重复数字; 2. list.pop() will return a value, not a list!!!

            states_remained = len(states_list)
            state_guessed = 50 - states_remained
            screen.title(f'Name the State  {state_guessed}/50')
            #print(f'{state_guessed}/50')  ## test

    if user_answer.title() == 'Exit':   ## screte code ## break allows you to exit a loop
        break

# # METHOD 2 获取数据
# ## TODO check if the answer exists; Type out the name on pic if guessed right
# data = pandas.read_csv()
# guessed = []
# if user_answer in states_list:
#     column = data.state  ## all column
#     row = data[data.state == user_answer] ## specific rows: pull out the row where state == user_answer state
#     #     state    x    y
#     # 31  New York 236 104
#
#     pen.goto(int(row.x), int(row.y)) ## original:Strings!!! What: tap into the attributions using the names of the columns !!!
#     pen.write(row.state.item())  ## the cell; ## item(): no spelling format request
#
#     guessed.append(row.state.item())
#     remain = 50-len(guessed)


# TODO export the unguessed states to a CSV file
df = pandas.DataFrame(states_list)
df.to_csv('states_to_learn.csv')

screen.exitonclick()