def add (n1, n2):    
    return n1 + n2


def sub (n1, n2):    
    return n1 - n2


def mul (n1, n2):    
    return n1 * n2

 
def div (n1, n2):    
    if n2 == 0:
        raise ValueError("Cannot divide by zero")
    return n1 / n2

