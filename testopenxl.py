#/usr/bash/python
# *--coding:uft-8 --*

"""the code is just testing the package of openpyxl"""

from openpyxl import Workbook

#creating the excel file
wb = Workbook()

#the other way is loading the file
wb = Workbook("testfile.xlsx")