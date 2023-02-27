import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

## WELCOME TO MY CODE!

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Choose a city to receive info on!\nyou have three options New York City, Chicago or Washington?\n")
        # make input case-insensitive
        city = city.lower()

        # check the validity of the user's input
        if city not in ('new york city', 'chicago', 'washington'):
            print("Invalid choice, please try again!")
            continue
        else:
            break

    # get user input for month (all, january, february-june)
    while True:
        month = input("Which month are you interested in?\nKeep in mind we have the first six months data avaliable: January, February, March, April, May, June or type 'all'!\n")
        # make input case-insensitive
        month = month.lower()

        # check the validity of the user's input
        if month not in ('january', 'february', 'march', 'april', 'may',
                         'june', 'all'):
            print("Invalid choice, please try again!")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of the week would you like to have statistics on?\n or you can always type 'all' if you don't have anything in mind!\n")
        # make input case-insensitive
        day = day.lower()

        # check the validity of the user's input
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                       'saturday', 'sunday', 'all'):
            print("Invalid choice, please try again!")
            continue
        else:
            break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['Month'] == month]
    # filter by day if applicable
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        df = df[df['Weekday'] == day]

    return df


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['Month'].mode()[0]

    print('Most common month of the year based on your selection is: ', common_month)


    # display the most common day of week
    common_day_of_week = df['Weekday'].mode()[0]

    print('Most common day of the week based on your selection is: ', common_day_of_week)


    # display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['Start Hour'].mode()[0]

    print('Most popular start hour based on your selection is: ', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most popular start station based on your selection is: ', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most popular end station based on your selection is: ', common_end_station)

    # display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    frequent_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most common combination of Start Station and End Station trip based on your selection is: \n', frequent_combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total travel time based on your selection is: ', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean travel time based on your selection is: ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users. Statistics will be calculated using NumPy."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Here is the count of User Types based on your selection: ')
    print(df['User Type'].value_counts())

    # Display counts of gender
    if city.title() != 'Washington':
        print('Here is the count of Gender based on your selection: ')
        print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common birth year of users based on your selection is: ',common_birth_year)
        most_recent_birth_year = df['Birth Year'].max()
        print('The most recent birth year of users based on your selection is: ',most_recent_birth_year)
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest birth year of users based on your selection is: ',earliest_birth_year)
        birthyear = df['Birth Year'].values

    else:
        # if the user input was washington
        print('Sorry. Gender and birth year data are not available for Washington!')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# new function for raw data display
def raw_data(df):
    """ Displays 5 lines of raw data at a time when yes is selected."""
    i = 1
    while True:
        raw_data_display = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if raw_data_display.lower() == 'yes':
            # print current 5 lines
            print(df[i:i+5])


            i = i+5

        else:

            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        # raw data function
        raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

###SHOUT-OUT: Thanks to one of the session leads: Israa for her help in understanding this project!
