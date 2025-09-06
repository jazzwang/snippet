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