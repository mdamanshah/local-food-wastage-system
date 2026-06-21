import pandas as pd
import matplotlib.pyplot as plt

claims = pd.read_csv("data/claims_data.csv")

claims['Status'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title('Claims Status Percentage')
plt.ylabel('')

plt.savefig("chart15_claims_percentage.png")
plt.show()