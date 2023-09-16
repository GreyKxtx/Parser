from src.parser import start
import time

st = time.time()
start()

end = time.time() - st
print(f'Time: {end}')

