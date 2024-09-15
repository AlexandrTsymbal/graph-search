from random import randint


def create_graph(numb_vert: int) -> list:
    matrix = []

    for i in range(numb_vert):
        matrix.append([])
        for j in range(numb_vert):
            if i == j:
                matrix[i].append(0)
            else:
                matrix[i].append(randint(0, 10))

    with open("matrix6.txt", 'w') as f:
        f.write(f'{numb_vert}\n')
        for row in matrix:
            for el in row:
                f.write(f'{el} ')
            f.write('\n')

    for row in matrix:
        for el in row:
            print(el, end=' ')
        print("\n")

    return matrix


if __name__ == "__main__":
    create_graph(1000)
