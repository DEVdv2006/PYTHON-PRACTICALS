import math
wallHeight=int(input("Enter Height of wall: "))
angle_degrees=int(input("Enter the leaning angle of ladder"))
#it is necessary to convert angle in degrees into radians since python function works with radian
ladderHeight=wallHeight/math.sin(math.radians(angle_degrees))
print(ladderHeight)
