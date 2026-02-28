data_aktivitas = {("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)}

for i, j in data_aktivitas:
    if j > 80:
        print(f"{i} mendapatkan predikat Gold")
    elif j > 50 and j <= 80 :
        print(f"{i} mendapatkanpredikat Silver")
    else:
        print(f"{i} mendapatkan predikat Bronze")