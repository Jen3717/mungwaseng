import csv

#read CSV file

def getCsv():
    csvlist = []

    f = open('C:\Files\sample1.csv', 'r') # 현재 경로의 sample.csv를 연다
    csvReader = csv.reader(f) # csv.reader로 파일을 읽는다.

    for i in csvReader:
        csvlist.append(i)
        # all the datas in CSV is saved as 'list'

    f.close()

    return csvlist

print(getCsv())

