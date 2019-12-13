import pygame
import logging
from pyparrot.Bebop import Bebop

pygame.init()
size = [100, 100]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('TeleOp')

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

if pygame.joystick.get_count() == 0:
    print("No joysticks found")
    done = True
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("Initialized %s" % (joystick.get_name()))
    print("Number of buttons %d. Number of axis %d, Number of hats %d" %
          (joystick.get_numbuttons(), joystick.get_numaxes(),
           joystick.get_numhats()))

left_trigger_initialized = False
right_trigger_initialized = False

# -------- Initialize drone ------------



bebop = Bebop(drone_type="Bebop2")
success = bebop.connect(num_retries=3)

logging.error("Connected = {}".format(success))

# -------- Main Program Loop -----------

while not done:
    try:
        # EVENT PROCESSING STEP
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
        executing_command = False

        user_movement = False
        MAX_VEL = 90
        roll = joystick.get_axis(0) * MAX_VEL
        pitch = joystick.get_axis(1) * -MAX_VEL
        yaw = joystick.get_axis(2) * MAX_VEL
        gaz = joystick.get_axis(3) * -MAX_VEL

        if roll != 0:
            user_movement = True
        if pitch != 0:
            user_movement = True
        if yaw != 0:
            user_movement = True
        if gaz != 0:
            user_movement = True

        if user_movement == True:
            bebop.fly_direct(roll=roll, pitch=pitch, yaw=yaw, vertical_movement=gaz, duration=0.5)
        else:
            bebop.fly_direct(0, 0, 0, 0, 0.5)

        
        if joystick.get_button(0) == 1:
            executing_command = True
            bebop.safe_land(timeout=3)

        if joystick.get_button(3) == 1:
            executing_command = True
            bebop.safe_takeoff(timeout=3)

        if joystick.get_button(4) == 1:
            print("Button 4 pressed")

        if joystick.get_button(5) == 1:
            print("Button 5 pressed")

        if joystick.get_button(6) == 1:
            print("Button 6 pressed")

        if joystick.get_button(7) == 1:
            print("Button 7 pressed")

        # Triggers initialize at 0 and then reset to -1
        if joystick.get_axis(2) != 0:
            left_trigger_initialized = True

        if joystick.get_axis(5) != 0:
            right_trigger_initialized = True

        if left_trigger_initialized and joystick.get_axis(2) == 1:
            pass

        if right_trigger_initialized and joystick.get_axis(5) == 1:
            pass

        (hat_x, hat_y) = joystick.get_hat(0)
        if hat_x != 0 or hat_y != 0:
            print("Hat %d, %d" % (hat_x, hat_y))

        bebop.smart_sleep(timeout=0.05)
    except Exception as e:
        logging.error(e)
        done = True

# Close the window and quit.
pygame.quit()
