# #Question 1
#
# import pandas as pd
# df1 = pd.read_excel("Data_Sales_Rep.xlsx")
# df2 = pd.read_excel("Data_Sales_units.xlsx")
# print("------------------------------Data_Sales_Rep---------------------------")
# print(df1)
# print("------------------------------Data_Sales_Units---------------------------")
# print(df2)
# #
# #Question 2
#
# import pandas as pd
# df1 = pd.read_excel("Data_Sales_Rep.xlsx")
# df2 = pd.read_excel("Data_Sales_units.xlsx")
# print("-------------------Header of Data_Sales_Rep-----------------")
# print(" || ".join(df1.iloc[0:0].columns.tolist()))
# print("-------------------Header of Data_Sales_Units-----------------")
# print(" || ".join(df2.iloc[0:0].columns.tolist()))
# print("--------------------First 10 data of Data_Sales_Rep------------------")
# print(df1.head(10))
# print("-------------------First 10 data of Data_Sales_Units-----------------")
# print(df2.head(10))
#
# #Question 3
#
# import pandas as pd
#
# df1 = pd.read_excel("Data_Sales_Rep.xlsx")
# df2 = pd.read_excel("Data_Sales_units.xlsx")
# print("-------------------Datatype of Data_Sales_Rep-----------------")
# print(df1.dtypes)
# print("-------------------Datatype of Data_Sales_Units-----------------")
# print(df2.dtypes)
#
# #Question 4
# import pandas as pd
# file = pd.read_excel("Data_Sales_Rep.xlsx")
# fp = pd.read_excel("Data_Sales_units.xlsx")
# combine = pd.merge(file, fp, on=["OrderDate", "Rep"])
# combine['OrderDate'] = pd.to_datetime(combine['OrderDate']).dt.date
# print("-----------------------First 10 rows of combied output dataframe------------------------")
# print(combine.head(10))
# # combine.to_excel("Output_Sales_Data.xlsx", index=False) {Excel file already created}
#
# #Question 5
#
# import pandas as pd
# file = pd.read_excel("Output_Sales_Data.xlsx")
# print("---------------------10 random row data from output dataframe--------------------")
# print(file.sample(10))
#
# #Question 6
#
# import pandas as pd
# def fx(uc):
#     if uc < 100:
#         rem = uc*0.10
#         uc += rem
#         return uc
#     else:
#         rem = uc*0.20
#         uc += rem
#         return uc
#
# file = pd.read_excel("Output_Sales_Data.xlsx")
# file["new Total"] = file["Unit Cost"].apply(fx) * file["Units"]
# file["new Total"] = file["new Total"].round(2)
# file['OrderDate'] = pd.to_datetime(file['OrderDate']).dt.date
# maximum = file.loc[file["new Total"].idxmax()]
# max_value = maximum["new Total"]
# rep_name = maximum["Rep"]
# print("Highest new total: ", max_value)
# print("Rep Name: ", rep_name)
# # file.to_excel("Updated_Sales_Data.xlsx", index=False) {Excel file already created}
#
# #Question 7
#
# import pandas as pd
# file = pd.read_excel("Updated_Sales_Data.xlsx")
# region = file.groupby("Region")["new Total"].sum()
# print("--------------------------Sales of each region-------------------------")
# print(region)
#
# #Question 8
#
# import pandas as pd
# file = pd.read_excel("Updated_Sales_Data.xlsx")
# sort_date = file.sort_values(by='OrderDate', ascending=False)
# sort_date['OrderDate'] = pd.to_datetime(sort_date['OrderDate']).dt.date
# # sort_date.to_excel("Sorted_Sales_Data.xlsx", index=False)  {Excel file already created}
#
# #Question 9
#
# import pandas as pd
# file = pd.read_excel("Sorted_Sales_Data.xlsx")
# maximum = file.loc[file["new Total"].idxmax()]
# max_value = maximum["new Total"]
# rep_name = maximum["Rep"]
# file.loc[file["Rep"] == rep_name, "new Total"] += 100
# file['OrderDate'] = pd.to_datetime(file['OrderDate']).dt.date
# # file.to_excel("Bonus_Sales_data.xlsx", index=False)  {Excel file already created}
#
# #Question 10
#
# import pandas as pd
# file = pd.read_excel("Bonus_Sales_data.xlsx")
# file['OrderDate'] = pd.to_datetime(file['OrderDate']).dt.date
# # file.to_excel("Sales_data_new.xlsx", index=False)  {Excel file already created}
#
# #Question 11
#
# import pandas as pd
# file = pd.read_excel("Sales_Data_new.xlsx")
# extra = file.sample(n=9956, replace = True)
# extend = pd.concat([file, extra], ignore_index=True)
# extend['OrderDate'] = pd.to_datetime(extend['OrderDate']).dt.date
# # extend.to_excel("Extended_Sales_File.xlsx", index=False)  {Excel file already created}
#
