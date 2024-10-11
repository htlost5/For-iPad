import math
import time
from tabulate import tabulate

set = True
number = 1
AA = aa = number
Aa = number * 2

count = 0

# Open a file in write mode
with open("output.txt", "w", encoding="utf-8") as file:
    # Define headers outside the loop
    headers1 = ["回数", "AA", "Aa", "aa"]
    headers2 = ["丸", "しわ"]
    combined_headers = headers1 + [""] + headers2

    # Write headers once before entering the loop
    file.write(tabulate([], headers=combined_headers, tablefmt="grid") + "\n")

    while set:
        count += 1

        AA = AA * 4 + Aa * 1
        aa = aa * 4 + Aa * 1
        Aa *= 2

        gcd_ab = math.gcd(math.gcd(int(AA), int(Aa)), int(aa))

        AA /= gcd_ab
        Aa /= gcd_ab
        aa /= gcd_ab

        data1 = [str(count), f"{AA:.2f}", f"{Aa:.2f}", f"{aa:.2f}"]
        data2 = [f"{AA + Aa:.2f}", f"{aa:.2f}"]

        combined_data = [data1 + [""] + data2]

        # Write only the data rows inside the loop to the file with uniform column width
        file.write(tabulate(combined_data, tablefmt="grid", showindex=False, colalign=("center",) * len(combined_headers)) + "\n")

        if count == 5:
            set = False

        time.sleep(1)  # Wait for 1 second