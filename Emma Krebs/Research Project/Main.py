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


def extract_xy(group, plant_type):
    x = [p['QY (Dark)'] for p in group if p['Plant Type'] == plant_type]
    y = [p['QY (Light)'] for p in group if p['Plant Type'] == plant_type]
    return x, y

def extract_qy(group, plant_type):
    qy = [p['QY (Light)'] for p in group if p['Plant Type'] == plant_type]
    return np.mean(qy), np.std(qy)


results = {
    '10%': {'Basil': [], 'Tomato': []},
    '100%': {'Basil': [], 'Tomato': []},
    '50%': {'Basil': [], 'Tomato': []},
    'Misc': {'Basil': [], 'Tomato': []}
}

stds = {
    '10%': {'Basil': [], 'Tomato': []},
    '100%': {'Basil': [], 'Tomato': []},
    '50%': {'Basil': [], 'Tomato': []},
    'Misc': {'Basil': [], 'Tomato': []}
}

files = [r"C:\Users\wolf1\OneDrive\Documents\GitHub\PHYS4130-S26\Emma Krebs\Research Project\Day_1.csv",
         r"C:\Users\wolf1\OneDrive\Documents\GitHub\PHYS4130-S26\Emma Krebs\Research Project\Day_2.csv",
         r"C:\Users\wolf1\OneDrive\Documents\GitHub\PHYS4130-S26\Emma Krebs\Research Project\Day_3.csv",
         r"C:\Users\wolf1\OneDrive\Documents\GitHub\PHYS4130-S26\Emma Krebs\Research Project\Day_4.csv"]

date = ['4/19', '4/22', '4/25', '4/28']
days = [0, 3, 6, 9]
day = 0
for file_name in files:

    # Maybe make this a function to call on for certain lines in the code
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skip the first line of data describing the columns' data
        next(csv_reader)
        data_array = []

        # Cycle through lines
        for line in csv_reader:
            data = {
                'Group ID': line[0],
                'Plant Type': line[1],
                'Height': float(line[2]),
                'QY (Dark)': float(line[3]),
                'QY (Light)': float(line[4])
            }
            data_array.append(data)

        df_raw = pd.DataFrame(data_array)

        print(f"\n--- Raw Data Day {date[day]} ---")
        print(df_raw.to_string(index=False))
        df_raw.to_csv('data_raw.csv', index=False)

        H, P, G, D = organize_boxes(data_array)
        groups = {'10%': H, '100%': P, '50%': G, 'Misc': D}

        # Store averages for this day
        for key, group in groups.items():
            mean_b, std_b = extract_qy(group, "Basil")
            mean_t, std_t = extract_qy(group, "Tomato")

            results[key]['Basil'].append(mean_b)
            results[key]['Tomato'].append(mean_t)

            stds[key]['Basil'].append(std_b)
            stds[key]['Tomato'].append(std_t)

    fig, ax = plt.subplots()

    # Plot the basil first then the tomatoes 

    x_Hb, y_Hb = extract_xy(H, "Basil")
    x_Ht, y_Ht = extract_xy(H, "Tomato")

    plt.scatter(x_Hb, y_Hb, marker='o', color='green', label='10% Basil', s=18)
    plt.scatter(x_Ht, y_Ht, marker='o', color='red', label='10% Tomato', s=18)

    x_Pb, y_Pb = extract_xy(P, "Basil")
    x_Pt, y_Pt = extract_xy(P, "Tomato")

    plt.scatter(x_Pb, y_Pb, marker='x', color='green', label='100% Basil', s=18)
    plt.scatter(x_Pt, y_Pt, marker='x', color='red', label='100% Tomato', s=18)

    x_Gb, y_Gb = extract_xy(G, "Basil")
    x_Gt, y_Gt = extract_xy(G, "Tomato")

    plt.scatter(x_Gb, y_Gb, marker='*', color='green', label='50% Basil', s=18)
    plt.scatter(x_Gt, y_Gt, marker='*', color='red', label='50% Tomato', s=18)

    x_Db, y_Db = extract_xy(D, "Basil")
    x_Dt, y_Dt = extract_xy(D, "Tomato")

    plt.scatter(x_Db, y_Db, marker='v', color='green', label='Misc. Basil', s=18)
    plt.scatter(x_Dt, y_Dt, marker='v', color='red', label='Misc Tomato', s=18)
    
    plt.legend()
    plt.xlabel("QY Dark-adapted")
    plt.ylabel("QY Light Adapted")
    plt.xlim(0.6, 0.85)
    plt.ylim(0.35, 0.85)
    plt.title(f"Photosystem II Efficency Day {date[day]}")
    
    plt.show()

    day += 1


for key in results:
    plt.errorbar(
        days,
        results[key]['Basil'],
        yerr=stds[key]['Basil'],
        marker='o',
        capsize=4,
        label=key
    )


plt.xlabel("Day")
plt.ylabel("Light Adapted QY")
plt.title("Basil PSII Quantum Yield")
plt.legend()

plt.ylim(0, 0.9)

plt.show()

for key in results:
    plt.errorbar(
        days,
        results[key]['Tomato'],
        yerr=stds[key]['Tomato'],
        marker='o',
        capsize=4,
        label=key
    )


plt.xlabel("Day")
plt.ylabel("Light Adapted QY")
plt.title("Tomato PSII Quantum Yield")
plt.legend()

plt.ylim(0, 0.9)

plt.show()  

# -------------- Table for all Mean and STD ----------------

table_data = []

for key in results:

    for i in range(len(date)):

        table_data.append({
            'Treatment': key,
            'Date': date[i],

            'Basil Mean QY':
                round(results[key]['Basil'][i], 4),

            'Basil Std':
                round(stds[key]['Basil'][i], 4),

            'Tomato Mean QY':
                round(results[key]['Tomato'][i], 4),

            'Tomato Std':
                round(stds[key]['Tomato'][i], 4)
        })

df = pd.DataFrame(table_data)

print(df.to_string(index=False))
df.to_csv('data_table_raw.csv', index=False)

# --------------- Table for Averaged mean ---------------------------
print()
print()
avg_table = []

for key in results:

    basil_avg = np.mean(results[key]['Basil'][1:])
    tomato_avg = np.mean(results[key]['Tomato'][1:])

    basil_std = np.std(results[key]['Basil'][1:], ddof=1)
    tomato_std = np.std(results[key]['Tomato'][1:], ddof=1)

    avg_table.append({
        'Treatment': key,
        'Basil Avg QY': round(basil_avg, 3),
        'Basil Std': round(basil_std, 3),
        'Tomato Avg QY': round(tomato_avg, 3),
        'Tomato Std': round(tomato_std, 3)
    })

df_avg = pd.DataFrame(avg_table)

print(df_avg.to_string(index=False))

# ----------------- Now Plot Them ------------
order = ['10%', '50%', 'Misc', '100%']

df_avg['Treatment'] = pd.Categorical(
    df_avg['Treatment'],
    categories=order,
    ordered=True
)

df_avg = df_avg.sort_values('Treatment')
intensities = [48, 242, 299, 484]

for key in results:
    plt.errorbar(
        intensities,
        df_avg['Basil Avg QY'],
        yerr=df_avg['Basil Std'],
        marker='o',
        capsize=4,
        color='green'
    )

for key in results:
    plt.errorbar(
        intensities,
        df_avg['Tomato Avg QY'],
        yerr=df_avg['Tomato Std'],
        marker='o',
        capsize=4,
        color='red'
    )


plt.xlabel("Treatment")
plt.ylabel("Avg QY")
plt.title("PSII for Treatments")

plt.ylim(0, 0.9)

plt.show()  

anova_data = []

for key in results:
    for plant in ['Basil', 'Tomato']:
        for value in results[key][plant][1:]:   # Days 2-4 only
            anova_data.append({
                'QY': value,
                'Species': plant,
                'Treatment': key
            })

df_anova = pd.DataFrame(anova_data)

model = ols(
    'QY ~ C(Species) + C(Treatment) + C(Species):C(Treatment)',
    data=df_anova
).fit()

anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)
anova_table.to_csv('anova.csv', index=False)

tukey = pairwise_tukeyhsd(
    endog=df_anova['QY'],
    groups=df_anova['Treatment'],
    alpha=0.05
)

print(tukey)