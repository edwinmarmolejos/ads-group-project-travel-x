# TravelX
Algorithm that allows user to optimize their trip.

Our algorithm is able to carry out the following task:
1. It enables users to optimize their vacation based on the city they select and the number of days they wish to spend.

# Installation

- Python programming language 
- Download data.csv file (can be found in the repository)

After downloading each city's information through csv file and importing it into Python, open the file travelx.py and run the program.

# Data Description
- Our data set includes 9 cities, each with 30 attractions, as well as the category, duration, rating, and cost of each attraction.

**Source**: The data was collected from Tripadvisor https://www.tripadvisor.com/ .

The cities and categories of attractions included in this data are listed below:

<img width="321" alt="Data Summary" src="https://user-images.githubusercontent.com/94702966/144243252-2125e70e-3008-4620-bff8-9a8c7b1e1806.png">


# User Journey
After the user enters the program they will be asked two give the algorithm some inputs:
1. User is welcomed "Hello welcome to TRAVELX , the perfect Itinerary Optimization App!"
2. A list of all the possible destinations is presented.
- **Input #1**: What city would you like to visit?
3. Algorithm prints "TRAVELX would like to ask you about your preferences to make the 
Right travel itinerary for you!" 
- **Input #2**: Would you like to tells us about your preferences? (yes or no)
If the user enters yes, the algorithm will ask the user to rate each category of attraction on a scale of 0 to 5, and it will then proceed to **Input #3**.
If the user enters no, they will proceed to **Input 3** directly.
- **Input #3**: How many days will you stay? (Algorithm can only accept trips of less than 10 days)
- **Input #4**: How many hours per day will you like to spend doing tourism? (The algorithm can only accept times between 6 and 10 hours)
- **Input #5**: What is your budget(€)?
- **Final Output #1**: The algorithm will output the itinerary to maximize rating, the output will be divided by day including all the attractions for a certain day as well as the total duration and cost per day.
- **Final Output #2**: The algorithm outputs average rating, total cost, average hours per day of tourism of the whole trip.
- **Input #6**: The user is prompted if he wants to run the program again.
If the user has selected yes, the program will be restarted from the beginning.
If the user enters no, the algorithm will respond, "TRAVELX thanks you for using our app!"


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






