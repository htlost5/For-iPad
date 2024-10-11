import time
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes_up_to(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    try:
        number = int(input("X="))
        if number < 2:
            print("2以上の整数を入力してください。")
            return
        
        start_time = time.perf_counter()

        primes = get_primes_up_to(number)
        
        print(f"\n{number}までの素数のリスト:")
        print(primes)
        
        print(f"\n{number}は素数です。" if is_prime(number) else f"\n{number}は素数ではありません。")
        
        print(f"\n{number}までの素数の個数: {len(primes)}")

        end_time = time.perf_counter()

        count_time = end_time - start_time

        print(f'time: {count_time:.6f}s')

    except ValueError:
        print("有効な整数を入力してください。")

if __name__ == "__main__":
    main()