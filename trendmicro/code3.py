import unittest


class TestMethods(unittest.TestCase):

    def test1(self):
        self.assertTrue(solution('A2Le', '2pL1'))

    def test2(self):
        self.assertTrue(solution('a100', '100a'))

    def test3(self):
        self.assertFalse(solution('ba1', '1Ad'))

    def test4(self):
        self.assertFalse(solution('a100', '200a'))


def solution(S, T):
    # filter all numbers in string
    import re
    numberS = re.findall('\d+', S)
    numberT = re.findall('\d+', T)

    # replace number to marker '?'
    for n in numberS:
        S = S.replace(n, '?' * int(n))
    for n in numberT:
        T = T.replace(n, '?' * int(n))

    # check same length?
    if len(S) != len(T):
        return False

    for i in range(len(S)):
        if S[i] == '?' or T[i] == '?':
            continue
        elif S[i] != T[i]:
            return False

    # replace number as marker
    return True


if __name__ == '__main__':
    unittest.main()
