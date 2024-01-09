# Chapter 1: Preliminaries

First of all, we should discuss what's actually going on with a compiler by discussing concrete and abstract syntax.

Take, for example, this MarkDown file you're currently looking at. 

## 1.1: Abstract Syntax Trees

We start by taking a look at Abstract Syntax Trees - or how compilers decide what each part of a program statement is trying to do.

My first instinct was to recreate the Constant class from the book and then create an instance of it to see it in action. When I tried to get a `Constant()` I got this:

```
<__main__.Constant object at 0x1021d0350>
```

And while I should mention that I rather enjoy Python's ability to show you memory addresses (which is almost completely absent in JavaScript), this isn't exactly what I was expecting. In pressing further with the book's examples, I soon realized that in looking at the `ast` library in Python's docs that everything I was doing was already there!

Another fun note: maybe it's because it's been WAY TOO LONG since I defined classes in Python, but the "autocomplete" for `def __init__` ended up adding `-> None` every time I used it. I believe that this is an optional thing in order to improve readability (essentially, it's borrowing the idea of having to define the type of a function's return value from more type safe languages), but in checking it out further, it doesn't seem to affect the program's ability to run if you try to be cheeky with it...

## 1.2: Grammars

This section seems to be more of a theoretical chapter rather than a practical one, but it's still important to understand the theory behind what's going on when compiling a program. However, I'll be honest: I'm not *entirely* sure what's going on here.

...Or at least I wasn't on my first read through. This leads me to some more general advice I think would be helpful to those trying to do something similar to this:

Don't be afraid to wait.

I think with how employers are asking for these wide skillsets nowadays, people are insanely tempted to move on from one topic to the next as quickly as possible to get those "skills" onto their resume, but the reality is that this can lead to not actually knowing said skill - something that can come out in interviews. If you're trying to truly understand a concept, then spending time with it until you're ready to move on will help you make sure that you have a good understanding of the concept and can use it to build up to other, more challenging topics.

Anyway, back to THIS book, the basic rules are laid out using a "smaller language" called L<sub>int</sub>. While going over every single rule here might be a bit pedantic, I think going over the "gist" of the ruleset may help: It divides everything we've declared so far into *expressions* and *statements*. Most of what we have from the last module are in the *expressions* category: constants, our operators, and an empty function call are expressions, while printing things, as well as stating a variable itself, are statements.

In addition, we add a `Module` class to tie everything together.

## 1.3: Pattern Matching

We start by introduing something rather new: Python's `match` keyword. It was added in Python 3.10 back in 2021, and is, in essence, a Python version of the `switch` statement found in other languages like JavaScript (i.e. a way ot grouping if/elif statements).

As an example of this, the book takes all of the classes we've been using so far and determines whether or not they are leaf nodes of an AST (i.e. is there more logic below ). In our case, the Constant and Call classes are leaves, but the unary and binary operators are not as there is other logic we need to figure out before we hit the leaf nodes.

(Coincidentally, I tried writing this out and got an error that immplied that I wasn't using Python 3.10 or newer; I checked my version and it was 3.11 and the code ran fine)

## 1.4: Recursive Functions

For those who don't know (although you) really should, recursion is when a function calls itself when running. While it may seem like it's only useful in the world of data structures and algorithms, I have used recursion for front end work in the past.

Here, we check if we have valid logic in our program by making sure that our expressions are written with valid inputs (i.e. the Constant and input_int expressions).

This section also features a powerful Python feature that doesn't have a clear analog in other languages: list comprehension! List comprehension is basically a form of a forEach() loop from other languages where you take a list (or array if you're in something like JavaScript) and run a function on it. It's useful for writing "cleaner" code, and I'm unaware of any other languages that have anything similar to it (I could've used it for some React stuff early in my career...).

## 1.5: Interpreters

We start discussing the idea of interpreters in this section.

Again, let's look at the language this file is written in: MarkDown. GitHub has a feature that interprets certain MarkDown features and translates them to look "different" upon presentation (i.e. it essentially HTML's the raw data). For example, assuming you're not looking at the raw data, then typing \*hi!\* will end up looking like *hi!* due to how MarkDown interprets stuff surrounded by the * character (or _).

Something I didn't realize until I got to this section: We have the standard `print()` function available to us, but we also have another function called `input_int()`. These are the only two functions available to us that aren't in Python's `ast` module (except for a few others). However, this section introduced a group of functions that are also not part of Python's standard library; they're available in the book's support code, but the file that contains them has utils for EVERYTHING in the book. For now, I'm only copying the ones that are pertinent to this chapter: `add64()`, `sub64()`, `neg64()`, and `input_int()`, along with some other things that they require.

## 1.6 Example Compiler: A Partial Evaluator

Finally, we get into partial evaluation. The book uses the idea of computing 5 + 3 vs just putting in 8 to explain how the compiler translates programs: since we have to do something with 5 + 3, an AST is created for it.