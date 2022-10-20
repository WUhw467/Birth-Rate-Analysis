# Load the packages
library(tidyverse)
library(highcharter)
library(htmlwidgets)

# Load the data
data <- read.csv("final_dataset_ALL.csv", header = T)

# Filter out the countries with birth rate less than 10 in 2019
data4 <- data
data4 <- data4[data4$Entity %in%
  data4$Entity[data4$Year == 2019 & data4$Birth_rate < 10], ]

# Assign a color to every unique entity
data4$Color[data4$Entity == "Austria"] <- "#D04945"
data4$Color[data4$Entity == "Bosnia and Herzegovina"] <- "#489966"
data4$Color[data4$Entity == "Bulgaria"] <- "#23313A"
data4$Color[data4$Entity == "Channel Islands"] <- "#322D75"
data4$Color[data4$Entity == "Croatia"] <- "#D53F5D"
data4$Color[data4$Entity == "Cuba"] <- "#932951"
data4$Color[data4$Entity == "Finland"] <- "#357DC4"
data4$Color[data4$Entity == "Germany"] <- "#73A9E1"
data4$Color[data4$Entity == "Greece"] <- "#F9D25D"
data4$Color[data4$Entity == "Hungary"] <- "#FBDE67"
data4$Color[data4$Entity == "Italy"] <- "#93B2DB"
data4$Color[data4$Entity == "Japan"] <- "#8E1C32"
data4$Color[data4$Entity == "Malta"] <- "#2F5E38"
data4$Color[data4$Entity == "Moldova"] <- "#225887"
data4$Color[data4$Entity == "Poland"] <- "#224471"
data4$Color[data4$Entity == "Portugal"] <- "#3A84C9"
data4$Color[data4$Entity == "Puerto Rico"] <- "#4296D6"
data4$Color[data4$Entity == "Qatar"] <- "#EC4768"
data4$Color[data4$Entity == "Romania"] <- "#EE804A"
data4$Color[data4$Entity == "Singapore"] <- "#23313A"
data4$Color[data4$Entity == "Slovenia"] <- "#8469B3"
data4$Color[data4$Entity == "South Korea"] <- "#112028"
data4$Color[data4$Entity == "Spain"] <- "#D53F5D"
data4$Color[data4$Entity == "Ukraine"] <- "#224471"

# Create a data frame with entity name and color for the outer ring
donutBase <-
  data4 %>%
  select(Entity, Color) %>%
  distinct(Entity, Color) %>%
  mutate(
    primary_color = Color
  )

# Create a schooling years summary for each entity
SchoolingSummary_df <-
  data4 %>%
  group_by(Entity) %>%
  filter(is.na(Mean_years_of_schooling) == FALSE) %>%
  ungroup()

# Create a DF with tooltip chart nested list
donutList <-
  donutBase %>%
  select(Entity, primary_color) %>%
  inner_join(SchoolingSummary_df) %>%
  nest(-Entity, -primary_color) %>%
  mutate(
    sSummary =
      data %>%
        map(mutate_mapping, hcaes(x = Year, y = Mean_years_of_schooling), drop = TRUE) %>%
        map(list_parse)
  ) %>%
  select(-data) %>%
  mutate(segment = 1)

# Create the plot of an outer ring with an interactive tooltip inside
hchart(
  donutList,
  "pie",
  hcaes(name = Entity, y = segment, color = primary_color),
  innerSize = 500
) %>%
  hc_tooltip(
    useHTML = TRUE,
    headerFormat = "<b>{point.key}</b>",
    pointFormatter =
      tooltip_chart(
        accesor = "sSummary",
        hc_opts = list(
          chart = list(type = "line"),
          yAxis = list(
            # set limits
            # min = 0.4, max = 0.75,
            title = list(
              text = "Mean years of schooling",
              color = "rgba(0, 0, 0, 1.0)"
            )
          ),
          xAxis = list(title = list(
            text = "Year",
            color = "rgba(0, 0, 0, 1.0)"
          )),
          height = 325,
          width = 475
        )
      ),
    # Javascript positioner to center tooltip inside pie chart
    positioner = JS(
      "function () {
      xp =  this.chart.chartWidth/2 - this.label.width/2
      yp =  this.chart.chartHeight/2 - this.label.height/2
      return { x: xp, y: yp };
    }"
    ),
    # animation settings
    shadow = FALSE,
    borderWidth = 0,
    backgroundColor = "transparent",
    hideDelay = 1000
  ) %>%
  hc_size(height = 750) %>%
  hc_title(text = "Figure 6: The Change in Education Level from 1960 to 2010") %>%
  hc_subtitle(text = "Country breakdowns with low birth rate (< 10) in 2019") %>%
  hc_caption(text = "<br>The mean years of schooling in the countries with low birth rates
             all show an increasing trend from 1960 to 2010.</br>") %>%
  hc_add_theme(hc_theme(
    chart = list(
      backgroundColor = "white",
      style = list(
        fontFamily = "Courier",
        fontSize = "13.33px"
      )
    ),
    title = list(
      style = list(
        fontWeight = "bold",
        fontSize = "20px"
      ),
      align = "center"
    ),
    subtitle = list(
      style = list(
        fontWeight = "bold",
        fontSize = "14px",
        color = "black"
      ),
      align = "center"
    ),
    caption = list(
      style = list(
        fontFamily = "Courier",
        fontSize = "13.33px",
        color = "black"
      ),
      align = "center"
    )
    # yAxis = list(style = list(fontSize = '16px'))
  ))
