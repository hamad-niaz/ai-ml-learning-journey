import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Books_Data_Clean")
print(df)
# # print(df.shape)
# # print(df.head())
# # print(df.dtypes)
# # print(df.describe())

# # print(df['day'].value_counts())
# # sns.histplot(data=df, x = "total_bil")
# # plt.show()

# # average_bill = df.groupby('day')['total_bill'].max()
# # print(average_bill)

# # print("Highest average bill:", average_bill.idxmax())


# # sns.scatterplot(data = df, x = "total_bill", y= "tip")
# # plt.show()

# correlation = df[["total_bill", "tip", "size"]].corr()
# sns.heatmap(correlation, annot=True)
# plt.show()