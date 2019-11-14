
# Writing to an excel sheet using Python
import xlwt
from xlwt import Workbook

import re

def get_lines(filename):
    """
    Read all lines from `filename` and return a list of strings,
    one per line, with whitespace stripped from the ends.
    >>> lines_list = get_lines("doctestText.txt")
    doctestText.txt
    >>> print(lines_list[0:2])
    ['Tomorrow, and tomorrow, and tomorrow,', 'Creeps in this petty pace from day to day,']
    """
    print(filename)
    lines = []
    with open(filename) as fp:
        for line in fp:
            processed_line = line.strip()
            lines.append(processed_line)
    return lines

def make_spreadsheet(filename, id, id_underscore):
    # Workbook is created
    wb = Workbook()

    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')

    lines_list = get_lines(filename)

    start = 0;
    counter = 0;

    for i in range (len(lines_list)):
        print(lines_list[i])
        if lines_list[i-1] == "" and lines_list[i] == "":
            p = str(lines_list[start:i])
            if re.search('[a-zA-Z]', p) and p.isupper()==False:
                sheet1.write(counter, 0, str(counter)+ id_underscore)
                sheet1.write(counter, 1, id)
                sheet1.write(counter, 2, p)
                counter += 1;
            start = i;


    wb.save('xlwt both.xls')



# Run this code when called from the command line
if __name__ == "__main__":
    import doctest

    # Run all doctests in this file
    doctest.testmod()
