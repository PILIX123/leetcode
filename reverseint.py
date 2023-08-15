import timeit
import random
def reverse(x: int) -> int:
    val = "".join(list(reversed(str(abs(x)))))
    if(int(val)>pow(2,31)-1):
        return 0
    if(x<0):
        return int(f"-{val}")
    return int(val)
start = timeit.default_timer()
for x in range(1041):
    reverse(random.randint(pow(-2,31),pow(2,31)-1))
print(timeit.default_timer()-start)