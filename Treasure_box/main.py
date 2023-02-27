row1 = ["&", "&", "&"]
row2 = ["&", "&", "&"]
row3 = ["&", "&", "&"]

MAP = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("where do you wanna place yr treasure")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = (MAP[vertical - 1])
selected_row[horizontal - 1] = "X"

# print(MAP[vertical - 1])
# print(MAP[horizontal - 1])

print(f"{row1}\n{row2}\n{row3}")
