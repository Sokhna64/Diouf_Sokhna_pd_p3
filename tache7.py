transaction_list = [250, 12, 45, 32, 23, 25, 250, 12]
liste = []
for i in range(0, (len(transaction_list))):
    if transaction_list[i] not in transaction_list[i+1:]:
        liste.append(transaction_list[i])
print(liste)            
        
       