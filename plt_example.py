import matplotlib.pyplot as plt

# data to plot
labels = ['Python', 'C++', 'JavaScript', 'Java']
sizes = [245, 130, 215, 210] # x/sum(x) all can use percentage
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0) # explode first slice

# plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()