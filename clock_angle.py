hour=int(input())
minutes=int(input())

angle_hour = (hour* 60 + minutes ) * 0.5
angle_minute = 6 * minutes

angle = abs(angle_hour - angle_minute)
angle=min(angle, 360- angle)
print(angle)