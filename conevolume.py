PI = 3.1415926553589793

height_input = int(input('Please input the hieght of the cone: '))
radius_input = int(input('Please input the radius of the cone: '))

volume = (PI) * (radius_input * radius_input) * (height_input // 3)

print(volume)