# this approach works for values of total_number_of_days which is less than or around range of 20. any more and program slows down too much
from itertools import product
import math
import sys

class Graduation:

    def __init__(self,total_number_of_days,max_absent_days_in_streak):
        if not type(total_number_of_days) ==int:
            if type(total_number_of_days)==float:
                total_number_of_days=math.ceil(total_number_of_days)
            elif type(total_number_of_days) == str and total_number_of_days.isnumeric():
                total_number_of_days = math.ceil(int(total_number_of_days))
            else:
                raise TypeError("Total number of days must be a number")
        if not type(max_absent_days_in_streak) == int:
            if type(max_absent_days_in_streak)==float:
                max_absent_days_in_streak=math.ceil(max_absent_days_in_streak)
            elif type(max_absent_days_in_streak) == str and max_absent_days_in_streak.isnumeric():
                max_absent_days_in_streak = math.ceil(int(max_absent_days_in_streak))
            else:
                raise TypeError("max number of absent days must be a number")
        
        if total_number_of_days < 0:
            raise ValueError("total number of days must be Positive number or 0")
        
        if max_absent_days_in_streak<0:
            raise ValueError("max_absent_days_in_streak must be a positive number or 0")

        if max_absent_days_in_streak > total_number_of_days:
            raise ValueError("max number of absent days must be always less than total_number_of_days")
        
            
        self.max_days = int(total_number_of_days)
        self.max_absent_days = int(max_absent_days_in_streak)
        self.combinations_list =[]
        self.limit_absent_cases =[]
        self.fail_cases = []
        self.limit_absent_cases = []
        self.fail_cases_count =self.max_combinations_count = 0

    def possible_combinations(self):
        pattern_to_look_for= 'A'*(self.max_absent_days)
        possible_combinations = product(['P','A'],repeat=self.max_days)
        for possible_combination in possible_combinations:
            combination = ''.join(possible_combination)
            if pattern_to_look_for in combination:
                self.limit_absent_cases.append(combination)
            else:
                self.combinations_list.append(combination)        
    
    def valid_combinations(self):
        for combination in self.combinations_list:
            if combination[-1]=='A':
                self.fail_cases.append(combination)
            
        
    def get_chances_of_graduation(self):
        self.possible_combinations()
        self.valid_combinations()
        return f"{len(self.fail_cases)}/{len(self.combinations_list)}"

    
    def use_iteraror_to_speed_up(self):
        pattern_to_look_for= 'A'*self.max_absent_days
        possible_combinations = product(['P','A'],repeat=self.max_days)
        for possible_combination in possible_combinations:
            combination = ''.join(possible_combination)
            if pattern_to_look_for not in combination:
                self.max_combinations_count+=1
                if possible_combination[-1] == 'A':
                    self.fail_cases_count+=1

        return f"{self.fail_cases_count}/{self.max_combinations_count}"

if __name__ == "__main__":
    try:
        total_number_of_days = sys.argv[1]
        max_absent_days_in_streak = sys.argv[2]
    except IndexError:
        print("Please pass 'total_number_of_days' and 'max_absent_days_in_streak' arguments while running the file")
    except Exception as e:
        print(e)
    else:
        solution1 = Graduation(total_number_of_days = total_number_of_days ,max_absent_days_in_streak=max_absent_days_in_streak).get_chances_of_graduation()
        solution2 = Graduation(total_number_of_days = total_number_of_days ,max_absent_days_in_streak=max_absent_days_in_streak).use_iteraror_to_speed_up()
        print(solution1)
        print(f"The number of ways to attend classes over {total_number_of_days} days is {solution1.split('/')[1]}")
        print(f"The probability that you will miss your graduation ceremony is {solution1.split('/')[0]}")
