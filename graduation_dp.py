# this approach works for higher value of number of days but only works for 4 absents

import sys

def graduation_probability(days):

    combinations = [[0,0,0,0] for i in range(days+1)]  # combinations[i][j] is the number of ways to attend classes up to i days with j consecutive absences
    combinations[0][0] = 1  # if a person wants to graduate then he has to attend on graduation day, so with only one day as N, he has to attend on that day
    
    for day in range(1, days+1):
        # Attend class
        #  number of ways to attend class here is if they attended till previous day with 0,1,2,3 absents consecutively. any more and they cant
        combinations[day][0] = combinations[day-1][0] + combinations[day-1][1] + combinations[day-1][2] + combinations[day-1][3]  
        
        # Miss class -- if we want to miss 1-3 days from today then the chances are as follows
        combinations[day][1] = combinations[day-1][0]  # If we missed only one day on the previous day, we can attend on the current day
        combinations[day][2] = combinations[day-1][1]  # If we missed two consecutive days on the previous day, we can attend on the current day
        combinations[day][3] = combinations[day-1][2]  # If we missed three consecutive days on the previous day, we can attend on the current day
    
    # Calculate the answer
    total_ways = combinations[days][0] + combinations[days][1] + combinations[days][2] + combinations[days][3]  # Total number of ways to attend classes including miss classes on last day
    missed_ways = combinations[days][1] + combinations[days][2] + combinations[days][3]  # Number of ways to miss classes on the last day
    return f"{missed_ways}/{total_ways}"  # Return the probability of missing the graduation ceremony in string format


# print(graduation_probability(5))
if __name__ == "__main__":
    print(graduation_probability(int(sys.argv[1])))