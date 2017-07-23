import unittest


class Stack():
    def __init__(self):
        self.things = []

    def push(self, thing):
        self.things.append(thing)

    def pop(self):
        return self.things.pop()

    def peek(self):
        return self.things[-1]

    def is_empty(self):
        return len(self.things) == 0


def braces(values):
    brace_dict = {'{': '}',
                  '[': ']',
                  '(': ')'}

    open_braces = brace_dict.keys()

    response = []

    for i, line in enumerate(values):
        stack = Stack()
        response.append('YES')
        for char in line:
            if char in open_braces:
                stack.push(char)
            else:
                if brace_dict[stack.peek()] == char:
                    stack.pop()
                else:
                    response[i] = 'NO'
                    break
        if stack.is_empty():
            response[i] = 'YES'
        else:
            response[i] = 'NO'
    return response


class TestBracesFunction(unittest.TestCase):
    def test_balanced(self):
        self.assertEqual(braces(['{}[]()', '{[}]}', '{]}]', '{[()]']), ['YES','NO','NO','NO'])

if __name__ == '__main__':
    unittest.main()
