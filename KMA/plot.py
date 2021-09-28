import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

font = {
    'family': 'Denaju Sans',
    'size': 14,
    'weight': 'bold'
}
#plt.rc('font', **font)

# plt.title("플롯팅")
#plt.plot([10, 20, 30, 40], "r.", label="asc", color='skyblue', linestyle='--')
#plt.plot([40, 30, 20, 10], "g^", label="desc", linestyle=":")
# plt.legend(loc=5)
# plt.show()

#plt.hist([1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 10])
# plt.show()


def histPlot():
    dice = []
    for i in range(100):
        dice.append(random.randint(1, 6))
    plt.hist(dice, bins=6)
    print(dice)
    plt.show()


def box_plot():
    results = []
    for i in range(13):
        results.append(random.randint(1, 1000))
    print(sorted(results))
    np_results = np.array(results)
    print("1/4:{0}, 2/4:{1}, 3/4:{2}".format(np.percentile(np_results, 25),
          np.percentile(np_results, 50), np.percentile(np_results, 75)))
    plt.boxplot(results)
    plt.show()


box_plot()
