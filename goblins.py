def bubble_sort(a):
    x = []
    for i in range(len(a)):
        x.append(0)
    for k in range(1, len(a)):
        for i in range(0, len(a) - k):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                x[i] += 1
                x[i+1] += 1
                x[i], x[i+1] = x[i+1], x[i]
    for i in range(len(a)):
        if a[i] == a[i - 1]:
            a[i - 1] = -1
            x[i] = x[i] + x[i - 1]
    for i in range(len(a)):
        if a[i] != -1:
            print(a[i], end='')
            print(':', end='')
            print(x[i], end=' ')

massive = list(map(int, input().split()))
bubble_sort(massive)