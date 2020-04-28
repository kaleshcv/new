#plot / Line chart

from matplotlib import pyplot as plt
#print(plt.style.available) # gives all available styles
plt.style.use('fivethirtyeight') #use this style

month=['jan', 'feb', 'mar', 'apr', 'may']

sal1=[1000,2000,2300,1830,2000]
sal2=[3000,3400,4000,2900,3400]
sal3=[5600,5700,5000,5300,5900]

plt.plot(month,sal1, color='k', linestyle='--', marker='.', label='2019')
plt.plot(month,sal2, color='y', marker='.', label='2020', linewidth=3)
plt.plot(month,sal3, label='2021',color='g', linestyle='-', marker='>')

plt.xlabel('Month')
plt.ylabel('salaries')
plt.title('Chart - Month Vs Salaries')

plt.legend()
plt.tight_layout() # make small size
plt.grid(True) # enable grid
plt.savefig('linechart.png')

plt.show()

