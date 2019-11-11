# FizzBuzz
def fizzbuzz(x):
    for i in range(1,x+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizzbuzz(20)

# Fibonacci
def fibo(urut) :
    listData = [1,1]
    for i in range(2,urut):
        listData.append(listData[i-2] + listData[i-1])
    print(listData)

fibo(6)

# Reverse List
def listNya(x):
    listNyo = []
    for i in x:
        listNyo.insert(0, i)
    print(listNyo)

listNya([1, 2, 3, 4, 5, 6, 7, 8])