from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import pandas as pd
import numpy as np
from bokeh.models import ColumnDataSource, VBox, VBoxForm, HBox
from bokeh.plotting import Figure
from bokeh.models.widgets import Select
from bokeh.io import curdoc

# Load the data and save to a dataframe
red_wine = pd.read_csv('playing_with_outliers/data/winequality-red.csv', sep=';')

# Extract column names
column_names = red_wine.columns
features = column_names[0:-1].tolist()
print(features)

# Select a column for x-axis and y-axis
x_feature = Select(title='Select feature for x-axis', value=features[0], options=features)
y_feature = Select(title='Select feature for y-axis', value=features[0], options=features)
threshold = Select(title='Threshold (stdev from mean):', value='10',
                   options=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])

# Set up plot
source = ColumnDataSource(data=dict(x=[], y=[]))

plot = Figure(plot_width=400, plot_height=400, title='Outliers')
plot.scatter(x='x', y='y', source=source)


# Define outlier function
def outliers(df, threshold):

    column_names = df.columns

    mean_list = df.mean(axis=0).tolist()

    i = 0
    for col in column_names:
        mask = abs(df.loc[:,col] - df.loc[:,col].mean()) > \
               threshold*df.loc[:,col].std()
        # print(mask.index)
        df.loc[mask, col] = mean_list[i]
        i += 1

    return df


# Select values
def select_features():
    x_feature_value = x_feature.value
    y_feature_value = y_feature.value
    threshold_value = threshold.value

    # Load the data and save to a dataframe
    df = pd.read_csv('winequality-red.csv', sep=';')

    subset_dict = {
        x_feature_value+'_x': df.loc[:,x_feature_value],
        y_feature_value+'_y': df.loc[:,y_feature_value]
    }

    df_subset = pd.DataFrame(subset_dict)

    df_outliers_removed = outliers(df_subset, np.float(threshold_value))

    selection_dict = {
        'x': df_outliers_removed[x_feature_value+'_x'],
        'y': df_outliers_removed[y_feature_value+'_y']
    }

    return selection_dict


# Update plot
def update(attr, old, new):

    plot_dict = select_features()

    source.data = plot_dict


# Define controls list
# While server is running, update the values
input_values = [x_feature, y_feature, threshold]
for value in input_values:
    value.on_change('value', update)

inputs = VBox(VBoxForm(*input_values), width=300)

update(None, None, None)  # initial load of the data

curdoc().add_root(HBox(inputs, plot, width=1100))
