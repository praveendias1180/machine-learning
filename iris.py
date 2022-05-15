# IMPORTING LIBRARIES
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_palette('husl')
import matplotlib.pyplot as plt
# % matplotlib inline

# LOAD THE DATA
url='iris.csv'
col_name = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pd.read_csv(url,names = col_name)

# EXPLORE DATA
print('Dataset Size')
print(dataset.shape)
print('First Five Rows of the Dataset')
print(dataset.head())

print('Summary Statistics of the Dataset')
print(dataset.describe())

print('Data Types and Memmory Usage')
print(dataset.info())

print('classes and the number of examples')
print(dataset['class'].value_counts())

# Violin Plot
# sns.violinplot(y='class', x='sepal-length', data=dataset, inner='quartile')
# plt.show()
# sns.violinplot(y='class', x='sepal-width', data=dataset, inner='quartile')
# plt.show()
# sns.violinplot(y='class', x='petal-length', data=dataset, inner='quartile')
# plt.show()
# sns.violinplot(y='class', x='petal-width', data=dataset, inner='quartile')
# plt.show()

# Pair Plot
sns.pairplot(dataset, hue='class', markers='+')
plt.show()