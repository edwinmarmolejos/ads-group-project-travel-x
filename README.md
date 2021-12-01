# TravelX
Algorithm that allows user to optimize their trip.

Our algorithm is able to carry out the following task:
1. It enables users to optimize their vacation based on the city they select and the number of days they wish to spend.

# Installation

- Python programming language (version 3.9)
- Libraries: In order for the program to run the user needs to download three libraries pandas, os and random.

- Download data.csv file (can be found in the repository)

After downloading and importing each city's information via csv file into Python, import the libraries and open the file travelx.py to execute the application.

# Data Description
- Our data set includes 9 cities, each with 30 attractions, as well as the category, duration, rating, and cost of each attraction.

**Source**: The data was collected from Tripadvisor https://www.tripadvisor.com/ .

The cities and categories of attractions included in this data are listed below:

<img width="321" alt="Data Summary" src="https://user-images.githubusercontent.com/94702966/144243252-2125e70e-3008-4620-bff8-9a8c7b1e1806.png">


# User Journey
User is welcomed "Hello welcome to TRAVELX , the perfect Itinerary Optimization App!"

A list of all the possible destinations is presented.

- **Input #1**: What city would you like to visit?

Algorithm prints "TRAVELX would like to ask you about your preferences to make the 
Right travel itinerary for you!" 

- **Input #2**: Would you like to tells us about your preferences? (yes or no)

If the user enters yes, the algorithm will ask the user to rate each category of attraction on a scale of 0 to 5, and it will then proceed to **Input #3**.
If the user enters no, they will proceed to **Input #3** directly.

- **Input #3**: How many days will you stay? (Algorithm can only accept trips of less than 10 days)
- **Input #4**: How many hours per day will you like to spend doing tourism? (The algorithm can only accept times between 6 and 10 hours)
- **Input #5**: What is your budget(€)?
- **Final Output #1**: The algorithm will generate the itinerary that maximizes rating; the result will be divided by day and include all of the attractions for that day, as well as the total time and cost each day.
- **Final Output #2**: The algorithm outputs the average rating, total cost, and average amount of hours of tourism each day for the whole trip.
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






