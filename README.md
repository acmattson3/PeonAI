# PeonAI
A convolutional neural network (CNN) designed to predict if a peony is ready to harvest. Built in Python using Tensorflow and Keras. Data processed using C++ or Python.

# General Information

**AI Type:** Convolutional Neural Network (CNN) through Tensorflow and Keras.

**Purpose:** To predict the readiness of different varieties of peony buds for harvest.

## Primary Goal
The AI will output a “state” value (from zero to two), with zero being underdue and two being overdue. Values closest to one will indicate the peony bud is at the most ideal state for harvesting. 
## Stretch Goals
1. The AI should also output a prediction, in seconds (and interpreted later to a time/date), indicating when the bud will be most ready for harvest. This will likely require a separate network given past, present, and predicted future weather data, nearby flower states, the output of the primary goal AI (the current bud state value), and probably more factors (as I think of them) that can affect the speed at which peony buds bloom.
2. Soon to be more ideas as I inevitably come up with them!

## Explanation
Alaska, where I am from, is home to many peony (a highly popular flower) farms. I have had the pleasure of working on one of these farms, known as Alaska Peonyworks. I plan to work there in future summers, and so I am developing this AI to assist myself - and future workers - with knowing when to harvest flowers.

You may be asking yourself: Why would you need an AI to harvest flowers? Peony farming seems simple enough - just cut the flowers when they look pretty, right? Unfortunately, it is nowhere near that simple. The flowers, once they bloom, don't last much longer than a week or so in a vase before deteriorating. How are farmers expected to sell tens of thousands of flowers within just a couple month-long harvest season? After all, these farmers are in Alaska, which is scarcely populated compared to the rest of the US. Furthermore, it can take **up to a week** for shipments from Alaska to reach the rest of the states - *the flowers would be shriveled by then!* So, then, **what is the solution?**

To increase the longevity of peonies to both increase the selling window and buyer distance, peony farmers have some ingenious tactics. The primary method of storing peonies long-term is **by refrigerating them.** This, though, is also far less simple than it seems. In order to effectively refrigerate the flowers without them shriveling, they must be harvested at a *very particular* state, before the flower itself blooms. The flower buds must be *individually* inspected by farmers that look for a number of properties, including their appearance, texture, and hardness. That in and of itself sounds complicated to keep track of, but unfortunately, that is but the tip of the iceberg. The size of the bud influences how these properties apply. For example, smaller buds appear less ready compared to larger buds when they are actually ready for harvest. Additionally, the weather, *and even nearby flowers that release ethylene gas as they bloom,* can significantly change the speed at which the buds become ready for harvest. To make matters *even worse,* each variety of peony has often **vastly** different indicators of readiness.

Having worked over a summer at Alaska Peonyworks, and being a computer science student at the University of Alaska Fairbanks, I have taken it upon myself to apply computers to this ~~literal~~ field. This problem sounds like a standard neural network problem: I have an assortment of properties from which to make a prediction. It can take years for a peony farmer to have the expertise to identify when multiple different peony varieties are ready to harvest. My hope is that, by developing this AI, I can help these farms to expand at a much greater rate and become far more successful. 

Currently, the bottleneck in my local farm's growth and success appears to be getting new workers, as they can take multiple seasons to adequately train. However, an AI like this would require a worker to simply measure and photograph a peony bud, greatly decreasing the job's difficulty. If nothing else, the AI would help the workers to learn without needing an expert to constantly validate their choices. For example: A worker could identifies a flower they believe is ready. They then pull out their phone, take a photo and quick measurement (possibly with a specialized tool to expedite this process, too), and use the AI to determine whether their identification was correct. This *definitely* beats the alternative of expert farmers running circles around the farm to individually proctor their employees as they happen across possibly-ready flowers. 

# Training Data
The following will describe the type of data that should be collected, how we will collect it, and how it will be formatted. 

## Data to Collect: Primary Goal
* Peony variety
  * A separate boolean input for each variety.
  * Make a data structure to automate this.
* Diameter of peony bud (in centimeters) (horizontally and vertically?)
* Peony bud photograph
  * At a fixed distance.
  * The diameter measurement might cover this.
  * If the distance is fixed, camera focusing is not a problem!
  * Possibly from both the top and side?
* Estimated peony bud state (according to an expertised measurer)
  * An estimated state value ensures the maximum utilization of photos and measurements taken before, during, and after the ideal harvesting window.
  * A value of zero indicates an underdue bud. A value of two indicates an overdue bud. The most harvestable peony bud is closest to a value of one. A value of 0.5 would show some good signs of readiness, and a value of 1.5 would show that the bud has been ready for some time and may be approaching overdue.

## Data to Collect: Stretch Goal #1
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


