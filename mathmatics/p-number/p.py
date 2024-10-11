import time
import cProfile
number = int(input("X="))

start_time = time.perf_counter()

numbers = [list for list in range(2, number+1)]
multi = 2

while multi <= number/2:
    for i in numbers:
        if i % multi == 0:
            numbers.remove(i)
    numbers.append(multi)
    multi = numbers[0]
numbers.sort()

print(numbers)

if number in numbers:
    print(f"{number}は素数です。")
    print(f'その数までの素数は{len(numbers)}個あります。')
else:
    print(f'{number}は素数ではありません。')
    print(f'その数までの素数は{len(numbers)}個あります。')

end_time = time.perf_counter()

count_time = end_time - start_time

print(f'time:{count_time:.6f}s')