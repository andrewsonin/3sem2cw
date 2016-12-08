def generation(length=0, nils=0, sequence=''):
    if nils == 0:
        print(sequence + '1' * length)
    for i in range(length):
        string = sequence + ('1' * length)[:i] + '0'
        generation(length - i - 1, nils - 1, string)
A = list(map(int, input().split()))
a, b = A[0], A[1]
generation(a, a - b)