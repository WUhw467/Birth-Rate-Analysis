import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

data1 = pd.read_csv("final_dataset_all.csv")
data1 = data1[data1.Year == 2019]
data1 = data1.iloc[:, [0, -1]].reset_index(drop=True)
data2 = pd.read_csv("country_code_for_map.csv")
data2 = data2.iloc[:, [0, 2]].reset_index(drop=True)
data2 = data2.rename(
    columns={"English short name lower case": "Entity", "Alpha-3 code": "Code"}
)
df = pd.merge(data1, data2, how="inner", on="Entity")


# birth rate map
fig = go.Figure(
    data=go.Choropleth(
        locations=df["Code"],
        z=df["Birth_rate"],
        text=df["Entity"],
        colorscale="blugrn",
        marker_line_color="darkgray",
        marker_line_width=0.5,
        colorbar_title="Births Per 1000 People",
    )
)

fig.update_layout(
    title_text="Figure 1: 2019 Global Birth Rate<br>Figure 1 is a choropleth map of birth rate over the world.<br>The countries are colored based on the actual number of birth rates in 2019 with a sequential color scheme, <br>which means the darker the color the higher the birth rate.",
    title_x=0.5,
    title_font_family="Courier",
    title_font_size=15,
    geo=dict(showframe=False, showcoastlines=False, projection_type="equirectangular"),
)
fig.update_traces(
    colorbar_tickfont_family="Courier",
    colorbar_tickfont_size=10,
    selector=dict(type="choropleth"),
)
fig.update_yaxes(
    title_text="Figure 1 is a choropleth map of birth rate over the world. The countries are colored based on the actual number of birth rates in 2019 with a sequential color scheme, which means the darker the color the higher the birth rate. "
)
fig.write_html("figure1_map_of_global_birth_rate.html")
