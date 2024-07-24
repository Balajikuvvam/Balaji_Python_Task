def average(*args):
    sum = 0
    for i in args:
        sum+=i
    a=len(args)
    avg=sum/a
    return avg
print(average(1,2,3,4,5,6,7,8,9))
print(average(22,33,55,66,88,99,77,55,40,401))
      
