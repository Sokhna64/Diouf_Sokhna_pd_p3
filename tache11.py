transaction_list = [250, 12, 45, 32, 23, 25, 250, 12]
listkey =[ i for i in range(0,len(transaction_list))]
dico = {}
for i in listkey:
    for j in transaction_list:
        dico[i]= j
        transaction_list.remove(j)
print(dico)