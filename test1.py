a = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]

def knotengrad(x):
    for i in x:
        grad = 0
        for j in i:
            if j == 1:
                grad += 1
        print(grad)


knotengrad(b)
