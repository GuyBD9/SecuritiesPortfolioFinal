import matplotlib
matplotlib.use("macosx")  # נסה גם "macosx" אם אתה על macOS
import matplotlib.pyplot as plt

plt.figure()
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Test Plot")
plt.show()
