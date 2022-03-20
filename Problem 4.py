#Ryne Bigueras
#3/18/2022

#Problem 4 Num List Divide


counter = 0
tens=[]
while(counter<=50):
    if counter % 10 == 0:
        tens.append(counter)
    counter = counter + 1

print(tens)
