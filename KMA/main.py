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
aug = []
jan = []
month = [[], [], [], [], [], [], [], [], [], [], [], []]
days = []
for i in range(31):
    days.append([])

for row in data:
    try:
        if row[-1] == '':
            row[-1] = -999
        else:
            row[-1] = float(row[-1])
            max_temp = row[-1]
            results.append(max_temp)
            dates = row[0].split('-')

            month_idx = int(dates[1])-1
            #print(month_idx, max_temp)
            month[month_idx].append(max_temp)
            if dates[1] == '03' and dates[2] == "09":
                highs.append(float(row[-1]))
                lows.append(float(row[-2]))
            elif dates[1] == "08":
                aug.append(row[-1])
                days[int(dates[2])-1].append(max_temp)
            elif dates[1] == "01":
                jan.append(row[-1])

            if max_temp < row[-1]:
                max_date = row[0]
                max_temp = row[-1]

    except Exception as e:
        print(e)
f.close()

# print(month)


def max_seoul():
    print('기상 관측이래 서울의 최고 기온이 가장 높았던 날은 {0}로 {1}도였습니다'
          .format(max_date, max_temp))


def min_max_day():
    print(len(results))
    plt.rc('font', family="AppleGothic")
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(10, 2))
    plt.title("03-09 최고온도 및 최저온도")
    plt.plot(highs, 'hotpink', label='최고온도')
    plt.plot(lows, 'skyblue', label="최저온도")
    plt.legend()
    plt.show()


def histPlot():
    #plt.hist(results, bins=100, color='r', label="all")
    plt.hist(aug, bins=100, color="r", label="aug")
    plt.hist(highs, bins=100, color='b', label="hights")
    plt.hist(lows, bins=100, color="g", label="lows")
    plt.legend()
    plt.show()
# histPlot()


def box_plot():
    #plt.boxplot([jan, aug])
    plt.boxplot(month)
    plt.show()
# box_plot()


def gg_plot():
    plt.style.use('ggplot')
    plt.figure(figsize=(10, 5), dpi=300)
    plt.boxplot(days, showfliers=False)
    plt.show()


gg_plot()
