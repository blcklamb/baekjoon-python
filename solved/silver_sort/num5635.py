stuNum = int(input())
oldest = []
youngest = []

for _ in range(stuNum):
    name, day, month, year = input().split()
    if oldest == []:
        oldest=[name, int(day), int(month), int(year)]
        youngest=[name, int(day), int(month), int(year)]
    elif oldest[3] >= int(year):
        if oldest[3] > int(year):
            oldest =[name, int(day), int(month), int(year)]
        else:
            if oldest[2] > int(month):
                oldest =[name, int(day), int(month), int(year)]
            elif oldest[2] == int(month):
                if oldest[1] > int(day):
                    oldest =[name, int(day), int(month), int(year)]
    elif youngest[3] <= int(year):
        if youngest[3] < int(year):
            youngest =[name, int(day), int(month), int(year)]
        else:
            if youngest[2] < int(month):
                youngest =[name, int(day), int(month), int(year)]
            elif youngest[2] == int(month):
                if youngest[1] < int(day):
                    youngest =[name, int(day), int(month), int(year)]
    
print(youngest[0])
print(oldest[0])
