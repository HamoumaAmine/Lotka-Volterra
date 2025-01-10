import pandas as pd
import numpy as np
from model import lotka_volterra
from utils import calculate_mse, grid_search
from visualization import plot_combined_data

def main():
    
    num_lapins_renards = 100_000
    lapin_initial = 1
    renard_initial = 2
    alpha, beta, delta, gamma = 2/3, 4/3, 1, 1
    step = 0.0003

    time, lapin, renard = lotka_volterra(
        lapin_initial, renard_initial, 
        alpha, beta, delta, gamma, 
        step, num_lapins_renards
    )
    
    # Mise à l'échelle
    time = np.array(time)[:1000]
    lapin_initial = np.array(lapin) *1000
    renard_initial = np.array(renard) * 1000

    lapin_scaled = lapin_initial[::100][:1000] 
    renard_scaled = renard_initial[::100][:1000]
    
    #données réelles
    df = pd.read_csv("populations_lapins_renards.csv")
    df_copy = df.copy()
    df_copy["days"] = range(1, 1001)
    
    lapin_df = df["lapin"].values
    renard_df = df["renard"].values
    
    #mse
    lapin_scaled_truncated = lapin_scaled[:len(df_copy)]
    renard_scaled_truncated = renard_scaled[:len(df_copy)]
    
    lapin_mse = calculate_mse(lapin_scaled_truncated, lapin_df)
    renard_mse = calculate_mse(renard_scaled_truncated, renard_df)
    print(f"MSE initial pour les lapins : {lapin_mse}")
    print(f"MSE initial pour les renards : {renard_mse}")
    
    best_parameters, best_mse = grid_search(lapin_df, renard_df)
    print("Meilleurs paramètres trouvés : ", best_parameters)
    print("MSE minimal trouvé : ", best_mse)
    
    plot_combined_data(df_copy["days"], lapin_scaled, renard_scaled, lapin_df, renard_df)

if __name__ == "__main__":
    main()
