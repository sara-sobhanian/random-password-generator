import random
def make_pass(user_choice):

    if user_choice=='low':
        passlen=random.randrange(3,5)
    elif user_choice=='medium':
        passlen=random.randrange(6,10)
    elif user_choice=='high':
        passlen=random.randrange(11,20)
    else:
        return("user_choice = low/medium/high")

    s="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+=-,."
    p="".join(random.sample(s,passlen))
    return p
