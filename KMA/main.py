from os import path
import csv
import matplotlib.pyplot as plt

dir = path.dirname(path.realpath(__file__))
filePath = path.join(dir, 'seoul1.csv')
print(filePath)

#f = open(filePath, 'r', encoding='cp949')
f = open(filePath, 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')
header = []
header_len = 7
while header_len > 0:
    header.append(next(data))
    header_len -= 1
columns = next(data)
print(columns)

max_temp = -1
max_date = ''
results = []
highs = []
lows = []
for row in data:
    try:
        if row[-1] == '':
            row[-1] = -999
        else:
            row[-1] = float(row[-1])
            results.append(row[-1])
            if row[0].split('-')[1] == '03' and row[0].split('-')[2] == "09":
                highs.append(float(row[-1]))
                lows.append(float(row[-2]))
            if max_temp < row[-1]:
                max_date = row[0]
                max_temp = row[-1]

    except Exception as e:
        print(e)

print('기상 관측이래 서울의 최고 기온이 가장 높았던 날은 {0}로 {1}도였습니다'
      .format(max_date, max_temp))
f.close()


print(len(results))
plt.rc('font', family="AppleGothic")
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 2))
plt.title("03-09 최고온도 및 최저온도")
plt.plot(highs, 'hotpink', label='최고온도')
plt.plot(lows, 'skyblue', label="최저온도")
plt.legend()
plt.show()
