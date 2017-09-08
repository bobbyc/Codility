
def solution(A):
    # find positive
    Positives = [i for i in A if i > 0]
    Positives.sort()

    if len(Positives) == 0:
        return 1

    # find smallest positive
    n = 0
    nMin = min(Positives)
    nMax = max(Positives)
    if nMax > 100000:
        nMax = 100000

    # do find
    # TODO: optimization
    for n in range(1, nMax + 1):
        if n not in Positives:
            break

    if n == nMax:
        n = nMax + 1

    return n


def main():
    try:
        #A = [1, 3, 6, -1000, 4, 1, 2]
        A = [100000]
        #A = [-1, -3]
        n = solution(A)
        print(n)
    except Exception as e:
        exit(1)


if __name__ == '__main__':
    main()
