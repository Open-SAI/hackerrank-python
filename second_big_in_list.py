if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    n_input = list(arr)[0:n]
#    not_duplicates = list(dict.fromkeys(n_input))
    not_duplicates = []
    [not_duplicates.append(x) for x in n_input if x not in not_duplicates]
    arr_sort = sorted(not_duplicates, reverse=True)

    print(n,arr_sort,arr_sort[1])
    
