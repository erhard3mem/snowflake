import turtle
t = turtle.Turtle()
t.delay = 3


def fdd3(t,x):
    if(x<3):
        t.fd(x);
    else:
        t.fd(x/3);

def koch(t,x):
    fdd3(t,x);
    t.lt(60);    
    fdd3(t,x);
    t.rt(120);
    fdd3(t,x);
    t.lt(60);
    fdd3(t,x);
# is recursion necessary?
    
def schneeflocke(t,x):
    for i in range(2):          
        for i in range(30**2):          
            koch(t,x);
            t.rt(45);
            koch(t,x);
            t.lt(90);
            koch(t,x);
        for i in range(30**2):          
            koch(t,x);
            t.rt(45);
            koch(t,x);
            t.lt(90);
            koch(t,x);

schneeflocke(t,50);
