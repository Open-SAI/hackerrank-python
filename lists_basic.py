if __name__ == '__main__':
    N = int(input())
    commands = []
    numbers = []

    for i in range(0,N):
        #print ("Comando: ",i)
        commands.append(input())
    
    print ("Commands list:")
    print (*commands, sep = ", ")

    for i in range(len(commands)):
        if   (commands[i].split(' ')[0] == "insert"):
            print ("insert", commands[i].split(' ')[2], "en pos", commands[i].split(' ')[1])
            numbers.insert(int(commands[i].split(' ')[1]),int(commands[i].split(' ')[2]))
            print(*numbers)
        elif (commands[i].split(' ')[0] == "print"):
            print ("print ")
            print (numbers)
        elif (commands[i].split(' ')[0] == "remove"):
            print ("remove ", commands[i].split(' ')[1])
            numbers.remove(int(commands[i].split(' ')[1]))
        elif (commands[i].split(' ')[0] == "append"):
            print ("append ", commands[i].split(' ')[1])
            numbers.append(int(commands[i].split(' ')[1]))
        elif (commands[i].split(' ')[0] == "sort"):
            print ("sort ")
            numbers.sort()
        elif (commands[i].split(' ')[0] == "pop"):
            print ("pop ")
            numbers.pop()
        elif (commands[i].split(' ')[0] == "reverse"):
            print ("reverse ")
            numbers.reverse()

