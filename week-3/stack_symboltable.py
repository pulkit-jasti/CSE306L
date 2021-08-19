# Stack Operations and utility functions
def print_new_line():
	print("\n")

def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if (is_empty(stack)):
        return "stack is empty"
    return stack[:-1]


#Creating the stack	
stack = []
symbolTable = []


# Storing all the identifiersTables 
# Using a set because this is a set of all the identifiers in the program and it should be immutable
identifiersTable = ("variable", "function", "structure", "pointer", "array")



print_new_line()
print('*****CD-LAB-3-WEEK*****')
print_new_line()


#Printing the menu
while (True):
    menuInput = input("Do you want to enter indentifier in the symbol table ?\nPress Y or N please\n ")
    if (menuInput == "Y" or menuInput == "y"):
        for i in range(len(identifiersTable)):
            print(str(i+1), identifiersTable[i])
        option = int(input("Enter your option : "))

        if (option == 1):
            varname = input("Enter the name of the variable : ")
            x = False
            for i in symbolTable:
                if (i[0] == varname):
                    x = True
                    break
            if (x == False):
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
                symbolTable.append(stack)
                stack = []
            else:
                print("The variable already exits in the symbol table")

        if (option == 2):
            ls = []
            funname = input("Enter the name of the function : ")
            x = False
            for i in symbolTable:
                if (i[0] == funname):
                    x = True
                    break
            if (x == False):
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
                symbolTable.append(stack)
                stack = []
            else:
                print("The function identifiersTable already exists in the symbol table")
        
        if (option == 3):
            ls = []
            structname = input("Enter the name of the structure : ")
            x = False
            for i in symbolTable:
                if (i[0] == structname):
                    x = True
                    break
            if (x == False):
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
                symbolTable.append(stack)
                stack = []
            else:
                print("The structure identifiersTable already exists in the symbol table")
        
        if (option == 4):
            ptrname = input("Enter the name of the pointer : ")
            x = False
            for i in symbolTable:
                if (i[0] == ptrname):
                    x = True
                    break
            if (x == False):
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
                symbolTable.append(stack)
                stack = []
            else:
                print("The pointer identifiersTable already exists in the symbol table")
        
        if (option == 5):
            ls = []
            arrname = input("Enter the name of the array : ")
            x = False
            for i in symbolTable:
                if (i[0] == arrname):
                    x = True
                    break
            if (x == False):
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
                symbolTable.append(stack)
                stack = []
            else:
                print("The array identifiersTable already exists in the symbo table")
    else:
        break
print("\n"*2)
print("Symbol Table")
print_new_line()
print("\tVariables")
print_new_line()
print("name\tdatatype\tscope\t\taddress")
for i in symbolTable:
    if (i[0] == 'variable'):
        print(str(varname)+"\t"+str(vardtype)+"\t\t"+str(varscope)+"\t\t"+str(varid))
else:
    print("---------------------******---------------------")
print_new_line()
print("\tPointers")
print_new_line()
print("name\tdatatype\tidentifiersTable holding\t\tvalue\t\t\taddress")
for i in symbolTable:
    if (i[0] == 'pointer'):
        print(str(ptrname)+"\t"+str(ptrtype)+"\t\t\t"+str(ptrpoint)+"\t\t\t"+str(ptrvalue)+"\t\t\t"+str(ptrid))
else:
    print("---------------------******---------------------")
print_new_line()
print("\tFunctions")
print_new_line()
print("name\treturntype\tno. of para\t(name,datatype)\t\t\tpassing method\t\t\taddress")
for i in symbolTable:
    if (i[0] == 'function'):
        print(str(funname)+"\t"+str(funreturn)+"\t\t"+str(funpara)+"\t\t"+str(i[4])+"\t\t"+str(funpara1)+"\t\t\t"+str(funid))
else:
    print("------------------------------------------")
print_new_line()
print("\tStructures")
print_new_line()
print("name\tmembers\t(name,datatype)\t\t\t\taddress")
for i in symbolTable:
    if (i[0] == 'structure'):
        print(str(structname)+"\t"+str(structmem)+"\t"+str(i[3])+"\t"+str(structid))
else:
    print("---------------------******---------------------")
print_new_line()
print("\tArrays")
print_new_line()
print("name\tdatatype\tdim\tdimvalue\taddress")
for i in symbolTable:
    if (i[0] == 'array'):
        print(str(arrname)+"\t"+str(arrtype)+"\t\t"+str(arrdim)+"\t\t"+str(i[4])+"\t\t"+str(arrid))
else:
    print("---------------------******---------------------")