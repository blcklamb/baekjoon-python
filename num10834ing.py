beltNum = int(input())
beltSpin = 1
beltSpinClock = 0
for i in range(0, beltNum):    
    a, b, c = map(int, input().split())
    beltSpin *= b/a
    if c == 1:
        beltSpinClock += 1
if beltSpinClock%2==0:
    beltSpinClock = 0
else:
    beltSpinClock = 1
print(beltSpinClock, int(beltSpin))