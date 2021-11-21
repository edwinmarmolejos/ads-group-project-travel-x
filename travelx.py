
def knapsack(W, wt, val, n, attractions):
    K = [[0 for w in range(W + 1)]
         for i in range(n + 1)]
    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                v = ""
                K[i][w] = 0, v
            elif wt[i - 1] <= w:

                cond1 = val[i - 1], attractions[i - 1]
                cond2 = [K[i - 1][w - wt[i - 1]][0], K[i - 1][w - wt[i - 1]][1]]

                first_option = cond1[0] + cond2[0], cond1[1] + cond2[1]
                second_option = [K[i - 1][w][0], K[i - 1][w][1]]

                maximum = max(first_option[0], second_option[0])
                if maximum == first_option[0]:
                    K[i][w] = maximum, first_option[1]

                else:
                    K[i][w] = maximum, second_option[1]
            else:

                value = K[i - 1][w]

                K[i][w] = value

    # stores the result of Knapsack
    res = K[n][W][1]

    return res

def read_csv_file(city):
    infileName = city + '.csv'
    infile = open(infileName, "r")  # data
    attractions = []
    values = []
    weights = []
    final_attractions = []
    for line in infile:
        entry = line.split(",")

        attraction = entry[0]

        attractions.append(attraction)
        hours = int(entry[1])
        weights.append(hours)

        ratings = int(entry[2])

        values.append(ratings)
    for i in attractions:
        x = i + ";"
        final_attractions.append(x)
    infile.close()
    
    return final_attractions, values, weights

def city_error_handling(city_input):
    city_input = city_input.lower()
    city_input = city_input.strip()
    return city_input

def main():
    city_input = input("What city would you like to visit?")
    city_input = city_error_handling(city_input)
    attractions, values, weights = read_csv_file(city_input)
    days_constraint = int(input("How many days will you stay?"))
    hours_per_day = int(input("How many hours per day will you like to spend doing tourism?"))
    hours = days_constraint * hours_per_day
    itinerary = knapsack(hours, weights, values, len(values), attractions)

    itinerary = itinerary.split(";")
    itinerary = list(filter(None, itinerary))
    print("\nThe Optimize Itinerary for", days_constraint, "day(s) in", city_input.capitalize(), "is the following:")
    for i in itinerary:
        print(" -", i)
        
main()
        
 
