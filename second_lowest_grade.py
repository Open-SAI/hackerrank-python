if __name__ == '__main__':
    
    regs = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        regs.append([name,score])

    sorted_regs = sorted(regs, key=lambda x: float(x[1]))
    print(sorted_regs)
    
    grade = sorted_regs[0][1]
    print ("grade:", grade)

    x=0
    students = []
    while x <= len(sorted_regs):
       if (sorted_regs[0][1]) == grade:
         del sorted_regs[0]
       x+=1
    print(sorted_regs)
    
    grade = sorted_regs[0][1]
    print ("grade:", grade)

    x=0
    students = []
    while x <= len(sorted_regs):
       if (sorted_regs[0][1]) == grade:
         students.append(sorted_regs[0][0])
       del sorted_regs[0]
       x+=1

    [print(x) for x in sorted(students)]  
