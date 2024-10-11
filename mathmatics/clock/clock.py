from fractions import Fraction

def h_m(y):
    h = y
    y *= 720 
    calc = y/11
    count_minutes = int(calc - 60*h)
    count_seconds = (calc%1 * 60)

    return calc, count_minutes, count_seconds
    # 5.5x = 360y

y = int(input("what time? → "))
calc, count_minutes, count_seconds = h_m(y)

print(f'{y}時{count_minutes}分{count_seconds:.2f}秒')