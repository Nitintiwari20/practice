import numpy as np
import random
import time
import os

# Matrix characters
chars = list("01")

# Screen size
rows = 20
cols = 60

try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        matrix = np.random.choice(chars, size=(rows, cols))

        for row in matrix:
            line = "".join(row)
            print(line)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nMatrix stopped.")