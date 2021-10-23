transaction_list = [250, 12, 45, 32, 23, 25, 250, 12]
n = len(transaction_list)
for i in range(n-1):
    k = i
    for j in range(i+1,n):
        if transaction_list[j] < transaction_list[k]:
            k = j
    if i != k:
        tmp = transaction_list[i]
        transaction_list[i] = transaction_list[k]
        transaction_list[k] = tmp
print(transaction_list)

#Avec la fonction sort()
#transaction_list.sort()
#print(transaction_list)




