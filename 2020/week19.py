def get_nth_number(n):
    
    if isinstance(n, int):
        if n <= 0 or n > 9:
            return None
            
        first_digit = n
        second_digit = 10 - n
        return ("{}{}".format(first_digit, second_digit))
    return None
    
# Driver program to test above function 
if __name__=='__main__': 
    
    print (get_nth_number(1))
    print (get_nth_number(2))
    print (get_nth_number("test"))
    print (get_nth_number(12))
    print (get_nth_number(-8))
    print (get_nth_number(9))
    print (get_nth_number(0))
    print (get_nth_number(3))
    print (get_nth_number(4))
    print (get_nth_number(5))
    print (get_nth_number(6))
    print (get_nth_number(7))
    print (get_nth_number(8))