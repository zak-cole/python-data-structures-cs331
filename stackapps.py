"""Paired Delimiter Matching"""

delim_openers = '{([<'
delim_closers = '})]>'


def check_delimiters(expr):
    """Returns True if and only if `expr` contains only correctly matched delimiters, else returns False."""
    # init variables
    stack = Stack()
    idx = -1

    # iterate through expr
    for char in expr:
        if char in delim_openers:  # check if opener
            stack.push(char)
        elif char in delim_closers:  # check if closer
            try:  # try to get index, if not return False
                idx = delim_openers.index(stack.pop())
            except:
                return False
            if delim_closers.index(char) != idx:  # check if indexes are equal
                return False

    # if stack is empty, delimiters are checked
    return stack.empty()


"""Infix to Postfix Notation"""
# you may find the following precedence dictionary useful
prec = {'*': 2, '/': 2,
        '+': 1, '-': 1}


def infix_to_postfix(expr):
    """Returns the postfix form of the infix expression found in `expr`"""
    ops = Stack()
    postfix = []
    toks = expr.split()

    # iterate through tokens
    for token in toks:
        if str.isdigit(token):  # check if digit
            postfix.append(token)
        elif not bool(ops):
            ops.push(token)
        elif token == '(':  # paranthese logic
            ops.push(token)
        elif token == ')':
            while ops.peek() != '(':
                postfix.append(ops.pop())
            ops.pop()
        else:  # operator logic
            if ops.peek() == '(':
                ops.push(token)
            elif prec[token] > prec[ops.peek()]:
                ops.push(token)
            elif prec[token] == prec[ops.peek()]:
                postfix.append(ops.pop())
                ops.push(token)
            elif prec[token] < prec[ops.peek()]:
                while ops.peek() and prec[token] < prec[ops.peek()]:
                    postfix.append(ops.pop())
                ops.push(token)

    # append remaining pops
    while not ops.empty():
        postfix.append(ops.pop())

    return ' '.join(postfix)


# NOT MY CODE
# Credit to prof. Matthew Bauer
class Stack:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.top = None

    def push(self, val):
        self.top = Stack.Node(val, self.top)

    def pop(self):
        assert self.top, 'Stack is empty'
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.val if self.top else None

    def empty(self):
        return self.top == None

    def __bool__(self):
        return not self.empty()

    def __repr__(self):
        if not self.top:
            return ''
        return '--> ' + ', '.join(str(x) for x in self)

    def __iter__(self):
        n = self.top
        while n:
            yield n.val
            n = n.next
