import csv
import numpy as np
import matplotlib.pyplot as plt

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


files = [r"C:\Users\wolf1\OneDrive\Documents\GitHub\PHYS4130-S26\Emma Krebs\Research Project\Day_1.csv",
         r"C:\Users\wolf1\OneDrive\Documents\GitHub\PHYS4130-S26\Emma Krebs\Research Project\Day_2.csv",
         r"C:\Users\wolf1\OneDrive\Documents\GitHub\PHYS4130-S26\Emma Krebs\Research Project\Day_3.csv",
         r"C:\Users\wolf1\OneDrive\Documents\GitHub\PHYS4130-S26\Emma Krebs\Research Project\Day_4.csv"]
day = 1
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

    H, P, G, D = organize_boxes(data_array)

    fig, ax = plt.subplots()

    # Plot the basil first then the tomatoes 

    x_Hb, y_Hb = extract_xy(H, "Basil")
    x_Ht, y_Ht = extract_xy(H, "Tomato")

    plt.scatter(x_Hb, y_Hb, marker='o', color='red', label='10% Basil')
    plt.scatter(x_Ht, y_Ht, marker='x', color='red', label='10% Tomato')

    x_Pb, y_Pb = extract_xy(P, "Basil")
    x_Pt, y_Pt = extract_xy(P, "Tomato")

    plt.scatter(x_Pb, y_Pb, marker='o', color='blue', label='100% Basil')
    plt.scatter(x_Pt, y_Pt, marker='x', color='blue', label='100% Tomato')

    x_Gb, y_Gb = extract_xy(G, "Basil")
    x_Gt, y_Gt = extract_xy(G, "Tomato")

    plt.scatter(x_Gb, y_Gb, marker='o', color='green', label='50% Basil')
    plt.scatter(x_Gt, y_Gt, marker='x', color='green', label='50% Tomato')

    x_Db, y_Db = extract_xy(D, "Basil")
    x_Dt, y_Dt = extract_xy(D, "Tomato")

    plt.scatter(x_Db, y_Db, marker='o', color='purple', label='Misc. Basil')
    plt.scatter(x_Dt, y_Dt, marker='x', color='purple', label='Misc Tomato')
    

    plt.legend()
    plt.xlabel("QY Dark-adapted")
    plt.ylabel("QY Light Adapted")
    plt.xlim(0.5, 0.85)
    plt.ylim(0.35, 0.85)
    plt.title(f"Photosystem II Efficency Day {day}")
    
    plt.show()

    day += 1
