def even_nums_in_vector(vector):
    for i in vector:
        if i % 2 == 0:
            print i

def even_num(num):
    print num % 2 == 0

def even_nums_upto_num(num):
    i=0
    while i < num:
        if i % 2 == 0:
            print i
        i += 1

def even_nums_upto_num2(num):
    for i in range(num):
        if i % 2 == 0:
            print i

#even_num(6)
#even_nums_upto_num2(10)
vec = [1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1]
even_nums_in_vector(vec)