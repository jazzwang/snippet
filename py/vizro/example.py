import vizro.plotly.express as px
from vizro_ai import VizroAI

vizro_ai = VizroAI()

df = px.data.gapminder()
fig = vizro_ai.plot(df, "describe life expectancy per continent over time")
fig.show()
