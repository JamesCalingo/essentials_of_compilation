from ast import USub, Add, Sub, Constant, UnaryOp, Call, Name, BinOp, Module, Expr

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

def leaf(arith):
    match arith:
        case Constant(n):
            return True
        case Call(Name('input_int'), []):
            return True
        case UnaryOp(USub(), e1):
            return False
        case BinOp(e1, Add(), e2):
            return False
        case BinOp(e1, Sub(), e2):
            return False
        
def is_exp(e):
    match e:
        case Constant(n):
            return True
        case Call(Name('input_int'), []):
            return True
        case UnaryOp(USub(), e1):
            return is_exp(e1)
        case BinOp(e1, Add(), e2):
            return is_exp(e1) and is_exp(e2)
        case BinOp(e1, Sub(), e2):
            return is_exp(e1) and is_exp(e2)
        case _:
            return False
        
def is_stmt(s):
    match s:
        case Expr(Call(Name('print'), [e])):
            return is_exp(e)
        case Expr(e):
            return is_exp(e)
        case _:
            return False
        
def is_Lint(p):
    match p:
        case Module(body):
            return all([is_stmt for s in body])
        case _:
            return False
        
      
        