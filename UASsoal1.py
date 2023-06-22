import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Walmart = pd.read_csv('walmart.csv')
# print(Walmart)

print('1.b')
data_store_4 = Walmart[Walmart['Store'] == 4]

mean_s = data_store_4['Weekly_Sales'].mean()
mean_h = data_store_4['Holiday_Flag'].mean()
mean_t = data_store_4['Temperature'].mean()
mean_f = data_store_4['Fuel_Price'].mean()
mean_c = data_store_4['CPI'].mean()
mean_u = data_store_4['Unemployment'].mean()

median_s = data_store_4['Weekly_Sales'].median()
median_h = data_store_4['Holiday_Flag'].median()
median_t = data_store_4['Temperature'].median()
median_f = data_store_4['Fuel_Price'].median()
median_c = data_store_4['CPI'].median()
median_u = data_store_4['Unemployment'].median()

std_s = data_store_4['Weekly_Sales'].std()
std_h = data_store_4['Holiday_Flag'].std()
std_t = data_store_4['Temperature'].std()
std_f = data_store_4['Fuel_Price'].std()
std_c = data_store_4['CPI'].std()
std_u = data_store_4['Unemployment'].std()

variance_s = data_store_4['Weekly_Sales'].var()
variance_h = data_store_4['Holiday_Flag'].var()
variance_t = data_store_4['Temperature'].var()
variance_f = data_store_4['Fuel_Price'].var()
variance_c = data_store_4['CPI'].var()
variance_u = data_store_4['Unemployment'].var()

print("Mean Weekly_Sales:", mean_s)
print("Median Weekly_Sales:", median_s)
print("Simpangan Baku Weekly_Sales:", std_s)
print("Varians Weekly_Sales:", variance_s, "\n")

print("Mean Holiday_Flag:", mean_h)
print("Median Holiday_Flag:", median_h)
print("Simpangan Baku Holiday_Flag:", std_h)
print("Varians Holiday_Flag:", variance_h, "\n")

print("Mean Temperature:", mean_t)
print("Median Temperature:", median_t)
print("Simpangan Baku Temperature:", std_t)
print("Varians Temperature:", variance_t, "\n")

print("Mean Fuel_Price:", mean_f)
print("Median Fuel_Price:", median_f)
print("Simpangan Baku Fuel_Price:", std_f)
print("Varians Fuel_Price:", variance_f, "\n")

print("Mean CPI:", mean_c)
print("Median CPI:", median_c)
print("Simpangan Baku CPI:", std_c)
print("Varians CPI:", variance_c, "\n")

print("Mean Unemployment:", mean_u)
print("Median Unemployment:", median_u)
print("Simpangan Baku Unemployment:", std_u)
print("Varians Unemployment:", variance_u, "\n")


print('1.c')
fuel_price_q1 = data_store_4['Fuel_Price'].quantile(0.25)
fuel_price_q2 = data_store_4['Fuel_Price'].quantile(0.50)
fuel_price_q3 = data_store_4['Fuel_Price'].quantile(0.75)
fuel_price_iqr = fuel_price_q3 - fuel_price_q1

cpi_q1 = data_store_4['CPI'].quantile(0.25)
cpi_q2 = data_store_4['CPI'].quantile(0.50)
cpi_q3 = data_store_4['CPI'].quantile(0.75)
cpi_iqr = cpi_q3 - cpi_q1

unemployment_q1 = data_store_4['Unemployment'].quantile(0.25)
unemployment_q2 = data_store_4['Unemployment'].quantile(0.50)
unemployment_q3 = data_store_4['Unemployment'].quantile(0.75)
unemployment_iqr = unemployment_q3 - unemployment_q1

print("Fuel Price:")
print("Q1:", fuel_price_q1)
print("Q2:", fuel_price_q2)
print("Q3:", fuel_price_q3)
print("IQR:", fuel_price_iqr)

print("Customer Price Index:")
print("Q1:", cpi_q1)
print("Q2:", cpi_q2)
print("Q3:", cpi_q3)
print("IQR:", cpi_iqr)

print("Unemployment:")
print("Q1:", unemployment_q1)
print("Q2:", unemployment_q2)
print("Q3:", unemployment_q3)
print("IQR:", unemployment_iqr)

print('1.d')
grouped_data = Walmart.groupby('Holiday_Flag')['Weekly_Sales'].var()
print("Variance Description:")
for flag, variance in grouped_data.items():
    if flag == 1:
        print("Holiday Week:")
    else:
        print("Non-Holiday Week:")
    print("Variance:", variance)
    print()

print('1e')
average_sales_by_store = Walmart.groupby('Store')['Weekly_Sales'].mean()
is_average_sales_equal = average_sales_by_store.nunique() == 1
if is_average_sales_equal:
    print("Rata-rata Weekly Sales di setiap toko sama.")
else:
    print("Rata-rata Weekly Sales di setiap toko berbeda.")

print('1f')
max_cpi_by_store = Walmart.groupby('Store')['CPI'].max()
higher_cpi_by_store = max_cpi_by_store.idxmax()
higher_cpi_value = max_cpi_by_store.max()

print("CPI yang lebih tinggi di setiap toko:")
for store_id in max_cpi_by_store.index:
    cpi_value = max_cpi_by_store.loc[store_id]
    print("Store ID:", store_id)
    print("CPI:", cpi_value)
    print()

print('1g')
average_cpi_holiday = Walmart[Walmart['Holiday_Flag'] == 1]['CPI'].mean()
average_cpi_non_holiday = Walmart[Walmart['Holiday_Flag'] == 0]['CPI'].mean()
if average_cpi_holiday > average_cpi_non_holiday:
    print("Rata-rata CPI pada holiday week lebih tinggi.")
elif average_cpi_holiday < average_cpi_non_holiday:
    print("Rata-rata CPI pada non-holiday week lebih tinggi.")
else:
    print("Rata-rata CPI pada holiday week dan non-holiday week sama.")