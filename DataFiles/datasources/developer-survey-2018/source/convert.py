import csv
import xlsxwriter

def csv_to_xlsx():
    with open('final.csv', 'r', encoding='utf-8') as f:
        read = csv.reader(f)
        workbook = xlsxwriter.Workbook('Workbook.xlsx')
        worksheet = workbook.add_worksheet()
        l = 0
        for line in read:
            print(line)
            r = 0
            for i in line:
                print(i)
                worksheet.write(l, r, i)  
                r = r + 1
            l = l + 1
        workbook.close() 

if __name__ == '__main__':
    csv_to_xlsx()