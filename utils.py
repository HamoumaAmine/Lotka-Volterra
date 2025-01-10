from model import lotka_volterra
import numpy as np

# mse
def calculate_mse(actual_values, predicted_values):
    num_observations = len(actual_values)
    mse = 0
    for index in range(num_observations):
        mse += ((actual_values[index] - predicted_values[index]) ** 2) / num_observations
    return mse

#grid search
def grid_search(lapin_df, renard_df):
    alpha_values = [1/3, 2/3, 1, 4/3]
    beta_values = [1/3, 2/3, 1, 4/3]
    gamma_values = [1/3, 2/3, 1, 4/3]
    delta_values = [1/3, 2/3, 1, 4/3]
    
    best_parameters = []
    best_mse = 10 ** 10
    
    for a in alpha_values:
        for b in beta_values:
            for d in delta_values:
                for g in gamma_values:
                    time, lapin, renard = lotka_volterra(
                        lapin_initial=1,
                        renard_initial=2,
                        alpha=a,
                        beta=b,
                        delta=d,
                        gamma=g,
                        step=0.001,
                        num_lapins_renards=len(lapin_df)
                    )
                    
                    lapin_scaled = np.array(lapin[:len(lapin_df)]) * 1000
                    renard_scaled = np.array(renard[:len(renard_df)]) * 1000
                    
                    lapin_mse = calculate_mse(lapin_scaled, lapin_df)
                    renard_mse = calculate_mse(renard_scaled, renard_df)
                    mse = lapin_mse + renard_mse
                    
                    if mse < best_mse:
                        best_mse = mse
                        best_parameters = [a, b, d, g]
                        
    return best_parameters, best_mse
