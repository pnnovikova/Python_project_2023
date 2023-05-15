import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def barh_plot(data, ylim, title='', xlabel='', ylabel='', figsize=(9, 5)):
    _, ax = plt.subplots(figsize=figsize)
    bars = data.plot(kind='bar', width=0.8, ec='black')
    for container in bars.containers:
        bars.bar_label(container, label_type='edge', padding=5, rotation=0, color='black')
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.ylim(*ylim)
    plt.show()


def corr_heatmap(corr_data, igsize=(10, 10)):
    plt.figure(figsize=figsize)
    sns.heatmap(
        corr_data,
        cmap='coolwarm',
        square=True,
        annot=True,
        vmin=-1,
        cbar_kws={'shrink':0.7}
    )
    plt.show()
