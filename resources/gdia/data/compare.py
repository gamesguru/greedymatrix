#!/usr/bin/env python3

import json

import matplotlib.pyplot as plt


g = json.load(open("OD_MATRIX_FILE.json", "rb"))["ODMatrix"]["records"]
e = json.load(open("matrix-esri.json", "rb"))["ODMatrix"]["records"]

gdia = []
esri = []
ratios = []
for o in g:
    for i in g[o]:
        gdia.append(g[o][i] / 60 / 1000)
        esri.append(e[o][i] / 60 / 1000)
        ratios.append(g[o][i] / e[o][i])

avg_ratio = sum(ratios) / len(ratios)
print(avg_ratio)
# ratios = list(filter(lambda x: x < 5, ratios))
# x = list(range(0, len(ratios)))
x = list(range(0, len(ratios)))

fig, ax = plt.subplots()

# Plot the data
# data_line = ax.plot(x, ratios, label="Data", marker="o")
data_line = ax.plot(x, gdia, label="Gdia", marker="o")
data_line = ax.plot(x, esri, label="Esri", marker="o")

# Plot the average line
# mean_line = ax.plot(x, [avg_ratio] * len(x), label="Mean", linestyle="--")

# Make a legend
ax.set_xlabel("Matrix Entry (819x819)")
ax.set_ylabel("Travel time (min)")
legend = ax.legend(loc="upper right")

plt.show()


# # Create some random data
# x = np.arange(0, 10, 1)
# y = np.zeros_like(x)
# y = [random.random() * 5 for i in x]

# # Calculate the simple average of the data
# y_mean = [np.mean(y)] * len(x)

fig, ax = plt.subplots()

# Plot the data
data_line = ax.plot(x, y, label="Data", marker="o")

# Plot the average line
mean_line = ax.plot(x, y_mean, label="Mean", linestyle="--")

# Make a legend
legend = ax.legend(loc="upper right")

plt.show()
