import unittest


class TestMethods(unittest.TestCase):

    def test1(self):
        A = [60, 80, 40]
        B = [2, 3, 5]
        self.assertEqual(solution(A, B, 5, 2, 200), 5)

    def test2(self):
        A = [40, 40, 100, 80, 20]
        B = [3, 3, 2, 2, 3]
        self.assertEqual(solution(A, B, 3, 5, 200), 6)


def solution(A, B, M, X, Y):
    # write your code in Python 2.7
    times = 0

    # just exception check
    if len(A) != len(B):
        return 0

    while A:
        capacity = X
        loading = Y
        Stops = []
        while A:
            weight, target = A[0], B[0]
            if (loading - weight) < 0 or capacity == 0:
                break
            else:
                # take 1 man to target floor
                loading -= A.pop(0)
                capacity -= 1
                B.pop(0)
                if target not in Stops:
                    times += 1
                    Stops.append(target)

        # back to ground floor
        times += 1

    return times

if __name__ == '__main__':
    unittest.main()
