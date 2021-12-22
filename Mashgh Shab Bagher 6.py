angles_input = input("").split()
int_angles = list(map(int, angles_input))
x = int_angles[0]
y = int_angles[1]
z = int_angles[2]


def is_triangle(int_angles):
    if x > 0 and x < 360 and y > 0 and y < 360 and z > 0 and z < 360:
        if sum(int_angles) == 180:
            print('Yes')
        else:
            print('No')
    else:
        print("No")


is_triangle(int_angles)
