# TravelX
Algorithm that allows user to optimize their trip.

Our algorithm is able to carry out the following task:
1. It enables users to optimize their vacation based on the city they select and the number of days they wish to spend.

# Installation

- Python programming language 
- Download each city's csv file (can be found in the repository)

After downloading each city's information through csv file and importing it into Python, open the file travelx.py and run the program.

# Usage
After the user enters the program they will be asked two give the algorithm two inputs:
- **Input #1**: What city would you like to visit?
- **Input #2**: How many days will you stay?
- **Input #3**: How many hours per day will you like to spend doing tourism?
- **Output**: The Optimized Itinerary for the (Input #2) day(s) in (Input #1) is the following:

Then a list of activities will be presented to the user which they should follow in order to optimize their trip.

# Methods and Data Structures Used

- We used the **dynammic programming** as our programming method which maximized value (in this case ratings) under the constraint of the weight (which in this cases are the days of the trip and how much time every attraction takes).
- We used **lists** as data structures to store all of the cities' information (attractions, ratings of these attractions, and duration of these attractions).

# Future additions to the code
- We would like to add another constraint to the algorithm by considering the user's budget in relation to the cost of each attraction.
- We would like to integrate the data sets for each city and allow users to run the program without needing to download the csv file for each city separately.

# Credits
  Edwin Marmolejos,
  Sebastian Vasquez,
  Arturo Camarena,
  Francisco Jimenez,
  Facundo Exposito,
  Daniel Villalain






