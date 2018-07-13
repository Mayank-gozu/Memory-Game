# implementation of card game - Memory

import simplegui
import random

#print len(lst)
# helper function to initialize globals
def new_game():
    global state1i,state2i,state,turns,lst,exposed,count
    lst = range(8)+range(8)
    random.shuffle(lst)
    count = 0
    #state1i = 0
    #state2i = 0
    state = 0
    turns = 0
    exposed = [False]*16

    label.set_text("Turns: "+ str(turns))
    label1.set_text("Result Unkown!")

def detect_card(pos):
    return pos[0]// 50



# define event handlers
def mouseclick(pos):
    global exposed
    global state,state1i,state2i,turns,count
    global card1, card2
    # add game state logic here
    #check to see if click was on line
    if pos[0] % 50 !=0 and pos[1]%100 !=0 and pos[0] !=0 and pos[1]!=0:
        if exposed[detect_card(pos)]:
            return None
        turns += 1
        if state == 0:
            card1 = detect_card(pos)
            exposed[card1] = True
            state = 1
            #state1i = i
            #turns = turns+1
        elif state == 1:
            card2 = detect_card(pos)
            state = 2
            exposed[card2] = True
            #card2 = lst[i]
            #state2i = i
        else:
            if lst[card1] != lst[card2]:
                exposed[card1] = False
                exposed[card2] = False
            card1 = detect_card(pos)
            exposed[card1] = True
            state = 1

        label.set_text("Turns: "+ str(turns))
        if count == 8:
            label1.set_text("You Won")
            new_game()







# cards are logically 50x100 pixels in size
def draw(canvas):
    for i in range(len(lst)):
        number = lst[i]
        canvas.draw_text(str(number),(50*i,90),110,"white")
        canvas.draw_line((50*i,0),(50*i,100),1,"white")
    for j in range(len(lst)):
        if not exposed[j]:
            canvas.draw_polygon([[50*j,0], [50*j,100], [50+50*j,100], [50+50*j,0]], 1, 'Yellow', 'Orange')
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)



# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
label = frame.add_label("Turns:")
label1 = frame.add_label("Result:")

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
