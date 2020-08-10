#请编写一个函数输入n, 输出n个斐波那契数列的列表。 如：fib(5) -> [1, 1, 2, 3, 5]
def fibonacci(num):
    fList = []
    for i in range(0, num):
        if len(fList) < 2:
            fList.append(1)
            continue
        fList.append(fList[-1]+fList[-2])
    return fList

print(fibonacci(10))