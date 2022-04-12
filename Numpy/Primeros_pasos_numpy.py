import numpy as np
from matplotlib import pyplot as plt


a = np.array([1, 2, 3, 4, 5])
b = np.array([7, 8, 9, 5, 7])

# c = a * b
c = np.dot(a, b)
# print(c)

# x = [1, 2, 3, 4, 5]
# y = [7, 8, 9, 5, 7]
#
# z = x - y
# print(z)

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(m)
# print(m * m)
# print(m - m)

m2 = np.transpose(m)
# print(m2)

file = np.loadtxt("datos.csv")
print(file)
# print(file[:,0])
# plt.plot(file[:,0], file[:,1], '.', color = 'red', label = r'migrafica $\Delta_3 N^4$')
# plt.plot(file[:,0], file[:,1], '-', color = 'blue', label = r'continuo $\Delta_3 N^4$')
# plt.legend()
# plt.xlabel('ordenadas', fontsize = 16)
# plt.ylabel('cordenadas', fontsize = 16)
# plt.title('miTitulo')
# plt.show()

a3d = np.array([1, 2, 3, 15, 5, 6, 7, 8])
ax = plt.axes(projection = '3d')
ax.plot3D(file[:,0], file[:,1], a3d, '.', color = 'red', label = r'migrafica $\Delta_3 N^4$')

plt.show()