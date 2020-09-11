
# 1. Meet Dr.Ignaz Semmelweis

# Importing the modules
import pandas as pd 

# Loading the dataset
yearly = pd.read_csv('datasets/yearly_deaths_by_clinic.csv')

# Printing out the data 
yearly


# 2. The alarming numbers of the deaths

# Calculate the proportion of deaths per no. births
yearly["proportion_deaths"] =round((yearly["deaths"]/yearly["births"])*1000)

# Extract clinic 1 data into yearly1 and clinic 2 data into yearly2
yearly1 = yearly[yearly["clinic"] == "clinic 1"]
yearly2 = yearly[yearly["clinic"] == "clinic 2"]

#Printing out the yearly1
yearly1

# 3. Death at the clinics
# This makes plots appear in the notebook
import matplotlib.pyplot as plt
%matplotlib inline
# Plot yearly proportion of deaths at the two clinics
# ... YOUR CODE FOR TASK 3 ...
ax = yearly1.plot(x="year", y="proportion_deaths", label="Clinic 1")
yearly2.plot(x="year", y="proportion_deaths", label="Clinic 2", ax=ax)
ax.set_ylabel("Proportion deaths")


# 4. The handwashing begins
# Read datasets/monthly_deaths.csv into monthly
monthly = pd.read_csv("datasets/monthly_deaths.csv", parse_dates=['date'])

# Calculate proportion of deaths per no. births
# ... YOUR CODE FOR TASK 4 ...
monthly["proportion_deaths"]= round((monthly["deaths"]/monthly["births"])*1000)

# Print out the first rows in monthly
# ... YOUR CODE FOR TASK 4 ...
print(monthly.loc[0])

# 5. The effect of the handwashing

# Plot the monthly proportion of deaths
ax = monthly.plot(x="date",y="proportion_deaths", label="Proportion Deaths")
ax.set_ylabel('Proportion Deaths')


# 6. THe effect of handwashing  highlighted

# Date when handwashing was made mandatory
import pandas as pd
handwashing_start = pd.to_datetime('1847-06-01')

# Split monthly into before and after handwashing_start
before_washing = monthly[monthly["date"] < handwashing_start]
after_washing = monthly[monthly["date"] >= handwashing_start]

# Plot monthly proportion of deaths before and after handwashing
# ... YOUR CODE FOR TASK 6 ...
ax = before_washing.plot(x="date", y="proportion_deaths", label="Before Washing")
after_washing.plot(x="date", y="proportion_deaths", label="After Washing", ax=ax)
ax.set_ylabel('Proportion Deaths')

# 7. More handwashing fewer deaths
# Difference in mean monthly proportion of deaths due to handwashing
before_proportion = before_washing["proportion_deaths"]
after_proportion = after_washing["proportion_deaths"]
mean_diff = before_proportion.mean() - after_proportion.mean()
mean_diff

# 8. A Bootstrap analysis of Semelweis handwashing data
# A bootstrap analysis of the reduction of deaths due to handwashing
boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac=1, replace=True)
    boot_after = after_proportion.sample(frac=1, replace=True)
    boot_mean_diff.append( boot_before.mean()-boot_after.mean() )

# Calculating a 95% confidence interval from boot_mean_diff 
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975])
confidence_interval

# 9. THe fate of Dr.Semmelweis
doctors_should_wash_their_hands = True