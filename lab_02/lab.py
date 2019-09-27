def absolute_value(n):
    if n<0:
        return n*-1
    else:
        return n
   
    '''
    this function returns the absolute value of n

        >>> absolute_value(5)
        5
        >>> absolute_value(-5)
        5
        >>> absolute_value(5.5)
        5.5
        >>> absolute_value(-5.5)
        5.5
    '''
    

def hypotenuse(a,b):
    return ((a*a)+(b*b))**(1/2)
    '''
    returns c = square root of a squared plus b squared

        >>> hypotenuse(3.0,4.0)
        5.0
        >>> hypotenuse(12.0,5.0)
        13.0
    '''
    

def is_even(n):
    if n%2==0:
        return True
    else:
        return False
    '''
    this function returns True if n is even and False if n is odd

        >>> is_even(0)
        True
        >>> is_even(1)
        False
        >>> is_even(2000)
        True
        >>> is_even(-8)
        True
        >>> is_even(-9)
        False
    '''


def max_num(a,b):
    if a>b:
        return a
    else:
        return b
    
    '''
    this function returns the maximum of a and b

        >>> max_num(4,5)
        5
        >>> max_num(5,4)
        5
        >>> max_num(-4,-5)
        -4
        >>> max_num(4,4)
        4
    '''
    

def max_num_abs(a,b):
    ab=a
    ba=b
    if a<0:
        ab=a*-1
    if b<0:
        ba=b*-1
    if ab>ba:
        return a
    else:
        return b
    
    
    
    '''
    this function returns the number with the highest absolute value

        >>> max_num_abs(4,5)
        5
        >>> max_num_abs(4,5)
        5
        >>> max_num_abs(-4,-5)
        -5
        >>> max_num_abs(4,4)
        4
    '''
    

def max_num_4(a,b,c,d):
    '''
    this function returns the maximum of a, b, c, and d

        >>> max_num_4(1,2,3,4)
        4
        >>> max_num_4(2,3,4,1)
        4
        >>> max_num_4(3,4,1,2)
        4
        >>> max_num_4(4,1,2,3)
        4
        >>> max_num_4(10,1,2,3)
        10
    '''
    

def num_digits(n):
    if n<0:
        n=n*-1
    return len(str(n))
  
    
   
    
    '''
    Returns the number of digits in the input n.
    Note that a negative sign does not count as a digit,
    only numbers do.

        >>> num_digits(5)
        1
        >>> num_digits(10)
        2
        >>> num_digits(45678)
        5
        >>> num_digits(123456789012345678901234567890)
        30
        >>> num_digits(-5)
        1
        >>> num_digits(-10)
        2

    HINT: convert the number into a string and use the length of the string
    '''


def is_leap_year(n):
    if n>=1582 and n%4==0 and (n%400==0 or n%100!=0):
        return True
    else:
        return False
        
    
    '''
    Returns True if n is a leap year and False otherwise.

    HINT: You can find the formula to calculate leap years here at 
    https://www.mathsisfun.com/leap-years.html

        >>> is_leap_year(1582)
        False
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(2018)
        False
        >>> is_leap_year(2019)
        False
        >>> is_leap_year(2020)
        True
        >>> is_leap_year(2200)
        False
        >>> is_leap_year(2400)
        True
    '''
    

# DO NOT MODIFY BELOW THIS LINE
import doctest
doctest.testmod(verbose=True)


