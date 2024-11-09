import numpy as np
'''
arr = np.array([1,2,3])
z = np.zeros((2,3))
o = np.ones((3,3))
e = np.eye(4)
f = np.full((1,2),47)

seqa = np.arange(0,10, 2)
print(seqa)

lin = np.linspace(0,1,3)
print(lin)

marr = np.random.rand(3,3)
print(marr)

miarr = np.random.randint(0,1000,(3,3))
print(miarr)


rshape = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape((6,2))
print(rshape)


a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

d = a + b + c
print(d)

l = []
l.append(a)
l.append(b)
l.append(c)

print(l)

m = []
m.extend(a)
m.extend(b)
m.extend(c)

print(m)

v = np.hstack((a,b,c))
print(v)

sp = np.split(np.array([1,2,3,4,5,6,7,8]),4)
print(sp)

tr = np.array([[1,2],[3,4]]).transpose()
print(tr)
print(tr.transpose())

ad = np.add([1,2],[3,4])
print(ad)
mu = np.multiply([[1,2],[3,4]],[[5,6],[7,8]])
print(mu)

dp = np.dot([[1,2],[3,4]],[[5,6],[7,8]])
print((dp))


mn = np.mean([1,10, 1000000])
print(mn)

std = np.std([1,2,3])
print(std)
'''
arr1 = np.array([[1,2,3],[4,5,6]])
print(np.where(arr1>1,arr1*5,"NUM"))

arr2 = np.array([0,1,2,3,4])
result = np.where(arr2%2==0,'Even','Odd')
print(result)