#bar chart

from matplotlib import pyplot as plt
import numpy as np

#print(plt.style.available) # gives all available styles
plt.style.use('ggplot') #use this style

month=['jan', 'feb', 'mar', 'apr', 'may']
xaxis=np.arange(len(month))
width=0.25

sal1=[1000,2000,2300,1830,2000]
sal2=[1000,3400,4000,2900,3400]
sal3=[5600,5700,5000,5300,5900]

plt.bar(xaxis,sal1, color='k', label='2019', width=width)
plt.bar(xaxis+width,sal2, color='y', label='2020', width=width)
plt.bar(xaxis-width,sal3, label=2021, width=width)

plt.xlabel('Month')
plt.ylabel('salaries')
plt.title('Chart - Month Vs Salaries')
plt.xticks(ticks=xaxis,labels=month)

plt.legend()
plt.tight_layout() # make small size
plt.grid(True) # enable grid

plt.savefig('barchart.png')
plt.show()

