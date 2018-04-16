import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing

# Clean data
data = pd.read_csv("data/train.csv").drop("Name", axis=1).drop("Ticket", axis=1).drop("Cabin", axis=1)

sex_encoded = data[["Sex"]].apply(preprocessing.LabelEncoder().fit_transform)
data[["Sex"]] = sex_encoded
data["Age"] = data["Age"].fillna(data["Age"].mean())


# Plot
survivor_analyse = data["Survived"].value_counts()
labels = 'die', 'alive',

fig = plt.subplot()
fig.pie(survivor_analyse, labels=labels)
plt.show()
