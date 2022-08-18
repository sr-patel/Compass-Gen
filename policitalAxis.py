import matplotlib.pyplot as plt

# creates values so graph will be extended to correct dimensions
x = [-10, 10, -10, 10] 
y = [10, 10, -10, -10]

plt.scatter(x, y, color="black")

plt.plot([0, 0], [-10, 10], color="black")
plt.plot([-10, 10], [0, 0], color="black")

#contains personal values
personX = [] 
personY = []

numP = int(input("How many people will be added to the axis?\n"))
print("")

for i in range(0,numP):
    perX = float(input("What is the X value for person" + " " + str(i) + "?\n"))
    personX.append(perX)
    perY = float(input("What is the Y value for person" + " " + str(i) + "?\n"))
    personY.append(perX)
    print("")
    
plt.scatter (personX, personY, color="black")

# creates color zones of the four political quadrants 
plt.axhspan(-10, 0, facecolor="green", alpha=0.3, xmax=0.5) 
plt.axhspan(0, 10, facecolor="red", alpha=0.3, xmax=0.5)
plt.axhspan(0, -10, facecolor="purple", alpha=0.3, xmin=0.5)
plt.axhspan(10, 0, facecolor="blue", alpha=0.3, xmin=0.5)

# labels 
plt.xlabel("Economic") 
plt.ylabel("Social") 
plt.title("Political Axis")

# saves as .png file to root, displays graph 
plt.savefig ("TCH-PA.png") 
plt.show()

