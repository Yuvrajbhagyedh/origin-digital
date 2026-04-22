import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[12,32,43,23,12]
y2=[23,34,32,12,32]

plt.figure(figsize=(9,6))
plt.subplot(1,2,1)
plt.plot(x,y1,marker="*")
plt.title("p1")


plt.subplot(1,2,2)
plt.plot(x,y2,marker="o")
plt.title("p2")
plt.show()
