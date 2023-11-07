data = open("D:\DevStuff\DevSchool\Exercises\data-python\CupcakeInvoices.csv")

for row in data:
    print(row)
data.close()
data = open("D:\DevStuff\DevSchool\Exercises\data-python\CupcakeInvoices.csv")

for row in data:
    values = row.split(',')
    print(values[2])
data.close()
data = open("D:\DevStuff\DevSchool\Exercises\data-python\CupcakeInvoices.csv")

total = 0
for row in data:
    values = row.split(',')
    total += float(values[3]) * float(values[4]) 

print(round(total, 2))
data.close()