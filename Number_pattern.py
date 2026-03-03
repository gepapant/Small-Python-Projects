def number_pattern(n):
    
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    number = ""
    
    for i in range(1, n + 1):
        number += str(i)
        if i != n:
            number += " "
    
    return number
