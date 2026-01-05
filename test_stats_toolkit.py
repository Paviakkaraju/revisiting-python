from stats_toolkit import mean, median, mode
data = [7, 7, 4, 5, 5,6,3, 1, 7]

mean_val = mean(data)
median_val = median(data)
mode_val = mode(data)

print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Mode: {mode_val}")