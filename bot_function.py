import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"

def kalp():
    kalp_sayi = random.randint(0,1)
    if kalp_sayi == 0:
        return "💌"
    if kalp_sayi == 1:
        return "❤️"
