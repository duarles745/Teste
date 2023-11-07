import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,5))
plt.title("Função Constante")

x = np.linspace(-10, 10, 10000)
y = 20*np.ones(x.shape)

plt.plot(x, y)
plt.show()