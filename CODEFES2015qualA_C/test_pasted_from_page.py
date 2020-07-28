#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例1(self):
        input = """5 7
1 0
3 0
5 0
2 0
4 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1 1000000000
5 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1 0
100 99"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """3 11
5 2
6 4
7 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """6 92
31 4
15 9
26 5
35 8
97 9
32 3"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
