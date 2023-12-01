import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 10})

# Read the train.csv file
df = pd.read_csv("train.csv")

#make a directory for plots
import os
if not os.path.exists('plots'):
    os.makedirs('plots')

# show feature names
print(list(df.columns))


#plt.tight_layout()

def plot_feature(feature):
    plt.figsize=(10, 5)
    plt.clf()   
    plt.plot(df[feature][:800])
    plt.ylabel(feature)
    plt.xlabel("time step")
    plt.savefig(f"plots/{feature}.png")
    plt.clf()

def plot_breath(breath_id):
    fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(10, 10))
    feature_names = list(df.columns)
    feature_names.remove("breath_id")
    feature_names.remove("id")
    feature_names.remove("time_step")
    for i, feature in enumerate(feature_names):
        axes[i].plot(df[df["breath_id"] == breath_id][feature])
        axes[i].set_ylabel(feature)
        axes[i].set_xlabel("time")

    plt.savefig(f"plots/breath_id_{breath_id}.png")
    plt.clf()


def plot_multiple_breaths(breath_id_start, breath_id_end):
    fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(10, 10))
    # plot all breaths in one plot, with a vertical line seperteing each breath
    feature_names = list(df.columns)
    feature_names.remove("breath_id")
    feature_names.remove("id")
    feature_names.remove("time_step")

    for i, feature in enumerate(feature_names):
        axes[i].plot(
            df[df["breath_id"] >= breath_id_start][df["breath_id"] <= breath_id_end][
                feature
            ]
        )
        x = len(
            df[df["breath_id"] >= breath_id_start][df["breath_id"] <= breath_id_end][
                feature
            ]
        )
        space = len(
            df[df["breath_id"] >= breath_id_start][
                df["breath_id"] <= breath_id_start + 1
            ][feature]
        )
        for x in range(0, x, space):
            axes[i].axvline(x=x, color="red")
        axes[i].set_ylabel(feature)
    plt.savefig(f"plots/breath_id_{breath_id_start}_to_{breath_id_end}.png")
    plt.clf()

#plot_feature("pressure")
#plot_breath(1)

#plot_multiple_breaths(0, 10)

#count how many breath_ids of 1 there are
print(df[df["breath_id"] == 2]["breath_id"].count())

#count how many ids are there
print(df["id"].count())

#count the number of unique breath_ids
print(df["breath_id"].nunique())

