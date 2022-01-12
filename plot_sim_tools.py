def update_time(elapsed_time, dt):
    elapsed_time[-1] += dt
    if elapsed_time[-1] >= 60:
        elapsed_time[-2] += elapsed_time[-1] // 60
        elapsed_time[-1] = elapsed_time[-1] % 60
    if elapsed_time[-2] >= 60:
        elapsed_time[-3] += elapsed_time[-2] // 60
        elapsed_time[-2] = elapsed_time[-2] % 60
    if elapsed_time[-3] >= 24:
        elapsed_time[-4] += elapsed_time[-3] // 24
        elapsed_time[-3] = elapsed_time[-3] % 24
    if elapsed_time[-4] >= 365:
        elapsed_time[-5] += elapsed_time[-4] // 365
        elapsed_time[-4] = elapsed_time[-4] % 365

    return elapsed_time
