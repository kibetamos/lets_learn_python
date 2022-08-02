cows = ['cow1','cow2','cow3','cow4','cow5']

print(cows)
for b in range(0,len(cows)):
    print(cows[b],end=' ')
print("\nThe list after reversal is : ")
for b in range(len(cows)-1,-1,-1):
    print(cows[b],end=' ')
