from os import system

def CheckSpaces(expression):
    i = 0
    if " " in expression:
        while i <= len(expression) and " " in expression:
            if expression[i] == " ":
                expression = expression[:i] + expression[(i + 1):]
                i = 0
            else: i += 1
        return expression
    else: return expression

def FindElements(expression):
    elements = []
    element = ""
    i = 0
    if "+" or "-" or "/" or "*" in expression:
        while i < len(expression):
            if expression[i] != "+" and expression[i] != "-" and expression[i] != "*" and expression[i] != "/":
                element += expression[i]
                i += 1
                continue
            else:
                elements.append(element)
                element = ""
                element += expression[i]
                elements.append(element)
                i += 1
                element = ""
        elements.append(element)
    i = 0
    if "" in elements:
        while "" in elements:
            if elements[i] == "" and elements[i + 1] == "-":
                elements[i + 2] = str((-1)*float(elements[i + 2]))
                elements.pop(i + 1)
                elements.pop(i)
            i += 1
    return elements

def FindBrackets(expression):
    startBracket = None
    endBracket = None
    newExpression = ""
    if "(" and ")" in expression:
        for i in range(len(expression)):
            if expression[i] == "(": startBracket = i
            if expression[i] == ")":
                endBracket = i
                break
        for i in range(startBracket + 1, endBracket):
            newExpression = newExpression + expression[i]
        expression = newExpression
    return expression, startBracket, endBracket 

def Calculation(elements):
    i = 0
    while "*" in elements or "/" in elements:
        if elements[i] == "*":
            elements[i] = str(float(elements[i - 1]) * float(elements[i + 1]))
            elements.pop(i + 1)
            elements.pop(i - 1)
        elif elements[i] == "/":
            elements[i] = str(float(elements[i - 1]) / float(elements[i + 1]))
            elements.pop(i + 1)
            elements.pop(i - 1)
        else: i += 1
    i = 0
    while "+" in elements or "-" in elements:
        if elements[i] == "+":
            elements[i] = str(float(elements[i - 1]) + float(elements[i + 1]))
            elements.pop(i + 1)
            elements.pop(i - 1)
        elif elements[i] == "-":
            elements[i] = str(float(elements[i - 1]) - float(elements[i + 1]))
            elements.pop(i + 1)
            elements.pop(i - 1)
        else: i += 1
    return elements[0]

system('clear')
while True:
    try:
        expressionStart = input("Напишите выражение без знака равно со скобками или без:\n")
        expression = CheckSpaces(expressionStart)
        result = 0
        if FindBrackets(expression)[1] == None: result = Calculation(FindElements(FindBrackets(expression)[0]))
        else:
            while "(" in expression and ")" in expression:
                IMexpression = FindElements(FindBrackets(expression)[0])
                result = Calculation(IMexpression)
                expression = expression[:FindBrackets(expression)[1]] + result + expression[(FindBrackets(expression)[2] + 1):]
        out = Calculation(FindElements(expression))
        roundNumber = round(float(out), 2)
        if roundNumber % 1 * 100 == 0:
            print(f"{expressionStart} = {int(roundNumber)}")
        else: print(f"{expressionStart} = {roundNumber}")
        print(f"Для проверки функцией EVAL: {eval(expressionStart)}")
        break
    except: print("Похоже, что-то в Вашем выражении неправильно...\nПожалуйста, поищите ошибку.\n")