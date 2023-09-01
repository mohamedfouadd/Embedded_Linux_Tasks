
pin_config = {}
pin_list = []

for i in range(0,8):
    pin = i
    direction = int(input("Enter direction for PIN" + str(pin) + " (0 for input, 1 for output): "))
    pin_config[pin] = direction

    if direction == 1:
        pin_list.append(1)
    elif direction == 0:
        pin_list.append(0)
    else:
        print('wrong input')
        break

pin_list.reverse()
pin_list = map(str, pin_list)
pin_directions = ''.join(pin_list)

function = f'void Init_void (void)\n{{\nDDRA = {pin_directions}\n}}'
print(function)
