import numpy as np
import plotly.express as px
import pycountry
import pandas as pd
import plotly.graph_objects as go


############### Get the identify code for replacing dots with flags later
iso3_to_iso2 = {c.alpha_3: c.alpha_2 for c in pycountry.countries}

df = px.data.gapminder().query("year==2002")
df["iso_alpha2"] = df["iso_alpha"].map(iso3_to_iso2)
df = df[["country", "iso_alpha", "iso_num", "iso_alpha2"]]
df = df.rename(columns={"country": "Entity"})


## Load data and Make a copy
fertilty_data = pd.read_csv("final_dataset_ALL.csv")
fertilty_data = fertilty_data[
    ["Entity", "Year", "Continent", "Population", "Birth_rate"]
]

## only use data in 2019
fertilty_data = fertilty_data.loc[fertilty_data["Year"] == 2019]

## Load HDI
HDI_data = pd.read_csv("HDI2019.csv")
HDI_data = HDI_data.rename(columns={"Country": "Entity"})

## Merge DFs
merge = pd.merge(fertilty_data, HDI_data, on="Entity")
merge = pd.merge(merge, df, on="Entity")
df = merge


######################## Make plot  #####################################################
## Basic polt
fig = px.scatter(
    df,
    x="Birth_rate",
    y="HDI",
    hover_name="Entity",
    size="Population",
    hover_data=["Birth_rate", "HDI", "Population"],
)
fig.update_traces(marker_color="rgba(0,0,0,0)")


##################### Add vertical lines
avg1 = np.mean(df[df["Birth_rate"] <= 10].HDI)
avg2 = np.mean(df[df["Birth_rate"] > 10].HDI)

fig.add_hline(
    y=avg1,
    line_width=5,
    line_dash="dot",
    line_color="#77969A",
    annotation_text="Average HDI for low birth rate countries",
    annotation_position="bottom right",
    annotation=dict(font_size=15, font_family="Courier"),
    layer="below",
)

fig.add_hline(
    y=avg2,
    line_width=5,
    line_dash="dot",
    line_color="#77969A",
    annotation_text="Average HDI for other countries",
    annotation_position="bottom right",
    annotation=dict(font_size=15, font_family="Courier"),
    layer="below",
)

fig.add_hline(
    y=0.737,
    line_width=5,
    line_dash="dot",
    line_color="#7DB9DE",
    annotation_text="World HDI",
    annotation_position="bottom right",
    annotation=dict(font_size=15, font_family="Courier",),
    layer="below",
)

### Add green range represents low rate countries
fig.add_vrect(
    x0=5, x1=10, fillcolor="#69b3a2", opacity=0.5, line_width=0, layer="below"
)

fig.add_annotation(
    x=7.5,
    y=0.63,
    xref="x",
    yref="y",
    text="Low Birth <br> Rate Range  ",
    showarrow=True,
    font=dict(family="Courier", size=18, color="#4A593D"),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#69b3a2",
    ax=0,
    ay=0,
    # bordercolor="#69b3a2",
    borderwidth=2,
    borderpad=4,
    # bgcolor="#69b3a2",
    opacity=0.8,
)


############### Add Flag icon
minDim = df[["Birth_rate", "HDI"]].max().idxmax()
maxi = df[minDim].max()

for i, row in df.iterrows():
    country_iso = row["iso_alpha2"]
    fig.add_layout_image(
        dict(
            source=f"https://raw.githubusercontent.com/matahombres/CSS-Country-Flags-Rounded/master/flags/{country_iso}.png",
            xref="x",
            yref="y",
            xanchor="center",
            yanchor="middle",
            x=row["Birth_rate"],
            y=row["HDI"],
            sizex=np.sqrt(row["Population"] / df["Population"].max()) * maxi * 0.05
            + maxi * 0.02,
            sizey=np.sqrt(row["Population"] / df["Population"].max()) * maxi * 0.05
            + maxi * 0.02,
            sizing="contain",
            opacity=0.8,
            layer="above",
        )
    )

fig.update_layout(plot_bgcolor="white")  # height=800, width=1200,


## Add title and Update axis properties
fig.update_layout(
    title="Figure 7: Birth Rate And Human Development Index (in 2019)",
    xaxis_title="Birth Rate (births per 1,000 people) <br><br> Bubule size represents population. HDI is a summary measure of average achievement in key dimensions of <br> human development: a long and healthy life, being knowledgeable and have a decent standard of living.",
    yaxis_title="Human Development Index",
    legend_title="Legend Title",
    font=dict(family="Courier", size=12, color="black"),
    title_font_size=20,
)
fig.update_layout(title_x=0.5)

############################ Add size legend
# fig.update_layout(legend= {'itemsizing': 'constant'})
# fig.update_layout(showlegend=True)

fig.write_html("figure7_birth_rate_HDI_bubble_chart.html")
