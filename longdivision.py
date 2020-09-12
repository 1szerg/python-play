def extractfirst(problem, symbol):
    aStr = problem[0:problem.find(symbol)]
    return int(aStr)


def extractsecond(problem, symbol):
    aStr = problem[problem.find(symbol)+1:]
    return int(aStr)


def divideit(a, b):
    solution = ["Division "+str(a) +" / "+ str(b)+" is:"]
    astr = str(a)
    result = "0"
    c = ""
    for i in range(0, len(astr)):
        c = c+astr[i]
        result = result + str(int(int(c)/b))
        solution.append("     "[0:4-len(c)]+c+" / "+str(b)+" = "+str(int(int(c)/b))+" r"+str(int(c) % b))
        c = str(int(c) % b)
    solution.append(" result "+str(int(result))+" r"+c)
    solution.append(" verify "+str(int(a/b))+" r"+str(int(a % b)))
    return solution


def multiplyit(a, b):
    return ["multiplyit", "not", "implemented", str(a), str(b)]


def addit(a, b):
    return ["addit", "not", "implemented", str(a), str(b)]


def substractit(a, b):
    return ["substractit", "not", "implemented", str(a), str(b)]


problemStr = input("Tell me your problem (like '222/6') > ")
if problemStr.find("/") > 0:
    a = extractfirst(problemStr, "/")
    b = extractsecond(problemStr, "/")
    solution = divideit(a, b)
for line in solution:
    print(line)