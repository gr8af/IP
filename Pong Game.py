# Implementation of classic arcade game Pong

import pysimplegui as sg
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = True
RIGHT = False
keymap = sg.KEY_MAP
miny_pos = HALF_PAD_HEIGHT
maxy_pos = HEIGHT - HALF_PAD_HEIGHT
score1 = 0
score2 = 0
direct = ''
started = False

def restart():
    global score1, score2, direct, ball_pos
    
    score1 = score2 = direct =0
    
    ball_bos = [300, 200]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    if direction == RIGHT:
        xr = random.randrange(120,240)/ 60
        yr = - random.randrange(60,150)/ 60
        
        ball_vel = [xr, yr]
    
    elif direction == LEFT:
        xl = - random.randrange(120,240)/ 60
        yl = - random.randrange(60,180)/ 60
        
        ball_vel = [xl, yl]
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos  # these are numbers
    global score1, score2  # these are ints
    global started, direct
    
    ball_pos = [300, 200]
    
    if started:
        if direct:
            spawn_ball(RIGHT)
            
        
        else:
            spawn_ball(LEFT)
    
    paddle1_pos = 200
    paddle2_pos = 200
    
    paddle1_vel = 0
    paddle2_vel = 0
    
def draw(canvas):
    global started, score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global direct
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if started:
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

    else:
        canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'white', 'white')
    
    if ball_pos[1] <= 0 + BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1] 
    
    elif ball_pos[0] <= BALL_RADIUS + PAD_WIDTH + 5 and paddle1_pos + 45 > ball_pos[1] > paddle1_pos - 40:
        ball_vel[0] = - ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH - 5 and paddle2_pos + 45 > ball_pos[1] > paddle2_pos - 40:
        ball_vel[0] = - ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1    
    
      
    
    
    # draw ball
    
    canvas.draw_circle(ball_pos, BALL_RADIUS, 0.1, 'white', 'white')
    
    # update paddle's vertical position, keep paddle on the screen
    
    if paddle2_pos >= miny_pos:

        paddle2_pos += paddle2_vel
    
    else:
        paddle2_pos = miny_pos
    
    if paddle2_pos <= maxy_pos:
        
        paddle2_pos += paddle2_vel
    
    else:
        paddle2_pos = maxy_pos
    
    if paddle1_pos >= miny_pos:
        
        paddle1_pos += paddle1_vel
        
    else:   
        paddle1_pos = miny_pos
        
    if paddle1_pos <= maxy_pos:
        
        paddle1_pos += paddle1_vel
    
    else:   
        paddle1_pos = maxy_pos
    # draw paddles
    
    pad1_top = paddle1_pos + HALF_PAD_HEIGHT
    pad1_bottom = paddle1_pos - HALF_PAD_HEIGHT
    pad2_top = paddle2_pos + HALF_PAD_HEIGHT
    pad2_bottom = paddle2_pos - HALF_PAD_HEIGHT
    
    canvas.draw_line([HALF_PAD_WIDTH, pad1_top], [HALF_PAD_WIDTH, pad1_bottom], PAD_WIDTH, 'blue' )
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, pad2_top], [WIDTH - HALF_PAD_WIDTH, pad2_bottom], PAD_WIDTH, 'blue')
    # determine whether paddle and ball collide
    
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS - 5:
        ball_pos = [300, 200]
        direct = True
        score2 += 1
        started = False
        
    elif ball_pos[0] >= WIDTH + 5 - (PAD_WIDTH + BALL_RADIUS):
        ball_pos = [300, 200]
        score1 += 1
        direct = False
        started = False
    
    # draw scores
    
    canvas.draw_text(str(score2), [500, 50], 30, 'white')
    canvas.draw_text(str(score1), [100, 50], 30, 'white')
    
def keydown(key):
    global paddle1_vel, paddle2_vel, started, direct
        
    if key == keymap['space']:
        if not started:
            started = True
            new_game()
    
    if key == keymap['up']:
        paddle2_vel = -2
        
    
    if key == keymap['down']:
        paddle2_vel = 2
        
    if key == keymap['w']:
        paddle1_vel = -2
        
    
    if key == keymap['s']:
        paddle1_vel = 2   
    
def keyup(key):
    global paddle1_vel, paddle2_vel
        
    if key == keymap['up']:
        paddle2_vel = 0
        
    
    if key == keymap['down']:
        paddle2_vel = 0
        
    if key == keymap['w']:
        paddle1_vel = 0
        
    
    if key == keymap['s']:
        paddle1_vel = 0



# create frame
frame = sg.create_frame("Pong", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.set_draw_handler(draw)

frame.add_button('RESTART', restart)

label = frame.add_label('Press space to start the game', 200)

# start frame
new_game()
frame.start()
