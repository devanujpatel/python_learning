import matplotlib.pyplot as plt

x = [3,4,5]
y = [1,2,3]

x2 = [1,2,3]
y2 = [10,20,14]

plt.scatter(x,y ,label="scatter plot 1",s=50,marker="*")
plt.scatter(x2,y2,label="scatter plot 2",s=50,marker="o")
plt.legend()
plt.title("my first matplotlib prog")
plt.show()


