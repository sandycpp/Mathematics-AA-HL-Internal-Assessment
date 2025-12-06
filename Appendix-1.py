sequence = [0]*110 #Create the sequence B_n
sequence[0]=1 #Initialize the base case B_0 = 1
for i in range(1, 110): #Generate the sequence using the recurrence
    if(i>=1):
        sequence[i]+=sequence[i-1]
    if(i>=2):
        sequence[i]+=sequence[i-2]
print(sequence[109]) #output: 43566776258854844738105
