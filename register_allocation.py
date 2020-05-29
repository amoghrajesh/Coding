data = ['a = b + 1', 'c = a + 8', 'd = b * 7', 'a = k - 1','x = y + z', 'm = p + q','a = b + 1', 'h = b + 1']

'''

a: R4 , 1:R3, 7:R5, d:R6, k:R7, b: R2, z:R9, x:R10, p:R11, q:R0, m: R1, 

LD R0, b
MOV R1, #1
ADD R2, R0, R1

a is in R2
MOV R3, #8
ADD R4, R2, R3

c is in R4

MOV R5, #7
MUL R6, R0, R5

D IS IN R6

LD R7, k
ADD R8, R0, R5


'''

# ST a, R2   ST c, R4  ST d, R6 ST
n=len(data)
reg=[0]*12
var={} # a: R0
store_seq=[]
arithmetic_operator = {'+':"ADD", '-':"SUB", "*":"MUL" }
fifo_reg = 0

#this is supposed to reallocate one register
def fifo():
    print(" In FIFO Function", var)
    global fifo_reg
    for k,v in var.items():
        if v == 'R'+str(fifo_reg):
            var.pop(k)
            if k in store_seq:
                store_seq.remove(k)
                print("ST", k, v)
            fifo_reg = int(v[1:]) + 1
            print("FIFO reg & v", fifo_reg, v)
            return v

def getreg():
    for i in range(0,12):
        if reg[i]==0:
            reg[i]=1
            return 'R'+str(i)

    register = fifo()
    print("REGISTER" , register)
    return register

for lines in data:
    line=lines.split()
    operand1 = line[2] #can either be a number or a alphabet
    operand2 = line[4]
    lhs = line[0]

    if operand1.isalpha():
        if operand1 not in var:
            var[operand1] = getreg()
            print("LD", var[operand1], operand1)

    else:
        if operand1 not in var:
            var[operand1] = getreg()
            print("MOV", var[operand1], '#' + operand1)

    if operand2.isalpha():
        if operand2 not in var:
            var[operand2] = getreg()
            print("LD", var[operand2], operand2)
    else:
        if operand2 not in var:
            var[operand2] = getreg()
            print("MOV", var[operand2], '#' + operand2)

    operator = arithmetic_operator[line[3]]
    if lhs in store_seq:
        #remove the old occurence and put new one -->
        old_reg = var[lhs]
        index = store_seq.index(lhs)
        store_seq.pop(index)
        var[lhs] = getreg()
        reg[int(old_reg[1:])] = 0

    else:
        var[lhs] = getreg()

    store_seq.append(lhs)

    print(operator,var[lhs],var[operand1],var[operand2])



for i in store_seq:
    print("ST", i, var[i])







