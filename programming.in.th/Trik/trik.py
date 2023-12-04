trik = [1, 0, 0]
sequence = input()
for code in sequence:
    if code == 'A':
        trik[0], trik[1] = trik[1], trik[0]
        
    elif code == 'B':
        trik[1], trik[2] = trik[2], trik[1]
        
    elif code == 'C':
        trik[2], trik[0] = trik[0], trik[2]

print('1' if trik[0] == 1 else '2' if trik[1] == 1 else '3')

