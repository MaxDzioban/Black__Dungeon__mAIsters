import unittest
from polynumial import Mono, Polynomial

class TestMono(unittest.TestCase):
    def setUp(self):
        self.mono = Mono(2, 3)

    def test_mono_str(self):
        self.assertEqual(str(self.mono), "Mono: 2x**3")

    def test_mono_repr(self):
        self.assertEqual(repr(self.mono), "Mono(coeff=2, degree=3)")

    def test_mono_eq(self):
        mono2 = Mono(2, 3)
        self.assertEqual(self.mono, mono2)

class TestPolynomial(unittest.TestCase):
    def setUp(self):
        mono1 = Mono(2, 3)
        mono2 = Mono(1, 2)
        self.poly = Polynomial(mono1, mono2)

    def test_polynomial_str(self):
        self.assertEqual(str(self.poly), "Polynomial: 2x**3+x")

    def test_polynomial_repr(self):
        self.assertEqual(repr(self.poly), "Polynomial(Mono(coeff=2, degree=3) -> Mono(coeff=1, degree=2))")

    def test_polynomial_degree(self):
        self.assertEqual(self.poly.degree, 3)

    def test_polynomial_copy(self):
        poly2 = self.poly.copy()
        self.assertEqual(self.poly, poly2)

    def test_polynomial_sort(self):
        mono3 = Mono(3, 1)
        self.poly = Polynomial(self.poly, mono3)
        self.poly.sort()
        self.assertEqual(str(self.poly), "Polynomial: 2x**3+x**2+3x")

    def test_polynomial_simplify(self):
        mono2 = Mono(-2, 3)
        mono3 = Mono(1, 2)
        self.poly = Polynomial(self.poly, mono2, mono3)
        self.poly.simplify()
        self.assertEqual(str(self.poly), "Polynomial: x**2")

    def test_polynomial_eval_at(self):
        result = self.poly.eval_at(2)
        self.assertEqual(result, 20)

    def test_polynomial_eq(self):
        poly2 = Polynomial(self.poly)
        self.assertEqual(self.poly, poly2)

    def test_polynomial_hash(self):
        result = hash(self.poly)
        self.assertIsInstance(result, int)

    def test_polynomial_add(self):
        poly2 = Polynomial(self.poly)
        result = self.poly + poly2
        self.assertEqual(str(result), "Polynomial: 4x**3+2x**2")

    def test_polynomial_sub(self):
        poly2 = Polynomial(self.poly)
        result = self.poly - poly2
        self.assertEqual(str(result), "Polynomial: 0")

    def test_polynomial_mul(self):
        poly2 = Polynomial(self.poly)
        result = self.poly * poly2
        expected_result = Polynomial(Mono(4, 5), Mono(4, 4), Mono(4, 3))
        self.assertEqual(str(result), "Polynomial: 4x**5+4x**4+4x**3")

if __name__ == '__main__':
    unittest.main()
