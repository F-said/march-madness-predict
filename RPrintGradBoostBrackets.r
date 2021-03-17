# Script pulled from user "utresearch" https://www.kaggle.com/utresearch/visualize-your-predictions
suppressWarnings(suppressMessages(library(tidyverse)))
suppressWarnings(suppressMessages(install.packages("devtools")))
suppressWarnings(suppressMessages(devtools::install_github("dhutexas/collegehoops", dep = TRUE)))
library(collegehoops)

options(repr.plot.width = 14, repr.plot.height = 8)
# parse bracket - moving forward predicted winning teams

bracket = collegehoops::parse_bracket("predictions/submission_seedordinal_gb.csv", year = '2021')
# print the bracket
collegehoops::print_bracket(bracket, font_size = 0.7)
