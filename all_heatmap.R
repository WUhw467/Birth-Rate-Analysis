# Load the packages
library(tidyverse)
library(plotly)
library(ggcorrplot)

# Load the data
data <- read.csv("final_dataset_ALL.csv", header = T)

# Data pre-processing
## select birth rate and the influencing factors
data3 <- data %>%
  select(
    Labor_force_participation_rate, GDP_per_capita,
    Percentage_of_female_population_age_25_29_with_no_education,
    Under_five_mortality, Contraceptive_prevalence,
    Maternal_mortality_ratio,
    Mean_years_of_schooling, Birth_rate
  )
## filter out null values
data3 <- na.omit(data3)
## rename the variables
colnames(data3)[3] <- "Female_with_no_education(%)"

# Make heat map
## compute a correlation matrix
corr <- round(cor(data3), 1)

## compute a matrix of correlation p-values
p.mat <- cor_pmat(data3)

## visualize the correlation matrix
ggcorrplot(
  corr,
  method = "square",
  hc.order = FALSE,
  type = "upper",
  outline.col = "white",
  # p.mat = p.mat,
  legend.title = "",
  lab = TRUE,
  lab_col = "white",
  colors = c("#5499AF", "#FFFFFF", "#DF3B22")
) +
  theme(
    # legend.position = "right",
    panel.background = element_blank(),
    panel.border = element_blank(),
    axis.line = element_blank(),
    # panel.grid.major = element_line(colour = "#E8E8E8", size = 0.5),
    # panel.grid.minor = element_line(colour = "#E8E8E8", size = 0.5),
    text = element_text(family = "Courier"),
    plot.title = element_text(size = 15, face = "plain", hjust = 0.5),
    legend.text = element_text(size = 10),
    axis.title = element_text(size = 10),
    axis.text.x = element_text(size = 10),
    axis.text.y = element_text(size = 10),
    plot.caption = element_text(size = 10, hjust = 0.5)
  ) +
  scale_y_discrete(
    position = "left",
    labels = c(
      "Birth_rate" = "Birth rate",
      "Mean_years_of_schooling" = "Mean years of schooling",
      "Maternal_mortality_ratio" = "Maternal mortality ratio",
      "Contraceptive_prevalence" = "Contraceptive prevalence",
      "Under_five_mortality" = "Under five mortality",
      "Female_with_no_education(%)" = "Female with no education(%)",
      "GDP_per_capita" = "GDP per capita"
    )
  ) +
  scale_x_discrete(labels = c(
    "Labor_force_participation_rate" = "Labor force participation rate",
    "Mean_years_of_schooling" = "Mean years of schooling",
    "Maternal_mortality_ratio" = "Maternal mortality ratio",
    "Contraceptive_prevalence" = "Contraceptive prevalence",
    "Under_five_mortality" = "Under five mortality",
    "Female_with_no_education(%)" = "Female with no education(%)",
    "GDP_per_capita" = "GDP per capita"
  )) +
  labs(
    title = "Figure 4: Correlation Matrix of All Variables",
    caption = "GDP Per Capita, Percentage of Female with No Education, Under Five Mortality Rate, and Maternal Mortality Ratio have positive
       relationships with Birth Rate. Contraceptive Prevalence and Mean Years of Schooling have negative relationships with Birth Rate."
  )
