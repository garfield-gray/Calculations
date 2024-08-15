import matplotlib.pyplot as plt

x = range(1, 1001)
y = [i**2 for i in x]
# plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x, y, s=10)
