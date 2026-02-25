import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#To Load file in python
cafeteria = pd.read_csv("D:/DA-SQL/Mini Projects/Python mini Project/Cafeteria_csv.file-project.csv")
#print (cafeteria.info())
#print (cafeteria.describe())
#print (cafeteria.to_string())
#print (cafeteria.isnull().sum()) # To find the missing values 
#print (cafeteria.isnull().sum()/len(cafeteria)*100)# To find the missing values in percentage
#print (cafeteria.shape)
#print (cafeteria.duplicated())
#print (cafeteria['Transaction ID'].value_counts().head(10))
# to find the unique values in categorical columns
for col in cafeteria.columns:
    if cafeteria[col].nunique()< 20:
        print (cafeteria[col].value_counts())
        print ('_'*50)
# Handling the missing,Errors and Unknown data in categorical columns
cafeteria ['Item'] = cafeteria['Item'].replace (['UNKNOWN','ERROR'],np.nan)
cafeteria ['Item'] = cafeteria['Item'].replace ("",np.nan)
cafeteria ['Item'] = cafeteria ['Item'].fillna("No_Data")
# Handling the missing,Errors and Unknown data in categorical columns
cafeteria ['Payment Method'] = cafeteria ['Payment Method'].replace (['UNKNOWN','ERROR'],np.nan)
cafeteria ['Payment Method'] = cafeteria ['Payment Method'].replace ("",np.nan)
cafeteria ['Payment Method'] = cafeteria ['Payment Method'].fillna("No_Data")
# Handling the missing,Errors and Unknown data in categorical columns
cafeteria ['Location'] = cafeteria ['Location'].replace (['UNKNOWN','ERROR'],np.nan)
cafeteria ['Location'] = cafeteria ['Location'].replace ("",np.nan)
cafeteria ['Location'] = cafeteria ['Location'].fillna ("No_Data")
# Handling the missing,Errors and Unknown data in Numerical columns
cafeteria ['Quantity'] =pd.to_numeric(cafeteria ['Quantity'],errors = 'coerce')
median = cafeteria ['Quantity'].median()
cafeteria ['Quantity'].fillna(median,inplace = True)
# Handling the missing,Errors and Unknown data in Price Per Unit columns
cafeteria ['Price Per Unit ($)'] = pd.to_numeric (cafeteria ['Price Per Unit ($)'],errors = 'coerce')
cafeteria ['Price Per Unit ($)'].fillna(median,inplace =True)
# Handling the missing,Errors and Unknown data in Total Spent columns
cafeteria ['Total Spent ($)'] = pd.to_numeric (cafeteria ['Total Spent ($)'],errors = 'coerce')
cafeteria ['Total Spent ($)'].fillna(median, inplace = True)
# Recalucalating the missing and invalid values in Total Spent columns
cafeteria ['Total Spent ($)'] = cafeteria ['Total Spent ($)'].fillna (cafeteria ['Quantity']*cafeteria ['Price Per Unit ($)'])
# cahnge the date format in Transaction Date column
cafeteria ['Transaction Date'] = cafeteria ['Transaction Date'].replace(['UNKNOWN','ERROR',""],np.nan)
cafeteria ['Transaction Date'] = pd.to_datetime(cafeteria['Transaction Date'],errors  = 'coerce')
median_date = cafeteria ['Transaction Date'].median()
median_date = cafeteria ['Transaction Date'].fillna(median_date, inplace = True)
cafeteria ['Transaction Date'] = cafeteria ['Transaction Date'].dt.strftime("%d-%m-%y")
cafeteria.to_csv("Cafeteria_Cleaned_data.csv",index = False)                                                                     
#print (cafeteria.isnull().sum())
#print (cafeteria.info())
#find the Correlation between the Qantity and Total_spend
corr_matrix = cafeteria['Quantity'].corr(cafeteria['Total Spent ($)']).round (2)
corr_matrix_price = cafeteria['Quantity'].corr(cafeteria['Price Per Unit ($)']).round (2)
corr_matirx_spent = cafeteria ['Price Per Unit ($)'].corr(cafeteria['Total Spent ($)']).round (2)
#print (corr_matrix)
#print (corr_matrix_price)
#print (corr_matirx_spent)
#correlation between Quantity Vs Total Spent
plt.figure(figsize = (6,4))
plt.scatter(cafeteria['Quantity'],cafeteria['Total Spent ($)'],color = 'blue',s= 50)
plt.xlabel("Quantity",fontsize = 12,fontweight='bold')
plt.ylabel('Total Spent ($)',fontsize = 12, fontweight = 'bold')
plt.title("Quantity Vs Total Spent")
plt.grid(axis ='y',alpha =0.3)
plt.show()
#correaltion between Quantity Vs Price Per Unit ($)      
plt.figure(figsize = (6,4))
plt.scatter(cafeteria['Quantity'],cafeteria['Price Per Unit ($)'],color ='Green', s= 50)
plt.xlabel("Quantity",fontsize = 12,fontweight='bold')
plt.ylabel('Price Per Unit ($)',fontsize = 12, fontweight = 'bold')
plt.title("Quantity Vs Price Per Unit ($)")
plt.grid(axis ='y',alpha =0.3)
plt.show()
#correlation between Price Per Unit ($) Vs Total Spent ($)
plt.figure(figsize = (6,4))
plt.scatter(cafeteria['Price Per Unit ($)'],cafeteria['Total Spent ($)'],color ='red',s=50)
plt.xlabel('Price Per Unit ($)',fontsize = 12,fontweight='bold')
plt.ylabel('Total Spent ($)',fontsize = 12, fontweight = 'bold')
plt.title("Price Per Unit ($) Vs Total Spent ($)")
plt.grid(axis ='y',alpha =0.3)
plt.show()

#Best Selling Item in cafeteria
Best_selling = cafeteria.groupby('Item')['Total Spent ($)'].sum().sort_values(ascending = False)
plt.figure(figsize = (6,4))
bars = plt.bar(Best_selling.index, Best_selling.values)
plt.title("Best_Selling_Item",fontsize = 18,fontweight = 'bold')
plt.xlabel('Item',fontsize = 8,fontweight = 'bold')
plt.ylabel('Total Spent ($)',fontsize =8,fontweight = 'bold')
plt.xticks(rotation =45)
# add bar values
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x()+bar.get_width()/2,
        height,
        str(height),
        ha = 'center',
        va = 'bottom',
        fontsize = 8
    )        
plt.tight_layout()
plt.show()
#Location wise revenue
Revenue_by_Location =cafeteria.groupby('Location')['Total Spent ($)'].sum().sort_values(ascending = True)
plt.figure(figsize =(6,4))
bars = plt.bar(Revenue_by_Location.index,Revenue_by_Location.values)
plt.xlabel("Location",fontsize = 12,fontweight = 'bold')
plt.ylabel("Total Spent ($)",fontsize = 12,fontweight = 'bold')
plt.title("Loaction wise Cafeteria Revenue",fontsize = 12,fontweight = 'bold')
plt.xticks (rotation = 45)
# adding lables
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x()+bar.get_width()/2,
        height,
        str(height),
        ha = 'center',
        va = 'bottom',
        fontsize = 8
    )
plt.show()
#Payment method
Payment_Mode = cafeteria.groupby("Payment Method")["Total Spent ($)"].sum().sort_values(ascending = True)
plt.figure(figsize= (6,4))
bars = plt.bar(Payment_Mode.index,Payment_Mode.values)
plt.xlabel("Item",fontsize = 12)
plt.ylabel("Payment Method",fontsize = 12)
# adding the values
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x()+bar.get_width()/2,
        height,
        str(height),
        ha = 'center',
        va = 'bottom',
        fontsize = 8
    )
plt.show()
























