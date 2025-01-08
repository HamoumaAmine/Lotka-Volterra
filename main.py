import pandas as pd
import numpy as np
from model import lotka_volterra
from utils import calculate_mse, grid_search
from visualization import plot_population_evolution, plot_real_data

def main():
    # Paramètres initiaux
    num_lapins_renards = 100_000
    lapin_initial = 1
    renard_initial = 2
    alpha, beta, delta, gamma = 1, 1, 1, 1
    step = 0.001

    # Simulation initiale
    time, lapin, renard = lotka_volterra(
        lapin_initial, renard_initial, 
        alpha, beta, delta, gamma, 
        step, num_lapins_renards
    )
    
    # Mise à l'échelle
    lapin_scaled = np.array(lapin) *1000
    renard_scaled = np.array(renard) * 1000

    # Chargement des données réelles
    df = pd.read_csv("populations_lapins_renards.csv")
    lapin_df = df["lapin"].values
    renard_df = df["renard"].values
    temps_reel = df["date"].values
    
    # Calcul du MSE initial
    num_observations = len(df)
    lapin_scaled_truncated = lapin_scaled[:num_observations]
    renard_scaled_truncated = renard_scaled[:num_observations]
    
    lapin_mse = calculate_mse(lapin_scaled_truncated, lapin_df)
    renard_mse = calculate_mse(renard_scaled_truncated, renard_df)
    print(f"MSE initial pour les lapins : {lapin_mse}")
    print(f"MSE initial pour les renards : {renard_mse}")
    
    best_parameters, best_mse = grid_search(lapin_df, renard_df)
    print("Meilleurs paramètres trouvés : ", best_parameters)
    print("MSE minimal trouvé : ", best_mse)
    
    plot_population_evolution(time, lapin_scaled, renard_scaled)
    plot_real_data(lapin_df, renard_df)
if __name__ == "__main__":
    main()
