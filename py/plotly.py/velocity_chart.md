# Jira Velocity Chart

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
If I have a CSV file exported from Jira, could you recommend any python library that I can create a HTML file and show Velocity Chart like Jira?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
## Recommended Python Libraries for a Jira Velocity Chart 📊

The best tools for this task are a combination of two powerful Python libraries: **Pandas** for data manipulation and a plotting library like **Plotly** or **Altair** for visualization and HTML export.

***

### 1. Data Processing with Pandas
The first step is to use the **Pandas** library to read your exported Jira CSV file. Pandas is the industry standard for data manipulation in Python and is perfect for this job.

* **Read the Data:** You can load the CSV file directly into a `DataFrame`, which is a flexible table-like data structure.
* **Calculate Velocity:** You can then process the `DataFrame` to group issues by sprint and calculate key metrics, such as the total story points committed at the start of the sprint and the total story points completed at the end. 
* **Data Cleaning:** Pandas also makes it easy to handle missing data or non-numeric values that might be in your CSV file, ensuring your calculations are accurate.

***

### 2. Plotting and HTML Export with Plotly or Altair
While libraries like Matplotlib can create static images, **Plotly** and **Altair** are excellent choices for this task because they can generate interactive charts as standalone HTML files.

* **Interactive Charts:** These libraries allow users to hover over data points to see specific values, zoom in on a particular sprint, and even hide or show different data series (e.g., committed vs. completed story points).
* **HTML Output:** You can save the chart directly to a single HTML file. This file can then be shared with anyone—no Python installation is needed to view the chart!
* **Chart Type:** A velocity chart is typically a combination chart, with bars representing the committed and completed story points for each sprint and a line representing the average velocity. Plotly and Altair handle this type of chart composition with ease.

### Putting It All Together: A High-Level Workflow
Here's a general outline of the steps you would follow to achieve your goal:

1.  **Read the CSV:** Load your Jira CSV file into a Pandas `DataFrame` using `pd.read_csv()`.
2.  **Pre-process Data:** Clean the data, extract sprint names or IDs, and convert story point columns to numeric types.
3.  **Calculate Velocity Metrics:** Group the `DataFrame` by sprint to calculate committed and completed story points for each.
4.  **Create the Chart:** Use Plotly or Altair to create a chart based on your calculated data.
5.  **Export to HTML:** Save the final chart as an interactive HTML file.
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me an Altair example to generate interactive charts like Velocity Chart?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

Yes, here is a complete Python code example that uses the **Altair** library to generate an interactive Velocity Chart. The code creates a layered chart with bars for committed and completed story points and a line for the completed points, which represents velocity.

This code will create a file named `velocity_chart.html` in your current directory. You can open this file in any web browser to view and interact with the chart.

-----

### Example Altair Code

```python
import pandas as pd
import altair as alt

# Sample data for a Velocity Chart
# In a real-world scenario, you would load your Jira CSV file here
data = {
    'sprint': ['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4', 'Sprint 5'],
    'committed_points': [30, 45, 40, 50, 60],
    'completed_points': [25, 40, 35, 48, 55]
}
df = pd.DataFrame(data)

# To create a grouped bar chart, we need to melt the DataFrame
# This reshapes the data to have a 'Metric' column (committed/completed)
df_melt = df.melt('sprint', var_name='Metric', value_name='Story Points')

# Create the stacked bar chart for committed and completed points
# This chart uses the melted DataFrame
bar_chart = alt.Chart(df_melt).mark_bar(opacity=0.7).encode(
    x=alt.X('sprint:N', axis=alt.Axis(title='Sprint')),
    y=alt.Y('Story Points:Q', title='Story Points'),
    color=alt.Color('Metric:N', legend=alt.Legend(title="Metric")),
    tooltip=[
        alt.Tooltip('sprint', title='Sprint'),
        alt.Tooltip('Metric', title='Metric'),
        alt.Tooltip('Story Points', title='Story Points')
    ]
).properties(
    title='Agile Team Velocity Chart'
)

# Create the line chart for Velocity
# This chart uses the original DataFrame
line_chart = alt.Chart(df).mark_line(
    color='green',
    strokeDash=[5, 5],
    point=True  # Adds a point to each data marker
).encode(
    x=alt.X('sprint:N'),
    y=alt.Y('completed_points:Q', axis=alt.Axis(title='Completed Story Points')),
    tooltip=[
        alt.Tooltip('sprint', title='Sprint'),
        alt.Tooltip('completed_points', title='Completed Story Points')
    ]
)

# Layer the charts on top of each other and save as an HTML file
# The resolve_scale() function allows each chart to have its own independent y-axis
chart = alt.layer(bar_chart, line_chart).resolve_scale(y='independent')
chart.save('velocity_chart.html')

print("Velocity chart saved as velocity_chart.html")
```

</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
can it be 2 bar per sprint? e.g. 1 bar for committed points, 1 bar for completed and line chart for say/do ratio (i.e. completed divided by committed )
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

Yes, you can create a chart with two bars per sprint and a line chart for the Say/Do ratio. This requires creating three separate charts and then combining them.

The code below first calculates the new **Say/Do ratio** (`Completed Points` / `Committed Points`). It then creates a bar chart for committed points, a second bar chart for completed points, and a line chart for the ratio.

-----

### Example Altair Code

```python
import pandas as pd
import altair as alt

# Sample data
data = {
    'sprint': ['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4', 'Sprint 5'],
    'committed_points': [30, 45, 40, 50, 60],
    'completed_points': [25, 40, 35, 48, 55]
}
df = pd.DataFrame(data)

# Calculate the new metric: Say/Do Ratio
df['say_do_ratio'] = df['completed_points'] / df['committed_points']

# Create the bar chart for committed points
committed_bar = alt.Chart(df).mark_bar(
    color='#50a4f5'  # Use a distinct color for committed points
).encode(
    x=alt.X('sprint:N', title='Sprint'),
    y=alt.Y('committed_points:Q', title='Story Points'),
    tooltip=[
        alt.Tooltip('sprint', title='Sprint'),
        alt.Tooltip('committed_points', title='Committed Points')
    ]
)

# Create the bar chart for completed points
completed_bar = alt.Chart(df).mark_bar(
    color='#68d09f' # Use a distinct color for completed points
).encode(
    x=alt.X('sprint:N', title='Sprint'),
    y=alt.Y('completed_points:Q', title='Story Points'),
    tooltip=[
        alt.Tooltip('sprint', title='Sprint'),
        alt.Tooltip('completed_points', title='Completed Points')
    ]
)

# Create the line chart for the Say/Do Ratio
line_chart = alt.Chart(df).mark_line(
    color='red',
    point=True
).encode(
    x=alt.X('sprint:N', title='Sprint'),
    y=alt.Y('say_do_ratio:Q', title='Say/Do Ratio', axis=alt.Axis(format=".0%")), # Format as percentage
    tooltip=[
        alt.Tooltip('sprint', title='Sprint'),
        alt.Tooltip('say_do_ratio', title='Say/Do Ratio', format=".0%")
    ]
)

# Combine the charts
# This approach uses concatenation to place the charts side by side
# but does not layer them on the same axis.
final_chart = alt.hconcat(
    alt.layer(committed_bar, completed_bar).properties(title='Committed vs. Completed Story Points'),
    line_chart.properties(title='Say/Do Ratio')
).resolve_scale(y='independent')

# Save the interactive chart as an HTML file
final_chart.save('velocity_say_do_chart_hconcat.html')
```

</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me a Plotly example to generate interactive charts like Velocity Chart?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

Yes, **Plotly** is an excellent choice for creating interactive Velocity Charts. Unlike Altair, which is best for declarative charts, Plotly uses an imperative approach that gives you more control over complex layouts, like charts with multiple Y-axes. This makes it perfect for displaying story points and a ratio on the same graph.

-----

### Plotly Example for a Velocity Chart

This example creates a chart with three distinct elements:

1.  A bar for **Committed Points** per sprint.
2.  A bar for **Completed Points** per sprint.
3.  A line for the **Say/Do Ratio** (Completed / Committed), which uses a separate Y-axis.

The code below uses `plotly.graph_objects` to build the chart, giving you full control over each trace.

```python
import pandas as pd
import plotly.graph_objects as go

# 1. Sample Data
# In a real scenario, you'd load this from your Jira CSV
data = {
    'sprint': ['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4', 'Sprint 5'],
    'committed_points': [30, 45, 40, 50, 60],
    'completed_points': [25, 40, 35, 48, 55]
}
df = pd.DataFrame(data)

# Calculate the Say/Do Ratio
df['say_do_ratio'] = df['completed_points'] / df['committed_points']

# 2. Create the Plotly Figure
fig = go.Figure()

# Add a bar trace for Committed Points
fig.add_trace(go.Bar(
    x=df['sprint'],
    y=df['committed_points'],
    name='Committed Points',
    marker_color='#50a4f5'
))

# Add a bar trace for Completed Points
fig.add_trace(go.Bar(
    x=df['sprint'],
    y=df['completed_points'],
    name='Completed Points',
    marker_color='#68d09f'
))

# Add a line trace for the Say/Do Ratio on a secondary y-axis
fig.add_trace(go.Scatter(
    x=df['sprint'],
    y=df['say_do_ratio'],
    name='Say/Do Ratio',
    mode='lines+markers',
    marker=dict(color='red'),
    yaxis='y2' # Assign this trace to the second y-axis
))

# 3. Configure the layout for dual axes
fig.update_layout(
    title_text='Agile Team Velocity & Say/Do Ratio',
    barmode='group',
    xaxis_title='Sprint',
    yaxis_title='Story Points',
    yaxis2=dict(
        title='Say/Do Ratio',
        overlaying='y',
        side='right',
        tickformat='.0%',
        showgrid=False
    ),
    hovermode='x unified', # Enable a unified tooltip for all traces
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

# 4. Save the chart as an HTML file
fig.write_html("plotly_velocity_chart.html")

print("Plotly chart saved as plotly_velocity_chart.html")
```

</td></tr>
</table>