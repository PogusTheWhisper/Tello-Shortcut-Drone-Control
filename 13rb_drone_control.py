"""
==================================================================
Created: 25/10/23
Last Modeified: 28/10/23
==================================================================                                    
Credit: Naphat Sornwichai
        Wasupol Chaowsanguan 
        Hattakron Phannarak 
        Surawit Pakeepol
        Thanayot Monthlchachat 
        Nawin Charassangsomboon
        Metapat Nitimetviranon
From RB134 M.5/2 & 5/3

Email: NaphatSorn.Contact@gmail.com
Instagram: https://www.instagram.com/pogus_the_whisper/
Linkedin: https://www.linkedin.com/in/naphat-sornwichai-25759426a/
==================================================================
เคลื่อนที่ (movement)
w-ระยะ           forward
a-ระยะ           left
s-ระยะ           back
d-ระยะ           right
==================================================================
ตีลังกา (flip)
f-w             flip forward
f-a             flip left
f-s             flip back
f-d             flip right
==================================================================
หมุน  (rotate)
ror-องศา        rotate right
rol-องศา        rotate left
==================================================================
การควบคุมทั่วไป (common control)
t               take off
l               landing
b               battery
h               height
scan            scan-qr
speed           speed
bounce-ระยะ-ครั้ง  bounce
==================================================================
"""

from rcsa_dev_kit_edu_python_lib.fly_tello import *

def main():
    my_tellos = ['<paste here>']  # Your drone serial number
    print_menu()
    with FlyTello(my_tellos) as fly:
        while True:
            try :
                user_input = input("Enter your command: ")
                handle_user_input(fly, user_input)
            except KeyboardInterrupt as e: # Hide error when press ctrl+c for terminate monitor
                fly.stop()
                
                

def print_menu():
    print("====================================================================================================")
    print("|                               drone Monitor (Control & More!!!)                                  |")
    print("====================================================================================================")
    print("| t=takeoff, l=land, b=battery?, s=speed?, h=height, q=exit                                        |")
    print("| w-distance, a-distance, d-distance, s-distance, up-distance, down-distance                       |")
    print("| ror-angle, rol-angle, bounce, scan, scan-loop                                                    |")
    print("====================================================================================================")
    print("|'w': 'forward', 'a': 'left', 'd': 'right', 's': 'back', 'up': 'up', 'down': 'down', 'f': 'flip',  |")
    print("|'ror': 'rotate_cw', 'rol': 'rotate_ccw'                                                           |")
    print("====================================================================================================")
    print("|                                          Credits                                                 |")
    print("|                                    Wat Rajabopit RB134                                           |")
    print("|                            Read full credits in comment section                                  |")
    print("|                            Email: NaphatSorn.Contact@gmail.com                                   |")
    print("====================================================================================================")
    
    

def handle_user_input(fly, user_input):
    direction = {'w': 'forward', 'a': 'left', 'd': 'right', 's': 'back', 'up': 'up', 'down': 'down', 'f': 'flip', 'ror': 'rotate_cw', 'rol': 'rotate_ccw'}
    # Commends shortcut
    split_input = user_input.split('-') # Separate input by separating sentences with a - sign.

    if user_input == 't': # Take off from start point
        print('Takeoff')
        fly.takeoff()
    elif user_input == 'l': # Landding at where you are
        print('Land')
        fly.land()
    elif user_input == 'b': # Check % battery
        print('Battery?')
        fly.get_battery()
    elif user_input == 'speed': # Check speed
        print('Speed?')
        fly.get_speed()
    elif user_input == 'h': # Check height
        print('Height')
        fly.get_height()
        
    # Waiting for inspection to see if there is anything wrong.
    # elif user_input == "bounce":
    #     print('Bounce')
    #     fly.bounce(dist=100, times=3)
    
    elif user_input == 'scan':
        fly.stream_on(tello=1)
        start_video()      # Open camera
        print("WHERE QR!!!")
        while True:
            QR = find_QR()
            if QR != None: # Detact qr
                print(QR)
                time.sleep(1) # Prevent drone freezing
                if QR[1] != '': # Check that qr is not damaged
                    for round in range(int(QR[1])): # Follow the qr task
                        fly.rotate_ccw(angle=360)
                        fly.flip('back')
                        stop_video()
                        break
                    
    # You can create some "combo" or shortcuts at this point.
    # like this
    
    elif user_input == 'combo1' or user_input == 'cb1': # This combo will create a staircase flight pattern in a square shape.
        dist_cb1 = 50            # Easy right?
        direction_cb1 = 'forward' 
        angle_cb1 = 90
        for round in range(3):
            for side in range(4):
                fly.forward(dist=dist_cb1)
                fly.flip(direction=direction_cb1)
                fly.rotate_cw(angle=90)
                fly.up(dist=dist_cb1)
                
    elif user_input == 'combo2' or user_input == 'cb2': # This combo will create a reverse staircase flight pattern from combo1 in square shape.
        dist_cb1 = 50
        direction_cb1 = 'back' 
        angle_cb1 = 90
        for round in range(3):
            for side in range(4):
                fly.back(dist=dist_cb1)
                fly.flip(direction=direction_cb1)
                fly.rotate_ccw(angle=90)
                fly.down(dist=dist_cb1)
                
                   
        
    elif split_input[0] in direction: # Reformat command from shortcut
        if split_input[0] == 'ror' or split_input[0] == 'rol': # Rotate like ror-150 or rol-150
            func = f"fly.{direction[split_input[0]]}(angle={split_input[1]})"
            print('Rotate')
            eval(func)
        elif split_input[0] in direction and split_input[0] == 'f': # Flip like f-w or f-s
            func = f"fly.{direction[split_input[0]]}(direction='{direction[split_input[1]]}')"
            print('flip')
            eval(func)
        elif split_input[0] in direction and split_input[0] == 'bounce': # Bounce like bounce-100-3 or bounce-150-2
            func = f"fly.bounce(dist={split_input[1]}, times={split_input[2]})"
            print('Bounce')
            eval(func)
        else:
            func = f'fly.{direction[split_input[0]]}(dist={split_input[1]})' # Movement like w-150 or s-75 or up-30
            print(func)
            eval(func)
    elif user_input == 'q': # Exit monitor
        print('Exit Program')
        fly.Stop()
    else: # Umm... Just ignore it.
        print('what the fuck?!?!?')

main() # Run full script