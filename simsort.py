def bubble(Vasya, Masha):
    for k in range(1, len(Vasya)):
        for i in range(len(Vasya)-1):
            if Vasya[i] >= Vasya[i+1]:
                Vasya[i], Vasya[i+1] = Vasya[i+1], Vasya[i]
                Masha[i], Masha[i+1] = Masha[i+1], Masha[i]

Vasya = list(map(int, input().split()))
Masha = list(map(str, input().split()))
bubble(Vasya, Masha)
print(' '.join(Masha))