def swap_case(s):
    swapped_s=[]
    if len(s) <= 1000:        
        for c in s:
            if c.isupper():
                swapped_s.append(c.lower())
            else:
                swapped_s.append(c.upper())
    return swapped_s

if __name__ == '__main__':
    s = input()
    print(''.join(swap_case(s)))
