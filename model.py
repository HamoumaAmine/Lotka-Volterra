
def lotka_volterra(lapin_initial, renard_initial, alpha, beta, delta, gamma, step, num_lapins_renards):
   
    lapin = [lapin_initial]
    renard = [renard_initial]
    time = [0]
    
    for _ in range(0, num_lapins_renards):
        new_time = time[-1] + step
        new_lapins = (lapin[-1] * (alpha - beta * renard[-1])) * step + lapin[-1]
        new_renards = (renard[-1] * (delta * lapin[-1] - gamma)) * step + renard[-1]
        
        time.append(new_time)
        lapin.append(new_lapins)
        renard.append(new_renards)
    return time, lapin, renard
