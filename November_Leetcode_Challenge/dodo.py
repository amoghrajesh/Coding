def ans(n, instances, price):
    m = len(instances)
    if m == 1:
        return price[0]
    
    for i in range(m):
        if instances[i] == n:
            return price[i]
    
    inst = []
    pri = []
    for i in range(m):
        if price[i] > 0:
            inst.append(instances[i])
            pri.append(price[i])

    m = len(pri)

    if n < instances[0]:
        x1, y1 = instances[0], price[0]
        x2, y2 = instances[1], price[1]

    elif n > instances[-1]:
        x1, y1 = instances[-1], price[-1]
        x2, y2 = instances[-2], price[-2]
    
    else:
        for i in range(m - 1):
            if n > instances[i] and n < instances[i+1]:
                p, q = i, i + 1
                break

        x1, y1 = instances[p], price[p]
        x2, y2 = instances[q], price[q]

    m = (y2 - y1)/(x2 - x1)
    y = m * (n - x1) + y1
    return y

print(ans(10, [25, 50, 100], [5.0, 4.0, 3.0]))

