import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

# x = bill, y = tip
sns.scatterplot(x='total_bill', y='tip', data=df)
plt.title("Does bigger bill mean bigger tip?")
plt.show()

# 1. Correlation check 
print(df[['total_bill', 'tip', 'size']].corr())
# Output:
# total_bill 
# size aur tip 
# 2. Correlation heatmap (Visual)
sns.heatmap(df[['total_bill','tip','size']].corr(), annot=True)
plt.show()

# 3. Pairplot 
sns.pairplot(df[['total_bill', 'tip', 'size']], hue='sex')
plt.show()