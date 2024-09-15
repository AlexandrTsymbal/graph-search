import unittest
from unittest.mock import patch

from GraphsLib.GraphsLib import *


class TestGraphAlg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g = Graph()
        cls.g.from_file('matrix.txt')

        cls.g1 = Graph()
        cls.g1.extra_file('matrix.txt', 1, 4)

    @patch('builtins.input', side_effect=[
        '3',
        '0 1 2',
        '1 0 3',
        '2 3 0'
    ])
    def test_from_input(self, mock_input):
        expected_graph = Graph()
        expected_graph.vertices = 3
        expected_graph.add_edge(1, 2, 1)
        expected_graph.add_edge(1, 3, 2)
        expected_graph.add_edge(2, 1, 1)
        expected_graph.add_edge(2, 3, 3)
        expected_graph.add_edge(3, 1, 2)
        expected_graph.add_edge(3, 2, 3)

        g2 = Graph()
        g2.from_input()

        self.assertEqual(g2.get_vertices(), expected_graph.get_vertices())

    def test_right_file_argv(self
                             ):
        self.assertEqual(dij_alg(self.g, 1, 2), 18)
        self.assertEqual(fld_wrsh_alg(self.g, 1, 2), 18)
        self.assertEqual(bell_frd_alg(self.g, 1, 2), 18)
        self.assertEqual(a_star_alg(self.g, 1, 2), 18)
        self.assertEqual(jhn_alg(self.g, 1, 2), 18)

        self.assertEqual(dij_alg(self.g1, 1, 2), 18)
        self.assertEqual(fld_wrsh_alg(self.g1, 1, 2), 18)
        self.assertEqual(bell_frd_alg(self.g1, 1, 2), 18)
        self.assertEqual(a_star_alg(self.g1, 1, 2), 18)
        self.assertEqual(jhn_alg(self.g1, 1, 2), 18)

        self.assertEqual(dij_alg(self.g, 1, 3), 25)
        self.assertEqual(fld_wrsh_alg(self.g, 1, 3), 25)
        self.assertEqual(bell_frd_alg(self.g, 1, 3), 25)
        self.assertEqual(a_star_alg(self.g, 1, 3), 25)
        self.assertEqual(jhn_alg(self.g, 1, 3), 25)

        self.assertEqual(dij_alg(self.g1, 1, 3), 25)
        self.assertEqual(fld_wrsh_alg(self.g1, 1, 3), 25)
        self.assertEqual(bell_frd_alg(self.g1, 1, 3), 25)
        self.assertEqual(a_star_alg(self.g1, 1, 3), 25)
        self.assertEqual(jhn_alg(self.g1, 1, 3), 25)

        self.assertEqual(dij_alg(self.g, 1, 4), 19)
        self.assertEqual(fld_wrsh_alg(self.g, 1, 4), 19)
        self.assertEqual(bell_frd_alg(self.g, 1, 4), 19)
        self.assertEqual(a_star_alg(self.g, 1, 4), 19)
        self.assertEqual(jhn_alg(self.g, 1, 4), 19)

        self.assertEqual(dij_alg(self.g1, 1, 4), 19)
        self.assertEqual(fld_wrsh_alg(self.g1, 1, 4), 19)
        self.assertEqual(bell_frd_alg(self.g1, 1, 4), 19)
        self.assertEqual(a_star_alg(self.g1, 1, 4), 19)
        self.assertEqual(jhn_alg(self.g1, 1, 4), 19)

    def test_graph_moduls(self):
        self.assertEqual(self.g.get_vertices(), list(self.g.graph.keys()))
        self.assertEqual(self.g1.get_vertices(), list(self.g1.graph.keys()))

        self.assertEqual(self.g.get_neighbors(1), self.g.graph.get(1, []))
        self.assertEqual(self.g1.get_neighbors(1), self.g1.graph.get(1, []))

        self.assertEqual(self.g.get_neighbors(2), self.g.graph.get(2, []))
        self.assertEqual(self.g1.get_neighbors(2), self.g1.graph.get(2, []))

        self.assertEqual(self.g.get_neighbors(3), self.g.graph.get(3, []))
        self.assertEqual(self.g1.get_neighbors(3), self.g1.graph.get(3, []))

        self.assertEqual(self.g.get_neighbors(4), self.g.graph.get(4, []))
        self.assertEqual(self.g1.get_neighbors(4), self.g1.graph.get(4, []))

        self.assertEqual(self.g.get_neighbors(5), self.g.graph.get(5, []))
        self.assertEqual(self.g1.get_neighbors(5), self.g1.graph.get(5, []))

        self.assertEqual(self.g.get_neighbors(6), self.g.graph.get(6, []))
        self.assertEqual(self.g1.get_neighbors(6), self.g1.graph.get(6, []))

        self.g2 = Graph()
        self.g2.from_file('matrix.txt')
        self.g2.add_edge(100, 101)
        self.g2.add_edge(200, 201, 10)
        self.g2.add_edge(300, 301, 100)

        self.assertEqual(self.g2.graph[100][0], [101, 1])
        self.assertEqual(self.g2.graph[200][0], [201, 10])
        self.assertEqual(self.g2.graph[300][0], [301, 100])

    def test_false_file_argv(self):
        self.assertIsNone(dij_alg(self.g, 0, 2))
        self.assertIsNone(dij_alg(self.g, 1, 7))
        self.assertIsNone(dij_alg(self.g, -5, 15))
        self.assertIsNone(dij_alg(self.g1, 0, 2))
        self.assertIsNone(dij_alg(self.g1, 1, 7))
        self.assertIsNone(dij_alg(self.g1, -5, 15))

        self.assertIsNone(fld_wrsh_alg(self.g, 0, 2))
        self.assertIsNone(fld_wrsh_alg(self.g, 1, 7))
        self.assertIsNone(fld_wrsh_alg(self.g, -5, 15))
        self.assertIsNone(fld_wrsh_alg(self.g1, 0, 2))
        self.assertIsNone(fld_wrsh_alg(self.g1, 1, 7))
        self.assertIsNone(fld_wrsh_alg(self.g1, -5, 15))

        self.assertIsNone(bell_frd_alg(self.g, 0, 2))
        self.assertIsNone(bell_frd_alg(self.g, 1, 7))
        self.assertIsNone(bell_frd_alg(self.g, -5, 15))
        self.assertIsNone(bell_frd_alg(self.g1, 0, 2))
        self.assertIsNone(bell_frd_alg(self.g1, 1, 7))
        self.assertIsNone(bell_frd_alg(self.g1, -5, 15))

        self.assertIsNone(a_star_alg(self.g, 0, 2))
        self.assertIsNone(a_star_alg(self.g, 1, 7))
        self.assertIsNone(a_star_alg(self.g, -5, 15))
        self.assertIsNone(a_star_alg(self.g1, 0, 2))
        self.assertIsNone(a_star_alg(self.g1, 1, 7))
        self.assertIsNone(a_star_alg(self.g1, -5, 15))

        self.assertIsNone(jhn_alg(self.g, 0, 2))
        self.assertIsNone(jhn_alg(self.g, 1, 7))
        self.assertIsNone(jhn_alg(self.g, -5, 15))
        self.assertIsNone(jhn_alg(self.g1, 0, 2))
        self.assertIsNone(jhn_alg(self.g1, 1, 7))
        self.assertIsNone(jhn_alg(self.g1, -5, 15))

        self.assertEqual(self.g.right_argv(5, 1), True)
        self.assertEqual(self.g.right_argv(-1, 5), False)
        self.assertEqual(self.g1.right_argv(5, 1), True)
        self.assertEqual(self.g1.right_argv(-1, 5), False)


if __name__ == '__main__':
    unittest.main()
