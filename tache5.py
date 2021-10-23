transaction_list = [250, 12, 45, 32, 23, 25, 250, 12]
min=transaction_list[0]
x=transaction_list[1:]
for i in x:
    if i<min:
        min=i
print(min)

#Avec la fonction min : 
# x=min(transaction_list)
#print(x)