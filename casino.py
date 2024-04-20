import random
def set_number():
    num = random.randint(0, 32)
    return num

def set_color():
    color = random.choice(["Green", "Red", "Black"])
    return color

def main_num(user_input):
    if user_input == 0:
        if user_input == set_number():
            return 30
        else:
            return -40
    else:
        if user_input == set_number():
            return 20
        else:
            return -25
    
def main_color(user_input):
    if user_input == "Green":
        if user_input == set_color():
            return 30
        else:
            return -40
    else:
        if user_input == set_color():
            return 5
        else:
            return -7