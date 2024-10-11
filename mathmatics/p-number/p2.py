import time
def p():
    start_time = time.perf_counter()
    number=int(input("X="))
    numbers=list(range(2,number+1))
    n=numbers[0]
    while len([num for num in numbers if num % n == 0])>=2:
        numbers = [num for num in numbers if num % n != 0]
        n=numbers[0]

    if number >= 49:
        numbers = [2, 3, 5, 7] + numbers
    elif number >= 25:
        numbers = [2, 3, 5] + numbers
    elif number >= 9:
        numbers = [2, 3] + numbers
    elif number >= 4:
        numbers = [2] + numbers
    else:
        pass

    print(numbers)
    if number in numbers:
        print(number,"は素数です。")
    else:
        print(number,"は素数ではありません。")
    count=len(numbers)
    print("その数までの素数は",count,"個あります。")

    end_time = time.perf_counter()
    count_time = end_time - start_time
    print(f"time: {count_time:.6f}s")
p()