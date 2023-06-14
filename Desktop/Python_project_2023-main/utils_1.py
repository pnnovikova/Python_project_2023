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

import numpy as np
def corr_heatmap(corr_data, figsize=(10, 10)):
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


def dist_manh_plot(data, y_col, log=False, ylabel='', mask=None, mask_name=''):
    plt.figure(figsize=(10, 4))
    y = data[y_col].copy()
    x = data['dist_manhattan'].copy()
    if log:
        y = np.log1p(y)
    if mask is not None:
        x = x[mask]
        y = y[mask]
    s = sns.scatterplot(y=y, x=x)
    plt.title(f'{ylabel} в зависимости от удаленности от центра {mask_name}')
    plt.ylabel(ylabel)
    plt.xlabel('Расстояние от района Манхеттен')
    plt.show()