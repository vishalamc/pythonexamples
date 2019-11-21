from numpy import cov
import matplotlib.pyplot as plt

# prepare data
data1 =[ 2.1, 2.5, 3.6, 4.0]
data2 = [ 8, 10, 12, 14]
# calculate covariance matrix
covariance = cov(data1, data2)
print(covariance)

# plot
plt.xlabel('data1')
plt.ylabel('data2')
plt.scatter(data1, data2)
plt.show()
