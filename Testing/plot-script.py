import matplotlib.pyplot as plt 

values = [-39.1, -39.3, -48.05, -50.5, -49.8, -52.8, -58.08, -54.1, -55.1, -55.877]

x = []
y = []

for a, b in enumerate(values):
	x.append(a+1)
	y.append(b)

print(x)
print(y)

plt.plot(x, y)

#plt.gca().invert_yaxis()
plt.show()
