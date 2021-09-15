import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.scatter(df, x="Population", y="Per capita", color="Country", title="Per Capita on Country Population", size="Percentage", size_max=40)
fig.show()
