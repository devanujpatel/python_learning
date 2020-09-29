import matplotlib.pyplot as plt

my_integers= list(range(1,6))
cubes= []
for integer in my_integers:
    integer = integer * integer * integer
    cubes.append(integer)

plt.plot(cubes,my_integers,color="green")
plt.show()