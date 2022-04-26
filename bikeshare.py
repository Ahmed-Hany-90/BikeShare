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
        city = input('Please enter a city name from chicago, new york city or washington: ').lower()
        if city not in CITY_DATA:
            print('Please enter a valid city name.')
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please enter a month name from January to June or "all" to show all months: ').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month not in months and month != "all":
            print('Please enter a valid month name.')
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please enter a day of week or "all" to show all days: ').lower()
        days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        if day not in days and day != "all":
            print('Please enter a valid day name.')
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is: ", most_common_month)


    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day of week is: ", most_common_day)


    # TO DO: display the most common start hour
    most_common_hour = df['start_hour'].mode()[0]
    print("The most common start hour is: ", most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: ", most_start_station)


    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: ", most_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_combination = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print("The most frequent combination of start and end staion is: ", most_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The average travel time is: ", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_count = df['User Type'].value_counts()
    print("The counts of user types is: ", type_count)


    # TO DO: Display counts of gender
    gender_count = df['Gender'].value_counts()
    print("The counts of gender is: ", gender_count)


    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    print("The earliest year of birth is: ", earliest_birth)
    recent_birth = df['Birth Year'].max()
    print("The most recent year of birth is: ", recent_birth)
    common_birth = df['Birth Year'].mode()[0]
    print("The most common year of birth is: ", common_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    print('\n Raw data is available to display. \n')
    
    display_raw = input("Would you like to see 5 rows of data? Type yes or no")
    while display_raw == "yes":
        try:
            for chunk in pd.read_csv(CITY_DATA[city], chunksize=5):
                print(chunk)
                display_raw = input("Would you like to see another 5 rows of data? Type yes or no: ")
                if display_raw != "yes":
                    print("Thank you!")
                    break
            break
        except KeyboardInterrupt:
            print("Thank you!")
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
