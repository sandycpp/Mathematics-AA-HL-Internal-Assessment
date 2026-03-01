sequence = [0]*300 #Create the sequence B_n
sequence[0]=1 #Initialize the base case B_0 = 1
for i in range(1, 300): #Generate the sequence using the recurrence
    if(i>=2):
        sequence[i]+=sequence[i-2]
    if(i>=3):
        sequence[i]+=sequence[i-3]
    if(i>=4):
        sequence[i]+=sequence[i-4]
    if(i>=8):
        sequence[i]+=sequence[i-8]
    
print(sequence[218]) #output: 15143251282467089781378508969876444594
