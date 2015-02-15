def gcd(x,y):
    """GCD of two positive numbers.
    
    Args: x,y: two positive integers.
    Returns the GCD of x and y"""
    if isinstance(x,int)==False:
        if __name__!='__main__':
            print "Argument ",x, " must be an integer"
        return 0
    if isinstance(y,int)==False:
        if __name__!='__main__':
            print "Argument ",y, " must be an integer"
        return 0
    if x<=0:
        print 'First argument ', x, ' is not a positive integer'
        return 0
    if y<=0:
        print 'Second argument is not a positive integer'
        return 0
    while y:
        x,y=y,x%y
    return x
