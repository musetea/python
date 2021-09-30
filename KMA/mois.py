# 인구통계
import csv
import utils

filePath = utils.get_join('mois_seoul.csv')
print(filePath)

f = open(filePath, 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = next(data)
# print(header)


for row in data:
    print(row)
