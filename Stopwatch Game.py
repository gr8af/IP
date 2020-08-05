# template for "Stopwatch: The Game"
import simplegui
# define global variables
w = "0:00.0"
t = 0
y = 0
x = 0
d = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    global w, d
    a =	(time / 600) % 10
    b = (time / 100) % 6
    c = (time / 10)  % 10
    d = (time)       % 10
    w = (str(a) + ":"  + str(b) + str(c) + "." + str(d))
    return w
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global y, x, d
    if (timer.is_running()):
        y += 1
        if (d == 0):
            x += 1
    timer.stop()

def reset():
    global t, x ,y, w
    t = x = y = 0
    w = "0:00.0"
    timer.stop()
    
def startstop():
    global x, y, d
    if (timer.is_running()):
        y += 1
        if (d == 0):
            x += 1
        timer.stop()
    else:
        timer.start()
        

# define event handler for timer with 0.1 sec interval
def sec():
    global t
    t += 1
    format(t)

# define draw handler
def draw(canvas):
    global w, x, y
    canvas.draw_text(str(w), (60, 110), 30, "White")
    canvas.draw_text(str(x) + "/" + str(y), (170, 15,),12, "Green")
# create frame

frame	=	simplegui.create_frame("Stopwatch", 200, 200)
timer	=	simplegui.create_timer(100,	sec)
frame.set_draw_handler(draw)

# register event handlers
button1 = frame.add_button("Start", start, 100)
button2 = frame.add_button("Stop", stop, 100)
button3 = frame.add_button("Reset", reset, 100)
button4 = frame.add_button("Start/Stop", startstop, 100)

# start frame
frame.start()
# Please remember to review the grading rubric
