import sound
import matplotlib.pyplot as plt

plt.plot([sound.sine(100, 5000, i) for i in range (50)])
plt.show()