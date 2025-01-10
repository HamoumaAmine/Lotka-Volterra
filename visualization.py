# visualization.py
import matplotlib.pyplot as plt

<<<<<<< HEAD
def plot_combined_data(time, lapin_scaled, renard_scaled, lapin_df, renard_df):
    plt.figure(figsize=(12, 8))
    plt.plot(time, lapin_df, 'r--', label="Lapins réels")
    plt.plot(time,  renard_df, 'b--', label="Renards réels")

    plt.plot(range(len(lapin_scaled)), lapin_scaled, label="Lapins simulés", color="red")
    plt.plot(range(len(renard_scaled)), renard_scaled, label="Renards simulés", color="blue")
  
    plt.xlabel("Jours")
    plt.ylabel("Population")
    plt.title("Évolution des populations de lapins et de renards")
=======
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
>>>>>>> 9023ccec4fa95b3e6d638a8098d443fb542175c9
    plt.legend()
    plt.grid(True)
    plt.show()
