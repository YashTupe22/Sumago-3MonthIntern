def bill():
    ebill = [1500,1300,1450,1300,1250,
             1450,1200,1600,1230,1110,
             1210,1000]
    for i in range(len(ebill)):
        yield f"Month {i+1}:- {ebill[i]}"

for bills in bill():
    print(bills)