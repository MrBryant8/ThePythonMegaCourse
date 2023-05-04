from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
import pandas 

df['Start'] = pandas.to_datetime(df['Start'], format='%Y-%m-%d %H:%M:%S')
df['End'] = pandas.to_datetime(df['End'], format='%Y-%m-%d %H:%M:%S')

df["Start_string"] = df["Start"].dt.strftime('%Y-%m-%d %H:%M:%S')
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds = ColumnDataSource(df)

p = figure(x_axis_type='datetime', height=190, width=400, title="Motion Graph")
p.yaxis.minor_tick_line_color = None
p.yaxis.ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0, top=1, color="orange", source=cds)

output_file("Graph.html")
show(p)
