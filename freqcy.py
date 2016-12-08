def get_next():
    get_next.seed = (get_next.seed*513 + 1)%2**18
    if get_next.seed == 0:
        return 0
    else:
        return (get_next.seed**2 + 3*get_next.seed)%999 + 1
get_next.seed = int(input())

quantity = [0 for i in range(1001)]
while True:
    x = get_next()
    if x == 0:
        break
    quantity[x] += 1
A = []
maximum = max(quantity)
for i in range(1, 1001):
    if quantity[i] == maximum:
        A.append(i)
sorted(A)
string = ''
for i in A:
    string += str(i) + ' '
print(string.strip())