from ast import USub

class Constant:
    def __init__(self, value):
        self.value = value

class UnaryOp:
    def __init__(self, op, operand) -> None:
        self.op = op
        self.operand = operand

eight = Constant(8)
print(eight)
neg_eight = UnaryOp(USub(), eight)
print(neg_eight)