import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd


def organize_boxes(data):
    H_Box = []
    P_Box = []
    G_Box = []
    D_Box = []

    for plant in data:
        if plant['Group ID'] == 'H':
            H_Box.append(plant)
        elif plant['Group ID'] == 'P':
            P_Box.append(plant)
        elif plant['Group ID'] == 'G':
            G_Box.append(plant)
        elif plant['Group ID'] == 'D':
            D_Box.append(plant)

    return H_Box, P_Box, G_Box, D_Box


y_array = [0.742, 0.622, 0.537, 0.465]
x_array = [48, 242, 299, 484]
y_error = [0.011, 0.048, 0.112, 0.078]

plt.errorbar(x_array, y_array, yerr=y_error, marker='o', capsize=4, color='red')
plt.show()

slope, intercept = np.polyfit(x_array, y_array, 1, rcond=None, full=False, w=None, cov=False)
print(slope)
print(intercept)

plt.errorbar(x_array, y_array, yerr=y_error, marker='o', capsize=4, color='red')
plt.show()


y_array = [0.757, 0.618, 0.627, 0.414]
x_array = [48, 242, 299, 484]
y_error = [0.021, 0.066, 0.057, 0.021]

slope, intercept = np.polyfit(x_array, y_array, 1, rcond=None, full=False, w=None, cov=False)
print(slope)
print(intercept)

lc_array = [10, 20, 50, 100, 300, 500]
NPQ_array = [1, 2, 3, 4, 5]

lc_cols = ['LC_1', 'LC_2', 'LC_3', 'LC_4', 'LC_5', 'LC_6']
npq_cols = ['NPQ_1', 'NPQ_2', 'NPQ_3', 'NPQ_4', 'NPQ_Lss']
file_name = r"C:\Users\wolf1\OneDrive\Documents\GitHub\PHYS4130-S26\Emma Krebs\Research Project\Photo.csv"

# Maybe make this a function to call on for certain lines in the code
with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Skip the first line of data describing the columns' data
    next(csv_reader)
    data_array = []

    # Cycle through lines
    for line in csv_reader:
        data = {
            'Day': line[0],
            'Group ID': line[1],
            'Plant ID': line[2],
            'NPQ_1': float(line[3]),
            'NPQ_2': float(line[4]),
            'NPQ_3': float(line[5]),
            'NPQ_4': float(line[6]),
            'NPQ_Lss': float(line[7]),
            'LC_1': float(line[8]),
            'LC_2': float(line[9]),
            'LC_3': float(line[10]),
            'LC_4': float(line[11]),
            'LC_5': float(line[12]),
            'LC_6': float(line[13])
        }
        data_array.append(data)

    df_raw = pd.DataFrame(data_array)

    print(f"\n--- Raw Data Day  ---")
    print(df_raw.to_string(index=False))
    df_raw.to_csv('data_raw.csv', index=False)

    H, P, G, D = organize_boxes(data_array)
    groups = {'10%': H, '100%': P, '50%': G, 'Misc': D}

    plt.figure(figsize=(8, 5))

for treatment, group in groups.items():
    df = pd.DataFrame(group)

    means = df[lc_cols].mean()
    stds = df[lc_cols].std()

    plt.errorbar(
        lc_array,
        means,
        yerr=stds,
        marker='o',
        capsize=4,
        label=treatment
    )

plt.xlabel("PAR / Light Curve Step")
plt.ylabel("Quantum Yield")
plt.title("Average PSII Quantum Yield Light Curve by Treatment")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

for treatment, group in groups.items():
    df = pd.DataFrame(group)

    means = df[npq_cols].mean()
    stds = df[npq_cols].std()

    plt.errorbar(
        NPQ_array,
        means,
        yerr=stds,
        marker='o',
        capsize=4,
        label=treatment
    )

plt.xlabel("NPQ Step")
plt.ylabel("NPQ")
plt.title("Average NPQ Response by Treatment")
plt.legend()
plt.tight_layout()
plt.show()


treatments = []
means = []
stds = []

for treatment, group in groups.items():
    df = pd.DataFrame(group)

    treatments.append(treatment)
    means.append(df['NPQ_Lss'].mean())
    stds.append(df['NPQ_Lss'].std())

plt.figure(figsize=(7, 5))
plt.bar(treatments, means, yerr=stds, capsize=5)

plt.xlabel("Treatment")
plt.ylabel("Mean NPQ_Lss")
plt.title("Final NPQ by Treatment")
plt.tight_layout()
plt.show()

treatments = []
means = []
stds = []

for treatment, group in groups.items():
    df = pd.DataFrame(group)

    treatments.append(treatment)
    means.append(df['LC_6'].mean())
    stds.append(df['LC_6'].std())

plt.figure(figsize=(7, 5))
plt.bar(treatments, means, yerr=stds, capsize=5)

plt.xlabel("Treatment")
plt.ylabel("Mean Final Quantum Yield")
plt.title("Final Quantum Yield by Treatment")
plt.tight_layout()
plt.show()

df = pd.DataFrame(data_array)

# Rename columns for clarity
df = df.rename(columns={
    'Group ID': 'Treatment',
    'Plant ID': 'Species'
})

# Map treatment labels
df['Treatment'] = df['Treatment'].map({
    'H': '10%',
    'G': '50%',
    'D': 'Misc',
    'P': '100%'
})

print(df.head())

model = ols('NPQ_Lss ~ C(Treatment) + C(Species) + C(Treatment):C(Species)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print("\n--- ANOVA: NPQ_Lss ---")
print(anova_table)

model = ols('LC_1 ~ C(Treatment) + C(Species) + C(Treatment):C(Species)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print("\n--- ANOVA: LC_1 ---")
print(anova_table)

tukey = pairwise_tukeyhsd(
    endog=df['NPQ_Lss'],
    groups=df['Treatment'],
    alpha=0.05
)

print(tukey)

