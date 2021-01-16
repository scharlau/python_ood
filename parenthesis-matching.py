# a parenthesis matching algorithm
from arraystack import ArrayStack
def is_matched(expr):
    """Return True if all delimiters are properly matched"""
    
    lefty ='({['                    # opening delimiters
    righty = ')}]'                  # closing delimiters
    s = ArrayStack()
    for c in expr:
        if c in lefty:
            s.push(c)               # push delimiter onto the stack
        elif c in righty:
            if s.is_empty():
                return False        # nothing to match with
            if righty.index(c) != lefty.index(s.pop()):
                return False        # mismatched
    return s.is_empty()             # were all symbols matched?

# sample usage
matched = is_matched('[{{))}}]')
print(matched)
                