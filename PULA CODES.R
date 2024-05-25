library(readxl)
library(writexl)
library(tidyverse)

# Loading the three datasets
box_placement <- read_excel("D:/Documents/Gilbert/Box_Placement.xlsx")
wet_harvest <- read_excel("D:/Documents/Gilbert/Wet_Harvest.xlsx")
dry_harvest <- read_excel("D:/Documents/Gilbert/Dry_Harvest.xlsx")

#1. Merging the 3 datasets using @case_id
merged_data <- merge(box_placement, wet_harvest, by = "@case_id")
merged_data <- merge(merged_data, dry_harvest, by = "@case_id")

#2. Identifying potential data entry errors:
# Creating filters for potential errors
crazy_box_dimensions <- (merged_data$box_length > 10) | (merged_data$box_width > 10)
false_zero_yields <- (merged_data$wet_weight == 0) & (merged_data$dry_weight > 0)
dry_exceeds_wet <- merged_data$dry_weight > merged_data$wet_weight

# Identifying enumerators with potential errors
suspicious_enumerators <- merged_data[apply(cbind(crazy_box_dimensions, false_zero_yields, dry_exceeds_wet), 1, any), ]

#3. Spatial distribution of data points:
library(leaflet)
# Creating a map using the box placement latitude and longitude
m <- leaflet(merged_data) %>%
  addTiles() %>%
  addMarkers(~latitude, ~longitude)

# Display the map
m

#4. Computing average yield per hectare:
# First, we Convert weights from kg to metric tonnes and calculate yield per hectare
# Compute wet weight in metric tonnes
merged_data$box1_wet_weight_mt <- merged_data$box1_wet_weight / 1000
merged_data$box2_wet_weight_mt <- merged_data$box2_wet_weight / 1000

# Compute yield per hectare
merged_data$box1_yield_per_hectare <- merged_data$box1_dry_weight / (8 * 5)  # Assuming box dimensions are in meters
merged_data$box2_yield_per_hectare <- merged_data$box2_dry_weight / (8 * 5)

#5. Creating filters for outliers
merged_data$outlier_box1 <- with(merged_data, box1_wet_weight == 0 & box1_dry_weight > 0) |
  with(merged_data, box1_dry_weight > box1_wet_weight)

merged_data$outlier_box2 <- with(merged_data, box2_wet_weight == 0 & box2_dry_weight > 0) |
  with(merged_data, box2_dry_weight > box2_wet_weight)


# Creating filters for potential errors
crazy_box_dimensions <- (merged_data$box1_length > 10 | merged_data$box1_width > 10) |
  (merged_data$box2_length > 10 | merged_data$box2_width > 10)

false_zero_yields <- (merged_data$box1_wet_weight == 0 & merged_data$box1_dry_weight > 0) |
  (merged_data$box2_wet_weight == 0 & merged_data$box2_dry_weight > 0)

dry_exceeds_wet <- merged_data$box1_dry_weight > merged_data$box1_wet_weight |
  merged_data$box2_dry_weight > merged_data$box2_wet_weight

# Creating filters for non-compliant data sets
non_compliant_data <- is.na(merged_data$box1_length) & (merged_data$box1_wet_weight > 0 | merged_data$box1_dry_weight > 0) |
  is.na(merged_data$box2_length) & (merged_data$box2_wet_weight > 0 | merged_data$box2_dry_weight > 0) |
  (merged_data$box1_wet_weight == 0 & merged_data$box1_dry_weight == 0 & (merged_data$box1_wet_weight_confirmation != "No" | merged_data$box1_dry_weight_confirmation != "No")) |
  (merged_data$box2_wet_weight == 0 & merged_data$box2_dry_weight == 0 & (merged_data$box2_wet_weight_confirmation != "No" | merged_data$box2_dry_weight_confirmation != "No")) |
  (merged_data$box1_crop_condition != "Harvest" & merged_data$box1_dry_weight > 0) |
  (merged_data$box2_crop_condition != "Harvest" & merged_data$box2_dry_weight > 0) |
  (merged_data$box1_crop_condition == "Mixed with other crops" & merged_data$box1_dry_weight > 0) |
  (merged_data$box2_crop_condition == "Mixed with other crops" & merged_data$box2_dry_weight > 0)

# Creating filter for harvest crop mixed with other crops
harvest_mixed_with_other_crops <- (merged_data$box1_crop_condition == "Mixed with other crops" & merged_data$box1_dry_weight > 0) |
  (merged_data$box2_crop_condition == "Mixed with other crops" & merged_data$box2_dry_weight > 0)

# Creating filters for outliers
merged_data$outlier <- crazy_box_dimensions | false_zero_yields | dry_exceeds_wet | non_compliant_data | harvest_mixed_with_other_crops

# Showing the counts of outliers
table(merged_data$outlier)


# Identifying major problems affecting crops per district or state
problem_summary <- table(merged_data$farmer_state_district, merged_data$box1_problem)
problem_summary


# Writing a short auto report
library(officer)
doc <- read_docx()
doc <- body_add_par(doc, "Crop Cuts Experiment Analysis Report", style = "heading 1")
doc <- body_add_par(doc, "Major Problems Affecting Crops", style = "heading 2")

# Adding a table summarizing the major problems per district or state
doc <- body_add_table(doc, as.data.frame(problem_summary), first_column = TRUE)

# Saving the document
print(doc, target = "Crop_Cuts_Report.docx")

