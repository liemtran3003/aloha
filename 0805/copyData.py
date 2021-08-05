import openpyxl

wb = openpyxl.load_workbook("0805.xlsx")

ws_hello = wb["hello"]
ws_hello2 = wb["hello2"]

for i in range(1, 2):
	for n in range(1,8):
		copydata = ws.cell(row = i, column = n).value
	ws_hello2 = print(copydata)
wb.save("0805.xlsx")