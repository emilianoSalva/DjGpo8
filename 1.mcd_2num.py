def mcd(a,b):
    mcd = 1
    if a % b == 0:
        return b
    for i in range(int(b/2),0,-1):
        if a % i == 0 and b % i == 0:
            mcd = i
            break
    return mcd

print(mcd(10,5))
print(mcd(13,7))