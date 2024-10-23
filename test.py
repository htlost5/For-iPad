import time

for i in range(10, 0, -1):
    print(f'\rカウントダウン: {i}', end="")
    time.sleep(1)
print('\n終了!')