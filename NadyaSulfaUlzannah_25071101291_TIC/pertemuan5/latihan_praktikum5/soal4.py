gudang_pc = [
    {"item": "Monitor", "harga": 1500000, "stok": 5},
    {"item": "Keyboard", "harga": 400000, "stok": 12},
    {"item": "Mouse", "harga": 250000, "stok": 20}
]

for x in gudang_pc:
    if x["item"] == "Keyboard":
        x["kategori"] = "Aksesoris"
print(gudang_pc)

gudang_pc.append({
    "item" : "Headsed", 
    "harga" : 35000, 
    "stok" : 8
    })
print(gudang_pc)

for i in gudang_pc:
    total = i["harga"] * i["stok"]
    print(f"Item: {i["item"]} | Total Aset: Rp {total}")