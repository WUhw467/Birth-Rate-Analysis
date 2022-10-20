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

# birth rate histgram

data1["range"] = ""
data1["Birth_rate"] = pd.to_numeric(data1["Birth_rate"], downcast="float")
for i in range(len(data1)):
    if data1.iloc[i, 1] < 10:
        data1.range[i] = "0-10"
    elif data1.iloc[i, 1] >= 10 and data1.iloc[i, 1] < 20:
        data1.range[i] = "10-20"
    elif data1.iloc[i, 1] >= 20 and data1.iloc[i, 1] < 30:
        data1.range[i] = "20-30"
    else:
        data1.range[i] = ">30"

df2 = data1.groupby("range")["Entity"].count().reset_index(name="counts")

fig = px.bar(
    df2,
    x="range",
    y="counts",
    labels={
        "range": "Births Per 1000 People<br>counts the number of countries with different birth rates",
        "counts": "Counts",
    },
    title="Figure 2: Birth Rate Distribution",
)
fig.update_layout(title_x=0.5, title_font_family="Courier", title_font_size=15)
fig.update_layout(font=dict(family="Courier", size=10))
fig.write_html("figure2_histogram_counts_country_from_different_range.html")
