import statistics
import csv
import matplotlib.pyplot as plt


def avg_response_time():
    csv_path = "../response_times.csv"
    with open(csv_path, "r") as f:
        reader = csv.reader(f)
        times = [float(row[0]) for row in reader if row]

    avg_time = sum(times) / len(times)
    std_dev = statistics.stdev(times)

    plt.figure(figsize=(6, 4))
    plt.bar(["Average"], [avg_time], width=0.3, color="#1f77b4")
    plt.ylabel("Seconds")
    plt.title("Average Response Time")
    plt.text(0, avg_time * 0.5, f"{avg_time:.3f}s", ha="center", va="center",
             color="white", fontsize=12, weight="bold")

    # Add whitespace around the bar
    plt.xlim(-1, 1)
    plt.ylim(0, avg_time * 1.3)
    plt.tight_layout(pad=3)
    plt.show()

    print(f"Standard Deviation: {std_dev:.3f}s")

def scatter_plot_response_times():
    csv_path = "../response_times.csv"
    with open(csv_path, "r") as f:
        reader = csv.reader(f)
        times = [float(row[0]) for row in reader if row]

    plt.figure(figsize=(8, 5))
    plt.scatter(range(1, len(times) + 1), times, alpha=0.7)
    plt.xlabel("Request Number")
    plt.ylabel("Response Time (seconds)")
    plt.title("Response Times Scatter Plot")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    scatter_plot_response_times()