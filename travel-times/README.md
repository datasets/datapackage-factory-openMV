# Description
A driver uses an app to track GPS coordinates as he drives to work and back each day. The app collects the location and elevation data. Data for about 200 trips are summarized in this data set.

# Dataset
The dataset consists of:

- `Date` of travel
- `StartTime`: when getting into the car
- `DayOfWeek`: the day name
- `GoingTo`: direction of travel
- `Distance` travelled in kilometers
- `MaxSpeed`: fastest speed recorded (all trips are on the 407 highway for some portion)
- `AvgSpeed`: the average speed for the entire trip
- `AvgMovingSpeed`: the average speed recorded only while the car is moving
- `FuelEconomy`: a rough estimate of fuel economy (it is inaccurate)
- `TotalTime`: duration of the entire trip, in minutes
- `MovingTime`: duration when the car was considered to be moving (i.e. not counting traffic delays, accidents, or time while the car is stationary)
- `Take407All`: is Yes if the 407 toll highway was taken for the entire trip. I try to avoid taking the 407, taking slower back routes to save costs. But some days I'm running late, or just lazy, and take it all the way.
- `Comments`
# Preparation
Python version: 3.6 

# License
Please follow [this]("https://creativecommons.org/licenses/by-sa/4.0/") for License information