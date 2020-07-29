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
        input = """1 1 1"""
        output = """28.2743338823"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 1 1"""
        output = """75.3982236862"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """16 2 27"""
        output = """6107.2561185786"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
