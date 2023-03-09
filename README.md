# PeonAI
A convolutional neural network (CNN) designed to predict if a peony is ready to harvest. Built in Python using Tensorflow and Keras. Data processed using C++ or Python.

# General Information
**Name:** PeonAI

**AI Type:** Convolutional Neural Network (CNN) through Tensorflow and Keras.

**Purpose:** To predict the readiness of different varieties of peony buds for harvest.

## Primary Goal
The AI will likely output a “state” value (from zero to two), zero being underdue and two being overdue. 
## Stretch Goals
1. The AI should also output a prediction, in seconds (and interpreted later to a time/date), indicating when the bud will be most ready for harvest. This may take a separate network given weather data and nearby flower states.

# Training Data
The following will describe the type of data that should be collected, how we will collect it, and how it will be formatted. 

## Data to Collect (for Primary Goal)
* Peony variety
  * A separate boolean input for each variety.
  * Make a data structure to automate this.
* Diameter of peony bud (in centimeters) (horizontally and vertically?)
* Peony bud photograph
  * At a fixed distance.
  * The diameter measurement might cover this.
* If the distance is fixed, camera focusing is not a problem!
  * Possibly from both the top and side?
* Estimated peony bud state (according to the measurer)
  * An estimated state value ensures the maximum utilization of photos and measurements taken before, during, and after the ideal harvesting window.
  * A value of zero indicates an underdue bud. A value of two indicates an overdue bud. The most harvestable peony bud is closest to a value of one. A value of 0.5 would show some good signs of readiness, and a value of 1.5 would show that the bud has been ready for some time and may be approaching overdue.

## Data to Collect (for Stretch Goal #1)
* Measurement and Harvest times/dates
  * When the photo and measurements were taken.
  * When the bud was harvested.
* Peony bed number and location
  * A boolean value for each pair of beds. Beds are aligned in pairs (A0 and A1, A2 and A3, etc.) (Beds go from A0-A6, B0-B6, and C0-C6).
  * How far along the bed pair is the peony (in meter increments)?
  * The location data will help the AI estimate the readiness of nearby flowers. 
    * Blooming flowers release ethylene gas, encouraging nearby flowers to bloom quicker.
    * More nearby blooming flowers might indicate quicker readiness times.
* Current weather data
  * UV radiation data
  * Dry bulb and dew point temperatures
  * Pressure (opening can speed up if low pressure)
  * Precipitation
* Previous month’s average weather data
  * Starting from the time the peonies break the ground?
  * UV radiation
  * Precipitation
  * Dry bulb and dew point temperatures
* Weather forecasts for the upcoming week

## Data Format
To ensure the maximum utilization of data, photos and measurements taken well before, at, and after harvest time should all be kept. To do so, a peony bud “state” value should correspond to a bud to test the network. Example: The (default) underdue bud state value is zero. If the peony bud is overdue, the value is two. Any value between zero and two means the peony is ready to harvest


