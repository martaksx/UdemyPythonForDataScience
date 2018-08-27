
# coding: utf-8

# In[ ]:


#Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

#PROFIT
profit = []

for i in range(0,len(revenue)):
    profit.append(round(revenue[i] - expenses[i],2))
profit

tax = [round(i *0.3,2) for i in profit]
tax

profit_after_tax = []
for i in range(0,len(profit)):
    profit_after_tax.append(round(profit[i]-tax[i],2))
profit_after_tax

profit_margin = []
for i in range(0,len(profit_after_tax)):
    profit_margin.append(round((profit_after_tax[i]/revenue[i])*100,2))
profit_margin

from statistics import mean
profit_at_mean = round(mean(profit_after_tax),2)
profit_at_mean

good_months = []
for i in range(0,len(profit_after_tax)):
    good_months.append(profit_after_tax[i]>profit_at_mean)
good_months

bad_months = []
for i in range(0,len(profit_after_tax)):
    bad_months.append(profit_after_tax[i]<profit_at_mean)
bad_months

best_month = max(profit_after_tax)
best_month

#The Best Month Is Where Profit After Tax Was Equal To The Maximum
best_month2 = []
for i in range (0, len(profit_after_tax)):
    best_month2.append(profit_after_tax[i] == max(profit_after_tax))
best_month2

worst_month = min(profit_after_tax)
worst_month

#The Worst Month Is Where Profit After Tax Was Equal To The Minimum
worst_month2 = []
for i in range (0, len(profit_after_tax)):
    worst_month2.append(profit_after_tax[i] == min(profit_after_tax))
worst_month2

#Convert All Calculations To Units Of One Thousand Dollars
revenue_1000 = [round(i/1000, 2) for i in revenue]
expenses_1000 = [round(i/1000, 2) for i in expenses]
profit_1000 = [round(i/1000, 2) for i in profit]
profit_after_tax_1000 = [round(i/1000, 0) for i in profit_after_tax]

#Print Results
print ("Revenue :") 
print (revenue_1000)
print ("Expenses :") 
print (expenses_1000)
print ("Profit :")
print(profit_1000)
print ("Profit after tax :")
print (profit_after_tax_1000)
print ("Profit margin :")
print (profit_margin)
print ("Good months :")
print (good_months)
print ("Bad months :")
print (bad_months)
print ("Best month :")
print (best_month)
print ("Worst month :")
print (worst_month)

