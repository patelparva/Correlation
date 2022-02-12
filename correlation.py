import numpy as np
import csv
import plotly.express as px
import pandas as pd


def get_data_source(data_path):
    second_value = []

    first_value = []
    file_data = []

    with open(data_path, newline='') as f:
        reader = csv.reader(f)
        file_data = list(reader)

    file_data.pop(0)
    for i in file_data:
        first_value.append(float(i[1]))
        second_value.append(float(i[2]))

    return first_value, second_value


def find_correlation(data):
    correlation = np.corrcoef(data['x'], data['y'])

    return correlation[0,1]


def plot_figure(data_path):
    df = pd.read_csv(data_path)

    # df_list=df.tolist()
    x = list(df)[1]
    y = list(df)[2]
    # print(y)

    fig = px.scatter(df, x=x, y=y)
    fig.show()


def main():
    file_path=str(input('Enter the file path whose correlation you want to find. '))

    first_value, second_value = get_data_source(file_path)
    data = {'x': first_value, 'y': second_value}
    # print(data)
    
    correlation = find_correlation(data)
    print('Correlation is {}'.format(correlation))

    plot_figure(file_path)


if __name__ == '__main__':
    main()
