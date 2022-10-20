# Load the packages
library(tidyverse)
library(plotly)
library(GGally)

# Load the data
data <- read.csv("final_dataset_ALL.csv", header = T)

# Data pre-processing
## select data in 2019 and filter out variables with null values
data1 <- data %>%
  filter(Year == 2019) %>%
  select(
    Entity, Labor_force_participation_rate, GDP_per_capita,
    Under_five_mortality, Birth_rate
  )
## create a categorical variable representing birth rate level
data1$Birth_rate_level[data1$Birth_rate < 10] <- "low (<10)"
data1$Birth_rate_level[data1$Birth_rate >= 10] <- "normal (>=10)"
data1$Birth_rate_level <- as.factor(data1$Birth_rate_level)
## omit the null values
data1 <- na.omit(data1)
## rename the variables
names(data1) <- c(
  "Entity", "Labor.Force.Participation", "GDP.Per.Capita",
  "Under.Five.Mortality", "Birth.Rate", "Birth.Rate.Level"
)

# Make parallel coordinate plot
p <- ggparcoord(data1,
  columns = 2:5,
  groupColumn = 6,
  order = "anyClass",
  scale = "uniminmax",
  showPoints = TRUE,
  title = "Figure 3: Parallel Coordinate Plot of The Variables (in 2019)",
  alphaLines = 0.3,
  boxplot = TRUE
) +
  scale_colour_manual("Birth Rate Level", values = c("#69b3a2", "#E8E8E8")) +
  theme(
    # legend.position = "right",
    panel.background = element_rect(fill = "white"),
    panel.grid.major = element_line(colour = "#E8E8E8", size = 0.5),
    panel.grid.minor = element_line(colour = "#E8E8E8", size = 0.5),
    text = element_text(family = "Courier"),
    plot.title = element_text(size = 15, face = "plain", hjust = 0.5),
    legend.title = element_text(size = 10),
    legend.text = element_text(size = 10),
    axis.title = element_text(size = 10),
    axis.text = element_text(size = 10)
  ) +
  scale_x_discrete(labels = c(
    "Birth.Rate" = "Birth Rate",
    "GDP.Per.Capita" = "GDP Per Capita",
    "Under.Five.Mortality" = "Under Five Mortality",
    "Labor.Force.Participation" = "Labor Force Participation"
  )) +
  labs(
    x = "",
    y = "Standardized Values (Min = 0 and Max = 1)"
  )

# Make the plot interactive using Plotly
ggplotly(p) %>%
  layout(
    margin = list(b = 130, t = 100),
    annotations =
      list(
        x = 0.5, y = -0.15,
        text = "GDP Per Capita is negatively associated with Birth Rate and Under Five Mortality Rate.
                Countries with a low level of birth rate tend to have a relatively high GDP and a low under five mortality rate level.",
        showarrow = F, xref = "paper", yref = "paper",
        xanchor = "auto", yanchor = "auto", xshift = 0, yshift = 0,
        font = list(size = 13, family = "Courier")
      )
  )
