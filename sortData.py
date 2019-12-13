"""
Allows user to manually sort data using the terminal

For each sentence:
0: pro-recovery 1: pro-ana 2: neutral 3: bad data
Came from [number]

“sentence here”


On “s”: you ended at row ___


"""

import xlwt # allows writing to excel
import xlrd # allows reading excel
from xlwt import Workbook
import re
import os

# open data.xls to read
book = xlrd.open_workbook("data.xls")

# get the first worksheet to read
sheet = book.sheet_by_index(0)


# Create Workbook to put stuff into
wb0 = Workbook()
wb1 = Workbook()
wb2 = Workbook()
wb3 = Workbook()

# create sheet in each workbook to put stuff into
sheet0 = wb0.add_sheet('Sheet 0')
sheet1 = wb1.add_sheet('Sheet 1')
sheet2 = wb2.add_sheet('Sheet 2')
sheet3 = wb3.add_sheet('Sheet 3')

counter0 = 0
counter1 = 0
counter2 = 0
counter3 = 0


i = int(input("Which row would you like to start at?"))
print(i)

for i in range (sheet.nrows):
    print("Line:  "+ str(i))

    print(sheet.cell(i, 2))
    print("0:pro-recovery, 1:pro-ana, 2:neutral, 3:bad data")
    decision = input("Sort: ")
    print(type(decision))
    print(decision)

    id = str(sheet.cell(i, 0))
    sentence = str(sheet.cell(i, 2))

    if decision == "0":
        # code for writing to make_spreadsheet: write(row, column, text)
        sheet0.write(counter0, 0, id)
        sheet0.write(counter0, 1, decision)
        sheet0.write(counter0, 2, sentence)
        counter0 += 1 # increased by one with every line written to sheet

    elif decision == "1":
        sheet1.write(counter1, 0, id)
        sheet1.write(counter1, 1, decision)
        sheet1.write(counter1, 2, sentence)
        counter1 += 1 # increased by one with every line written to sheet

    elif decision == "2":
        sheet2.write(counter2, 0, id)
        sheet2.write(counter2, 1, decision)
        sheet2.write(counter2, 2, sentence)
        counter2 += 1 # increased by one with every line written to sheet


    elif decision == "3":
        sheet3.write(counter3, 0, id)
        sheet3.write(counter3, 1, decision)
        sheet3.write(counter3, 2, sentence)
        counter3 += 1 # increased by one with every line written to sheet


    elif decision == "s":
        print("You have paused at row: "+ str(i))
        wb0.save('0.xls')
        wb1.save('1.xls')
        wb2.save('2.xls')
        wb3.save('3.xls')
