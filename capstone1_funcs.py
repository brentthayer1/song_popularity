import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

def select_columns(df, columns):
    return df[columns]

def drop_duplicates(df):
    '''
    Drops any duplicate values in the dataframe

    Input- df (pd.DataFrame)
    Output- df (pd.DataFrame)
    '''
    df.drop_duplicates(inplace=True)
    return df

def time_ms_to_sec(df):
    '''
    Converts milliseconds to second.
    Removes millisecond column and returns
    the dataframe with a new time_seconds
    column.

    Input- df (pd.DataFrame)
    Output- df (pd.DataFrame)
    '''

    df['time_seconds'] = df['duration_ms']//1000
    df.drop('duration_ms', axis=1, inplace=True)
    pop = df.pop('time_seconds')
    df.insert(3, 'time_seconds', pop)

def drop_columns(df, cols):
    df.drop(cols, axis=1, inplace=True)

def check_for_nans(df, cols):
    '''
    Returns the number of NaNs for each specified column
    in a dataframe

    Inputs- df (pd.DataFrame), cols (list of columns)
    Output- List of NaNs for each column
    '''
    for col in cols:
        print(f'NaNs in {col}:', df['acousticness'].isnull().sum())



def plot_hists(axs, dfs, names, col, color_list):
    for ax, df_, name, colr in zip(axs, dfs, names, color_list):
        ax.hist(df_[col], bins=70, color=colr)
        ax.set_title(name)










if __name__ == '__main__':

    file_path = '/Volumes/b/Galvanize/DS-RFT4/capstones-RFT4/datasets/music2/test1.csv'

    df = pd.read_csv(file_path)
    cols = ['artist_name', 'popularity', 'tempo']
    
    print(scatter_plot(df, df['popularity'], df['tempo']))
