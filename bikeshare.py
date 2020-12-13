""" Re-Submitting the Code after Review #1 was completed.
    Added the addtional function that will ask for input from user for showing 5 lines of raw data and continue to ask untill user says no.
    Refered Material are: Stack Overflow,https://www.w3schools.com/python/default.asp,https://pandas.pydata.org/docs/user_guide/index.html
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    
    while True:
        city = input("Bikeshare is available in 'chicago, new york city, washington', Please choose the city from these options?: ")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid input. Please enter a valid city option from 'chicago','new york city' or 'washington?")


    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month = input("Do you want details of specific month? Type month name, if looking for all months type input as 'all': ")
        month = month.lower()
        if month in [ 'january', 'february', 'march', 'april', 'may', 'june', 'all' ]:
            break
        else:
            print("Invalid Month. Please enter a valid month between January and June or 'all' option.")
                      


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                      
    while True:
        day = input("Do you want details of specific day? Type Day name, if looking for all days type input as 'all': ")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Invalid Day. Please enter a valid day of a week or 'all' option.")
                  


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into dataframe
    
    df = pd.read_csv(CITY_DATA[city])
                  
    # Start Time Column is converted to datatime 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Get month and day of Wekk from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
                  
    # Filter by Month of year if condition satisfies
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # Filter by Month to create a new dataframe
        df = df[df['month'] == month]
                  
        # Filter by Day of Week if applicable
    if day != 'all':
        # Filter by day of week to create a new datafram
        df = df[df['day_of_week'] == day.title()]
        
    return df
                  


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Popular Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common Month is ", df['month'].mode()[0], "\n")
          
    # TO DO: display the most common day of week
    print("Most Common day of week is ", df['day_of_week'].mode()[0], "\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("Most Common hour of day is ", df['hour'].mode()[0])
                
    print("\n Took %s seconds!" % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start Station is ", df['Start Station'].mode()[0], "\n")
       
    # TO DO: display most commonly used end station"
    print("Most Commonly used end station is ", df['End Station'].mode()[0], "\n")
    
    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " AND " + df['End Station']
    print("Most frequent Combination of start station AND end station during trip is: ", df['combination'].mode()[0])
                  
    print("\n This took %s minutes. " %((time.time() - start_time)/60))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total time to travel is", df['Trip Duration'].sum(), "\n")
           

    # TO DO: display mean travel time
    print("Total mean time to travel is", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n") 
    if city != 'washington':

    # TO DO: Display counts of gender
        gen = df.groupby(['Gender'])['Gender'].count()
        print(gen)
                  
    # TO DO: Display earliest, most recent, and most common year of birth
        earliestyob = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        mostrecentyob = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        mostcommonyob = df['Birth Year'].mode()[0]
    
        print("Earliest Year of Birth is ", earliestyob, "\n")
        print("Most Recent Year of Birth is ", mostrecentyob, "\n")
        print("Most Common Year of Birth is ", mostcommonyob, "\n")
                 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Added This function after reviewer feedback
    Ask User if they would like to see some dat
    Display 5 lines, and then ask if they want to see 5 more
    Continue assking until they stop
    """
    show_lines = 5
    lines_start = 0
    lines_end = show_lines - 1
    
    print('\nWould you like to see 5 lines of raw data?')
    
    
    while True:
        answer = input('Answer, yes or no: ')
        if answer.lower() not in  ['yes','no']:
            print('Wrong input, Options are yes or no.')
            
        elif answer.lower() == 'yes':
            
            print('\nDisplaying lines {} to {}:'.format(lines_start + 1, lines_end + 1))
            
            print('\n', df.iloc[lines_start : lines_end + 1])
            lines_start += show_lines
            lines_end += show_lines
            
            print('-'*40)
            print('\nWould you like to see the next {} lines?'.format(show_lines))
            continue
        elif answer.lower() == 'no':
            
            break
            


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to continue? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
