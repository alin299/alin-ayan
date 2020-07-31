for i in range(1, 10):

    for j in range(1, i+1):

        print("{}*{}={:2}".format(j, i, i*j), end=' ')

    print('')

for i in range(1, 1000):
    a = i // 100
    b = (i - a * 100) // 10
    c = i % 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)


