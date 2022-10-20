def fib_pos(n) :
    if (n <= 1) :
        return n
  
    a = 0
    b = 1
    c = 1
    pos = 1
    while (c < n) :
        c = a + b  
        pos = pos + 1
        a = b
        b = c       
    return pos

result = fib_pos(1)
print(result)