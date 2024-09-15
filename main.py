from GraphsLib.GraphsLib import *

if __name__ == "__main__":
    g1 = Graph()
    g2 = Graph()
    g3 = Graph()

    g1.from_input()
    g2.extra_file('matrix4.txt', 1, 4)
    g3.from_file('matrix4.txt')

    print('Граф построенный с оптимизацией')
    print(g2)
    print('Граф построенный без оптимизации')
    print(g3)

    print("Алгоритм Дейкстра")
    print(dij_alg(g1, 1, 2))
    print(dij_alg(g2, 1, 2))
    print(dij_alg(g3, 1, 2))

    print("Алгоритм Беллмана-Форда")
    print(bell_frd_alg(g1, 1, 3))
    print(bell_frd_alg(g2, 1, 3))
    print(bell_frd_alg(g3, 1, 3))

    print("Алгоритм Флойда-Уоршелла")
    print(fld_wrsh_alg(g1, 1, 4))
    print(fld_wrsh_alg(g2, 1, 4))
    print(fld_wrsh_alg(g3, 1, 4))

    print("Алгоритм A*")
    print(a_star_alg(g1, 1, 5))
    print(a_star_alg(g2, 1, 5))
    print(a_star_alg(g3, 1, 5))

    print("Алгоритм Джонсона")
    print(jhn_alg(g1, 1, 6))
    print(jhn_alg(g2, 1, 6))
    print(jhn_alg(g3, 1, 6))
