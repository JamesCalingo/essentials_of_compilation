from ast import USub, Add, Constant, UnaryOp, Call, Name, BinOp

# class Constant:
#     def __init__(self, value):
#         self.value = value

# class UnaryOp:
#     def __init__(self, op, operand):
#         self.op = op
#         self.operand = operand

# class Call:
#     def __init__(self, func, args):
#         self.func = func
#         self.args = args

# class Name:
#     def __init__(self, id):
#         self.id= id

# class BinOp:
#     def __init__(self, left, op, right):
#         self.op = op
#         self.left = left
#         self.right = right

read = Call(Name('input_int'), [])
print(read)

eight = Constant(8)
print(eight)
neg_eight = UnaryOp(USub(), eight)
print(neg_eight)

sst1_1 = BinOp(read, Add(), neg_eight)
print(sst1_1)