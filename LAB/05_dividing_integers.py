eggs = int(input("Enter total eggs: "))
trays = eggs // 30          # หารเอาเฉพาะจำนวนเต็ม (แผง)
remaining = eggs % 30       # หารเอาเศษ (ฟองที่เหลือ)

print(f"Trays: {trays} Remaining: {remaining}")
