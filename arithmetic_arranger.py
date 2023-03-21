'''''
Answer to: Arithmetic Formatter Challenge
From: freeCodeCamp's Scientific Computing with Python course

Made by: https://github.com/th3worst4
Date: 03.20.2023

Link for the challenge: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
'''''

def arithmetic_arranger(raw, result=False):
    data = list()
    numbers = list()

    if type(raw) == str:
        data.append(raw)
    else:
        data = raw

    if len(data) > 5:
        print("Error: Too many problems.")
        return None
    
    for i in data:                  
        if "+" in i:
            temp = i.split(" + ")
            temp.append("+")
            if len(temp[0])>4 or len(temp[1])>4:
                print("Error: Numbers cannot be more than four digits.")
                return None
            else:
                numbers.append(temp) 
                try:
                    temp.append(str(int(temp[0])+int(temp[1])))
                except ValueError:
                    print("Error: Numbers must only contain digits.")
                    return None
        elif "-" in i:
            temp = i.split(" - ")
            temp.append("-")
            if len(temp[0])>4 or len(temp[1])>4:
                print("Error: Numbers cannot be more than four digits.")
                return None
            else:
                numbers.append(temp)
                try:
                    temp.append(str(int(temp[0])-int(temp[1])))
                except ValueError:
                    print("Error: Numbers must only contain digits.")
                    return None
        else:
            print("Error: Operator must be '+' or '-'.")
            return None

    displayedProblems = len(numbers)
    lim = 3
    arranged_problems = str()
    if result == True:
        lim = 4
    for line in range(lim):    
        printedLine = list()
        for problem in range(displayedProblems):
            if line == 2:
                printedLine.append("-----")
                continue   
            printedLine.append(numbers[problem][line])
            while len(printedLine[problem]) < 5:    
                printedLine[problem] = " " + printedLine[problem]
                if line==1 and len(printedLine[problem])==4:
                    printedLine[problem] = str(numbers[problem][2]) + str(printedLine[problem])
        printedLine = "    ".join(printedLine)
        arranged_problems += printedLine + "\n"

    return(arranged_problems)

