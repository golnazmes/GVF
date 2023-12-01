import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_two_scales(data1, data2, feature_name):
    fig, ax1 = plt.subplots()

    t = np.arange(len(data1))
    assert len(data1) == len(data2)
    color = "tab:red"
    ax1.set_xlabel("time (s)")
    ax1.set_ylabel("cumulant", color=color)
    ax1.plot(t, data1, color=color)
    ax1.tick_params(axis="y", labelcolor=color)

    ax2 = ax1.twinx()
    color = "tab:blue"
    ax2.set_ylabel("return", color=color)
    ax2.plot(t, data2, color=color)
    ax2.tick_params(axis="y", labelcolor=color)
    plt.title(feature_name)

    fig.tight_layout()
    plt.savefig(f"{feature_name}_discounted_return.png")


def calculate_discounted_return_backward(feature_values, gamma):
    # Gt=Rt+γGt+1
    discounted_return = np.zeros(len(feature_values))
    discounted_return[-1] = feature_values[-1]
    for i in range(len(feature_values) - 2, 0, -1):
        discounted_return[i] = feature_values[i] + gamma * discounted_return[i + 1]
    return discounted_return


if __name__ == "__main__":
    df = pd.read_csv("train.csv")
    for feature_name in df.columns:
        feature_values = df[feature_name].values[:800]

        discounted_return = calculate_discounted_return_backward(feature_values, 0.90)
        print(feature_values[-1], discounted_return[-1])
        plot_two_scales(feature_values, discounted_return, feature_name)
