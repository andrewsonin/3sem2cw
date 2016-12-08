def push(A, data):
    p = A
    A = [data, p]


class LinkedList:
    def __init__(self):
        self._begin = None

    def push_front(self, data):
        p = self._begin
        self._begin = [data, p]

    def pop_front(self):
        if not self._begin:
            raise IndexError
        data = self._begin[0]
        self._begin = self._begin[1]
        return data

    def empty(self):
        return not self._begin


class SmileChecker:
    def __init__(self):
        self.sequence = []

    def check_correct(self):
        left, right = [':-(', ':-[', ':-{', ':-<'], [':-)', ':-]', ':-}', ':->']
        pair, stack = dict(zip(left, right)), LinkedList()
        for brace in self.sequence:
            if brace in left:
                stack.push_front(brace)
            elif brace in right:
                if stack.empty():
                    return False
                if pair[stack.pop_front()] != brace:
                    return False
        return stack.empty()

    def append_smile(self, obj):
        self.sequence.append(obj)