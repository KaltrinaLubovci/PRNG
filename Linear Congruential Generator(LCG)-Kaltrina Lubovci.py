import datetime

modulus=100
a=57
ep = datetime.datetime(1970, 1, 1, 0, 0, 0)
x = (datetime.datetime.utcnow() - ep).total_seconds()
seed = int(round(x))
for c in range(5):
    seed = (a * seed + c) % modulus
    print(seed, end="\t")

