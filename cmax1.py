def get_next():
    get_next.seed = (get_next.seed * 513 + 1) % 2**18
    if get_next.seed == 0:
        return 0
    else:
        return get_next.seed**2 % 100000 + 1
get_next.seed = int(input())
locations = []
counter = -1
i = float('-inf')
while True:
    x = get_next()
    if x == 0:
        break
    counter += 1
    if x > i:
        i = x
        locations = [str(counter)]
    elif x == i:
        locations.append(str(counter))
print(' '.join(locations))