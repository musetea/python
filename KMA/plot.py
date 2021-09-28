import random
import matplotlib as mpl
import matplotlib.pyplot as plt

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

dice = []
for i in range(5):
    dice.append(random.randint(1, 6))
print(dice)
