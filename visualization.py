# visualization.py
import matplotlib.pyplot as plt

def plot_population_evolution(time, lapin_scaled, renard_scaled, title="Évolution des populations de lapins et de renards prédites"):
    plt.figure(figsize=(15, 6))
    plt.plot(time, lapin_scaled, "b-", label="Lapins")
    plt.plot(time, renard_scaled, "r-", label="Renards")
    plt.xlabel("Temps")
    plt.ylabel("Population")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()



def plot_real_data(lapin_df, renard_df):
    plt.figure(figsize=(15, 6))
    plt.plot(lapin_df, label='Lapins')
    plt.plot(renard_df, label='Renards')
    plt.xlabel("Temps")
    plt.ylabel("Population")
    plt.title("Évolution des populations de lapins et de renards réelle")
    plt.legend()
    plt.grid(True)
    plt.show()
