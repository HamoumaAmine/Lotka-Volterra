import matplotlib.pyplot as plt

def plot_combined_data(time, lapin_scaled, renard_scaled, lapin_df, renard_df):
    plt.figure(figsize=(12, 8))
    plt.plot(time, lapin_df, 'r--', label="Lapins réels")
    plt.plot(time,  renard_df, 'b--', label="Renards réels")

    plt.plot(range(len(lapin_scaled)), lapin_scaled, label="Lapins simulés", color="red")
    plt.plot(range(len(renard_scaled)), renard_scaled, label="Renards simulés", color="blue")
  
    plt.xlabel("Jours")
    plt.ylabel("Population")
    plt.title("Évolution des populations de lapins et de renards")
    plt.show()
