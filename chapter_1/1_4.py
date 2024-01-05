from ast import USub, Add, Sub, Constant, UnaryOp, Call, Name, BinOp, Module, Expr
   
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
        
      
        