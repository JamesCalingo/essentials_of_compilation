# Chapter 1: Preliminaries

## 1.1: Abstract Syntax Trees

We start by taking a look at Abstract Syntax Trees - or how compilers decide what each part of a program statement is trying to do.

My first instinct was to recreate the Constant class from the book and then create an instance of it to see it in action. When I tried to get a `Constant()` I got this:

```
<__main__.Constant object at 0x1021d0350>
```

And while I should mention that I rather enjoy Python's ability to show you memory addresses (which is almost completely absent in JavaScript), this isn't exactly what I was expecting. In pressing further with the book's examples, I soon realized that in looking at the `ast` library in Python's docs that everything I was doing was already there!

Another fun note: maybe it's because it's been WAY TOO LONG since I defined classes in Python, but the "autocomplete" for `def __init__` ended up adding `-> None` every time I used it. I believe that this is an optional thing in order to improve readability (essentially, it's borrowing the idea of having to define the type of a function's return value from more type safe languages), but in checking it out further, it doesn't seem to affect the program's ability to run if you try to be cheeky with it...