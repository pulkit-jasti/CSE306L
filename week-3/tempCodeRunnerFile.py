def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack[:-1]


stack = create_stack()
symboltable = []

identifier = ("variable", "function", "structure", "pointer", "array")

while (True):
    ch = input("Enter identifiers into the symbol table (Y or N) : ")
    if (ch == "Y"):
        for i in range(len(identifier)):
            print(str(i+1), identifier[i])
        choice = int(input("Enter your choice : "))

        if (choice == 1):
            varname = input("Enter the name of the variable : ")
            flag = False
            for i in symboltable:
                if (i[0] == varname):
                    flag = True
                    break
            if (flag == False):
                push(stack, "variable")
                push(stack, varname)
                vardtype = input("Enter the datatype of the variable : ")
                push(stack, vardtype)
                varscope = input("Enter the scope of the variable (global, inside function, inside class): ")
                push(stack, varscope)
                varid = id(varname)
                push(stack, varid)
                print("Information of " + varname + " in the symbol table : ")
                print(str(stack))
                symboltable.append(stack)
                stack = []
            else:
                print("The variable already exits in the symbol table")

        if (choice == 2):
            ls = []
            funname = input("Enter the name of the function : ")
            flag = False
            for i in symboltable:
                if (i[0] == funname):
                    flag = True
                    break
            if (flag == False):
                push(stack, "function")
                push(stack, funname)
                funreturn = input("Enter the return type of the function : ")
                push(stack, funreturn)
                funpara = int(input("Enter the number of parameters : "))
                push(stack, funpara)
                print("Enter the name and datatype of the parameters : ")
                for i in range(funpara):
                    ls.append(list(map(str, input().split())))
                push(stack, ls)
                funpara1 = input("Enter the parameter passing methods (passing by value, passing by reference) : ")
                push(stack, funpara1)
                funid = id(funname)
                push(stack, funid)
                print("Information of " + funname + " in the symbol table : ")
                print(str(stack))
                symboltable.append(stack)
                stack = []
            else:
                print("The function identifier already exists in the symbol table")
        
        if (choice == 3):
            ls = []
            structname = input("Enter the name of the structure : ")
            flag = False
            for i in symboltable:
                if (i[0] == structname):
                    flag = True
                    break
            if (flag == False):
                push(stack, "structure")
                push(stack, structname)
                structmem = int(input("Enter the number of members of the structure : "))
                push(stack, structmem)
                print("Enter the name and datatype of the members : ")
                for i in range(structmem):
                    ls.append(list(map(str, input().split())))
                push(stack, ls)
                structid = id(structname)
                push(stack, structid)
                print("Information of " + structname + " in the symbol table : ")
                print(str(stack))
                symboltable.append(stack)
                stack = []
            else:
                print("The structure identifier already exists in the symbol table")
        
        if (choice == 4):
            ptrname = input("Enter the name of the pointer : ")
            flag = False
            for i in symboltable:
                if (i[0] == ptrname):
                    flag = True
                    break
            if (flag == False):
                push(stack, "pointer")
                push(stack, ptrname)
                ptrtype = input("Enter the data type type of the pointer : ")
                push(stack, ptrtype)
                ptrpoint = input("Enter the name of the variable whose address the pointer is holding  : ")
                push(stack, ptrpoint)
                ptrvalue = id(ptrpoint)
                push(stack, ptrvalue)
                ptrid = id(ptrname)
                push(stack, ptrid)
                print("Information of " + ptrname + " in the symbol table : ")
                print(str(stack))
                symboltable.append(stack)
                stack = []
            else:
                print("The pointer identifier already exists in the symbol table")
        
        if (choice == 5):
            ls = []
            arrname = input("Enter the name of the array : ")
            flag = False
            for i in symboltable:
                if (i[0] == arrname):
                    flag = True
                    break
            if (flag == False):
                push(stack, "array")
                push(stack, arrname)
                arrtype = input("Enter the data type of the array : ")
                push(stack, arrtype)
                arrdim = int(input("Enter the number of dimensions of the array : "))
                push(stack, arrdim)
                print("Enter the value of the dimensions: ")
                for i in range(arrdim):
                    ls.append(input())
                push(stack, tuple(ls))
                arrid = id(arrname)
                push(stack, arrid)
                print("Information of " + arrname + " in the symbol table : ")
                print(str(stack))
                symboltable.append(stack)
                stack = []
            else:
                print("The array identifier already exists in the symbo table")
    else:
        break
print("\n"*2)
print("Symbol Table")
print("\n")
print("\tVariables")
print("\n")
print("name\tdatatype\tscope\t\taddress")
for i in symboltable:
    if (i[0] == 'variable'):
        print(str(varname)+"\t"+str(vardtype)+"\t\t"+str(varscope)+"\t\t"+str(varid))
else:
    print("---------------------None---------------------")
print("\n")
print("\tPointers")
print("\n")
print("name\tdatatype\tidentifier holding\t\tvalue\t\t\taddress")
for i in symboltable:
    if (i[0] == 'pointer'):
        print(str(ptrname)+"\t"+str(ptrtype)+"\t\t\t"+str(ptrpoint)+"\t\t\t"+str(ptrvalue)+"\t\t\t"+str(ptrid))
else:
    print("---------------------None---------------------")
print("\n")
print("\tFunctions")
print("\n")
print("name\treturntype\tno. of para\t(name,datatype)\t\t\tpassing method\t\t\taddress")
for i in symboltable:
    if (i[0] == 'function'):
        print(str(funname)+"\t"+str(funreturn)+"\t\t"+str(funpara)+"\t\t"+str(i[4])+"\t\t"+str(funpara1)+"\t\t\t"+str(funid))
else:
    print("---------------------None---------------------")
print("\n")
print("\tStructures")
print("\n")
print("name\tmembers\t(name,datatype)\t\t\t\taddress")
for i in symboltable:
    if (i[0] == 'structure'):
        print(str(structname)+"\t"+str(structmem)+"\t"+str(i[3])+"\t"+str(structid))
else:
    print("---------------------None---------------------")
print("\n")
print("\tArrays")
print("\n")
print("name\tdatatype\tdim\tdimvalue\taddress")
for i in symboltable:
    if (i[0] == 'array'):
        print(str(arrname)+"\t"+str(arrtype)+"\t\t"+str(arrdim)+"\t\t"+str(i[4])+"\t\t"+str(arrid))
else:
    print("---------------------None---------------------")


    

    



