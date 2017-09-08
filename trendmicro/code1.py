import unittest


class TestMethods(unittest.TestCase):

    def test1(self):
        S = 'John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker'
        C = 'example'
        A = 'doe_john@example.com; parker_peter_b@example.com; watsonparker_mary_j@example.com; doe_john_e@example.com; doe_john_e2@example.com; doe_jane@example.com; parker_peter_b2@example.com'
        self.assertEqual(solution(S, C), A)


def solution(S, C):
    # Seperate name list
    Names = [name.strip() for name in S.lower().split('; ')]
    C = C.lower()

    # print(Names)

    # Generate emails
    Emails = []
    Exists = {}
    for n in Names:
        List = n.split(' ')
        email = ''
        if len(List) == 3:
            first, middle, last = List[0], List[1], List[2]
            last = last.replace('-', '')
            email = '_'.join([last, first, middle[0]])
        elif len(List) == 2:
            first, middle, last = List[0], '', List[1]
            last = last.replace('-', '')
            email = '_'.join([last, first])

        # join the email
        if email in Exists:
            Exists[email] = Exists[email] + 1
            email = email + str(Exists[email]) + '@' + C + '.com'
        else:
            Exists[email] = 1
            email = email + '@' + C + '.com'
        Emails.append(email)

    # print(Emails)
    return '; '.join(Emails)


if __name__ == '__main__':
    unittest.main()
