__counter=0

def sum1(list):
    global __counter
    __counter+=1
    sum=0
    for el in list:
        sum+=el
    return sum
def prod1(list):
    global __counter
    __counter+=1
    prod=1
    for el in list:
        prod*=el
    return prod

if __name__ == "__main__":
    print('Preferiría ser un modulo')
    l = [i for i in range(1,6)]
    print(sum1(l)==15)
    print(prod1(l)==120)
else:
    print('Me gusta ser un modulo')