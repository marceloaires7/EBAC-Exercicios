import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def renda_countplot(x, data, ax, title=''):
    sns.countplot(x=x,
                  data=data,
                  ax=ax,)
    ax.set_title(title)
    ax.tick_params(axis='x',
                   rotation=45)

def renda_lineplot(x, y, hue, data, ax, title=''):
    sns.lineplot(x=x,
                 y=y,
                 hue=hue,
                 data=data,
                 ax=ax)
    ax.set_title(title)
    ax.tick_params(axis='x',
                   rotation=45)
    
def renda_barplot(x, y, data, ax, title=''):
    sns.barplot(x=x,
                y=y,
                data=data,
                ax=ax)
    ax.set_title(title)
    ax.tick_params(axis='x',
                   rotation=45)