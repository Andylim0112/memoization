## recursive function
import time
def recur(n, depth = 0):
    if n == 0:
        return
    print('A', depth * ' ', n)
    recur(n-1, depth + 1)
    print('B', depth * ' ', n)

count = 0
def fib(n):
    global count
    count += 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib (n-2)

##
##for i in range(20):
##    print(i, fib(i), count)

def fibl(n):
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list[n]

def fibd(n):
    fib_dict = {0:0, 1:1}
    for i in range(2, n + 1):
        fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]
    return fib_dict[n]

#momoization

fibm_dict = {0:0, 1:1}
def fibm(n):
    if n not in fibm_dict:
        fibm_dict[n] = fibm(n - 1) + fibm(n - 2)
    return fibm_dict[n]

while True:
    in_val = input('Enter a fibonacci number to calculate: ')
    if in_val == 'done':
        break
    size = int(in_val)
    start_time = time.time()
    print(fibm(size), 'processing time: %.5f' %(time.time() - start_time))
    
