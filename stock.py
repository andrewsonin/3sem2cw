def generation(length=5, nils=1, sequence=''):
    if nils == 0:
        print(sequence + '1' * length)
    for i in range(length):
        string = sequence + ('1' * length)[:i] + '0'
        generation(length - i - 1, nils - 1, string)
A = list(map(int, input().split()))
a = A[0]
b = A[1]
generation(a, a - b)