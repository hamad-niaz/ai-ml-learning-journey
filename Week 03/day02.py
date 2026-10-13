# # ##### Pandas Creating Data frame


# # # import pandas as pd
# # # data = {'Name': ['Ali', ' Sara', 'Zain'],
# # #         'Marks': [66, 77, 88]}
# # # df = pd.DataFrame(data)
# # # print (df)


# # # ######Task

# # # import pandas as pd
# # # student = {'Name': ['Ali', ' Sara', 'Zain','shahid'],
# # #         'city': ['Lahore', 'Karachi',' Okara', 'Sahiwa'],
# # #         'score': [66, 77, 88, 76]}
# # # df = pd.DataFrame(student)
# # # print (df)

# # # #####Series vs DAtaFrame

# # # import pandas as pd
# # # s = pd.Series([1,3, 4], index = ["a", "b", "c"])
# # # print(s)
# # # df = pd.DataFrame({'Name': ['Ali', ' Sara', 'Zain','shahid']})
# # # print(df["name"])







# # #########Selection and Indexing

# # # import pandas as pd
# # # df =pd.DataFrame({'Name': ['Ali', ' Sara', 'Zain','shahid'],
# # #            'marks': [89,67,90,66]})
# # # print(df[df["marks"] > 75])
# # # print(df[['marks', 'name']])











# # #########DataFrame Operations(sort, unique, apply)

# # import pandas as pd
# # df = pd.DataFrame{'Name': ['Ali', ' Sara', 'Zain'],
# #         'Marks': [66, 77, 88]}
# # df["Grade"] = df['marks'].apply(
# #     lambda x: 'Pass' if x => 80 else 'fail'
# # )
# # print(df.sort')
    
    
    
    
    
# #     ###Task 
    
# # import pandas as pd

# # df = pd.DataFrame({
# #     "Marks": [85, 45, 70, 30]
# # })

# # df["Level"] = df["Marks"].apply(lambda x: "High" if x >= 50 else "Low")

# # print(df)



# # ################Handling Miassing DAta

# # import pandas as pd
# # df = pd.DataFrame(['a': [1,2,None],{'b':[4,None,6]}])
# # print(df.isnull())





# # ##############GroupBy

# # import pandas as pd
# # sales = pd.DataFrame({'dept':['it','it','hr','hr'],
# #                       'sales': [100, 159, 23, 42]})
# # print(sales.groupby('dept')['sales'].)



# # ##############Task



# # import pandas as pd

# # df = pd.DataFrame({
# #     "Product": ["Phone", "Laptop", "Shirt", "Tablet", "Jeans"],
# #     "Category": ["Electronics", "Electronics", "Clothes", "Electronics", "Clothes"],
# #     "Price": [50000, 80000, 3000, 40000, 5000]
# # })

# # print(df.groupby("Category")["Price"].mean())

# # print(df.groupby("Category").count())




# ####Merging and Concatenation

# import pandas as pd

# df1 = pd.DataFrame({
#     "ID": [1, 2, 3],
#     "Name": ["Ali", "Ahmed", "Sara"]
# })
# df2 = pd.DataFrame({
#     "ID": [2, 3, 4],
#     "Marks": [80, 90, 70]
# })

# # left = pd.merge(df1, df2, on="ID", how="left")
# # print(left)

# inner = pd.merge(df1, df2, on="ID", how="inner")
# print(inner)


# combined = pd.concat([df1, df2], ignore_index=True)

# print(combined)





###Prectice 
###Pandas Series

import pandas as pd
a =[1, 7, 2]
data = pd.Series(a)
print(data)


##DataFrames 
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
