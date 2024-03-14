from math import pi

def circle_area(r):
    area = pi*(r**2)
    return area

raduises = [2, 0, -3, True, "rad"]
log_msg = "Area of circles with r = {radius} is {area}"

for r in raduises:
    A = circle_area(r)
    print(log_msg.format(radius=r, area=A))