transaction_list = [250, 12, 45, 32, 23, 25, 250, 12]
som=0
for i in transaction_list:
    som=som+i
moy=som/len(transaction_list)
print(moy)