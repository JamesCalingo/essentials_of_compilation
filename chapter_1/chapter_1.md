# 1.1: Abstract Syntax Trees

There's something that's not quite in the book that is important to actually doing this: importing the actual ast module in Python. While the book does mention using the ast module, it never explicitly uses the import ast statement (or, since we have specific things from said module, the statement from ast import ).

My first instinct was to create the Constant class from the book and then create an instance

<\_\_main\__.Constant object at 0x1021d0350>