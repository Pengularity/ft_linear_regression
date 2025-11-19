import matplotlib.pyplot as plt
from src.linear_regression import load_csv, load_thetas, estimate_price


def main():
    xs, ys = load_csv("data.csv")
    t0, t1 = load_thetas("thetas.json")

    plt.figure()
    plt.scatter(xs, ys, s=12, label="data")

    x_min, x_max = min(xs), max(xs)
    plt.plot([x_min, x_max],
             [estimate_price(x_min, t0, t1),
             estimate_price(x_max, t0, t1)], color="red", label="fit")

    plt.xlabel("mileage (km)")
    plt.ylabel("price")
    plt.title("Linear Regrassion: price ~ mileage")
    plt.legend()
    plt.tight_layout()
    plt.savefig("regression_plot.png", dpi=150)
    print("Saved plot to regression_plot.png")
    plt.show()


if __name__ == "__main__":
    main()
