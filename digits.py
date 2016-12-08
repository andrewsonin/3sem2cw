def notate(base=10, number=0, new_base=10):
    num = bin(int(str(number), base))[2:][-1::-1]
    sum, j = 0, 0
    for i in num:
        sum += int(i) * 2 ** j
        j += 1
    new_number = ''
    while sum > 0:
        residue = sum % new_base
        if residue >= 10:
            new_number += chr(55 + residue)
        else:
            new_number += str(residue)
        sum = sum//new_base
    return str(new_number)[-1::-1]

print(notate(10, input(), 17).count('G'))