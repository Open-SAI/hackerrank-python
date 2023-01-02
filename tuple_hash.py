if __name__ == '__main__':

    '''
    # if 'n' is bigger than size(integer_list), will have a index out of range
    n = int(input())
    # default split character is space ' '
    integer_list = input().split()
    # itertools: [operation over i for i in set ]
    elements = [integer_list[i] for i in range(0,n)]    
    print (elements)
    # ERROR: every hash(t) are differents with the same input !!
    print (hash(tuple(elements)))
    '''
    n = int(input())
    elements = map(int, input().split())
    print(elements)
    print(hash(tuple(elements)))   
