# import packages
import altair as alt
import pandas as pd
import numpy as np

# load dataset
df = pd.read_csv("final_dataset_all.csv", parse_dates=["Year"])

# extract low birth rate country in 2019
df_2019 = df[df["Year"] == "2019-01-01"]

low = df_2019[df_2019["Birth_rate"] <= 10]
middle = df_2019[df_2019["Birth_rate"].between(10, 20, inclusive="neither")]
high = df_2019[df_2019["Birth_rate"].between(20, 30, inclusive="both")]
very_high = df_2019[df_2019["Birth_rate"] >= 30]

low_df = df.loc[df["Entity"].isin(low["Entity"])]
middle_df = df.loc[df["Entity"].isin(middle["Entity"])]
high_df = df.loc[df["Entity"].isin(high["Entity"])]
very_high_df = df.loc[df["Entity"].isin(very_high["Entity"])]

# draw interactive linked plot
interval = alt.selection_interval(encodings=["y", "x"])
multi = alt.selection_multi(fields=["Entity"], empty="none")
selector = alt.selection_single(empty="all", fields=["Entity"])

scatter = (
    alt.Chart(low_df)
    .mark_line()
    .encode(
        alt.X("Year", title="Year"),
        alt.Y("Birth_rate:Q", title="Birth_rate(birth per 1000 people)"),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": "Figure 5: Distribution of Global Birth rate",
            "subtitle": [
                "This plot shows the changes of",
                "birth rate from last 60 years",
            ],
        },
    )
    .interactive()
)
hist = (
    alt.Chart(low_df)
    .mark_bar()
    .encode(
        alt.X("Year", title="Year"),
        alt.Y(
            "Labor_force_participation_rate:Q",
            title="Labor force participation rate(%)",
        ),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .transform_filter(selector)
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": ["Figure 5.1: Distribution of Labor force", "participation rate"],
            "subtitle": [
                "This plot shows the changes of",
                "Labor force participation rate from last 60 years",
            ],
        },
    )
    .interactive()
)
hist2 = (
    alt.Chart(low_df)
    .mark_bar()
    .encode(
        alt.X("Year", title="Year"),
        alt.Y("GDP_per_capita:Q", title="GDP_per_capita(dollar)"),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .transform_filter(selector)
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": "Figure 5.2: Distribution of GDP per capita",
            "subtitle": [
                "This plot shows the changes of",
                "GDP per captia from last 60 years",
            ],
        },
    )
    .interactive()
)
hist3 = (
    alt.Chart(low_df)
    .mark_bar()
    .encode(
        alt.X("Year", title="Year"),
        alt.Y(
            "Percentage_of_female_population_age_25_29_with_no_education:Q",
            title="Percentage of female with no education(%)",
        ),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .transform_filter(selector)
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": [
                "Figure 5.3: Distribution of Percentage of",
                "female with no education",
            ],
            "subtitle": [
                "This plot shows the changes of",
                "Percentage of female with no education",
                "from last 60 years",
            ],
        },
    )
    .interactive()
)
hist4 = (
    alt.Chart(low_df)
    .mark_bar()
    .encode(
        alt.X("Year", title="Year"),
        alt.Y("Under_five_mortality:Q", title="Under five mortality rate(%)"),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .transform_filter(selector)
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": ["Figure 5.4: Distribution of Under five mortality", "rate"],
            "subtitle": [
                "This plot shows the changes of",
                "Under five mortality rate from last 60 years",
            ],
        },
    )
    .interactive()
)
hist5 = (
    alt.Chart(low_df)
    .mark_bar()
    .encode(
        alt.X("Year", title="Year"),
        alt.Y("Contraceptive_prevalence:Q", title="Contraceptive prevalence(%)"),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .transform_filter(selector)
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": ["Figure 5.5: Distribution of Contraceptive", "prevalence"],
            "subtitle": [
                "This plot shows the changes of",
                "Contraceptive prevalence rate from last 60 years",
            ],
        },
    )
    .interactive()
)
hist6 = (
    alt.Chart(low_df)
    .mark_bar()
    .encode(
        alt.X("Year", title="Year"),
        alt.Y("Maternal_mortality_ratio:Q", title="Maternal_mortality_ratio(%)"),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .transform_filter(selector)
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": ["Figure 5.6: Distribution of Maternal mortality", "ratio"],
            "subtitle": [
                "This plot shows the changes of",
                "Maternal mortality rate from last 60 years",
            ],
        },
    )
    .interactive()
)
box0 = (
    alt.Chart(low_df)
    .mark_boxplot()
    .encode(
        alt.X("Entity", title="Entity"),
        alt.Y("Birth_rate:Q", title="Birth_rate(birth per 1000 people)"),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .transform_filter(selector)
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": "Figure 5.7: Distribution of Global Birth Rate",
            "subtitle": [
                "This plot shows the boxplot of",
                "birth rate from last 60 years",
            ],
        },
    )
    .interactive()
)
box = (
    alt.Chart(low_df)
    .mark_boxplot()
    .encode(
        alt.X("Entity", title="Entity"),
        alt.Y(
            "Labor_force_participation_rate:Q",
            title="Labor force participation rate(%)",
        ),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .transform_filter(selector)
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": ["Figure 5.8: Distribution of Labor force", "participation rate"],
            "subtitle": [
                "This plot shows the box plot of",
                "Labor force participation rate from last 60 years",
            ],
        },
    )
    .interactive()
)
box2 = (
    alt.Chart(low_df)
    .mark_boxplot()
    .encode(
        alt.X("Entity", title="Entity"),
        alt.Y("GDP_per_capita:Q", title="GDP_per_capita(dollar)"),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .transform_filter(selector)
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": "Figure 5.9: Distribution of GDP per captia",
            "subtitle": [
                "This plot shows the boxplot of",
                "GDP per captia from last 60 years",
            ],
        },
    )
    .interactive()
)
box3 = (
    alt.Chart(low_df)
    .mark_boxplot()
    .encode(
        alt.X("Entity", title="Entity"),
        alt.Y(
            "Percentage_of_female_population_age_25_29_with_no_education:Q",
            title="Percentage of female with no education(%)",
        ),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .transform_filter(selector)
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": [
                "Figure 5.10: Distribution of Percentage of",
                "female with no education",
            ],
            "subtitle": [
                "This plot shows the box plot of",
                "Percentage of female with no education",
                "from last 60 years",
            ],
        },
    )
    .interactive()
)
box4 = (
    alt.Chart(low_df)
    .mark_boxplot()
    .encode(
        alt.X("Entity", title="Entity"),
        alt.Y("Under_five_mortality:Q", title="Under five mortality rate(%)"),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .transform_filter(selector)
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": ["Figure 5.11: Distribution of Under five mortality", "rate"],
            "subtitle": [
                "This plot shows the box plot of",
                "Under five mortalityrate from last 60 years",
            ],
        },
    )
    .interactive()
)
box5 = (
    alt.Chart(low_df)
    .mark_boxplot()
    .encode(
        alt.X("Entity", title="Entity"),
        alt.Y("Contraceptive_prevalence:Q", title="Contraceptive prevalence(%)"),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .transform_filter(selector)
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": ["Figure 5.12: Distribution of Contraceptive", "prevalence"],
            "subtitle": [
                "This plot shows the box plot of",
                "Contraceptive prevalence from last 60 years",
            ],
        },
    )
    .interactive()
)
box6 = (
    alt.Chart(low_df)
    .mark_boxplot()
    .encode(
        alt.X("Entity", title="Entity"),
        alt.Y("Maternal_mortality_ratio:Q", title="Maternal_mortality_ratio(%)"),
        color=alt.condition(selector, "Entity", alt.value("lightgray")),
        tooltip="Entity",
    )
    .transform_filter(selector)
    .properties(
        selection=selector,
        width=500,
        height=300,
        title={
            "text": ["Figure 5.13: Distribution of Maternal mortality", "ratio"],
            "subtitle": [
                "This plot shows the box plot of",
                "Maternal mortality ratio from last 60 years",
            ],
        },
    )
    .interactive()
)
alt.vconcat(
    alt.hconcat(scatter, box0),
    alt.hconcat(hist, box),
    alt.hconcat(hist2, box2),
    alt.hconcat(hist3, box3),
    alt.hconcat(hist4, box4),
    alt.hconcat(hist5, box5),
    alt.hconcat(hist6, box6),
).configure_title(
    fontSize=20, fontWeight="normal", font="Courier", subtitleFont="Courier"
).configure_axis(
    labelFontSize=12, titleFontSize=12, labelFont="Courier", titleFont="Courier"
).configure_legend(
    titleFontSize=10, labelFontSize=10
).save(
    "figure5_linked_plot_between_birth_rate_other_variabes.html"
)
