import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


CITIES = {1:'chicago', 2:'new york city', 3:'washington'}


MONTHS = {0:'all',1:'January',2:'February',3:'March',4:'April',5:'May',6:'June'}


WEEKS = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday', 7:'all'}

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
        try:
            city=int(input('Please input the city which you want to analyze, options are: 1 for chicago, 2 for new york city, 3 for washington\n'))
            if city in CITIES:
                break
            else:
                print('Please enter valid city input, Try Again!!')
        except ValueError:
            print("Please enter valid city input, Try Again!!")

    while True:
        try:
            print('\nChoose month to filter data')
            month = int(input('Enter 1 for January, 2 for February, 3 for March, 4 April, 5 May, 6 June or 0 to include all months\n'))
            if month in MONTHS:
                break
            else:
                print('Please enter valid month input, Try Again!!')
        except  ValueError:
            print("Please enter valid month input, Try Again!!")



    # TO DO: get user input for month (all, january, february, ... , june)


    while True:
        try:
            print('\nChoose month to filter data')
            week = int(input('Enter 0 for Monday, 1 for Tuesday, 2 for Wednesday, 3 Thursday, 4 Friday, 5 Saturday, 6 for Sunday or 7 to include all days of the week\n'))
            if week in WEEKS:
                break
            else:
                print('Please enter valid day of week input, Try Again!!')
        except  ValueError:
            print("Please enter valid day of week input, Try Again!!")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return CITIES[city], month, WEEKS[week]


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

    df = pd.read_csv(CITY_DATA[city]) #reading csv data

    #changing datatype of Start Time and End Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #extracting month, day of week and hour information from start time column
    df['month'] =  df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour

    #creating total_trip_duration column from end time and start time column
    df['total_trip_duration'] = df['End Time'] - df['Start Time']

    if day!='all':
        df = df[df['day_of_week']==day.title()]
    if month!=0:
        df = df[df['month']==month]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('Most common month of travel is: '+MONTHS[popular_month])
    # TO DO: display the most common day of week
    popular_week = df['day_of_week'].mode()[0]
    print('Most common day of week for travel is: '+popular_week)

    # TO DO: display the most common start hour
    popular_start_hour = df['start_hour'].mode()[0]
    print('Most common start hour for travel is: '+str(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_st_station = df['Start Station'].mode()[0]
    print('Most common start station is: '+popular_st_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most common end station is: '+popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combine_station'] = df['Start Station'] + ' and ' + df['End Station']
    popular_combination =  df['combine_station'].mode()[0]
    print('Most frequent combination of start and end station is: '+popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['total_trip_duration'].sum()
    print('Total travel time is: ' + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['total_trip_duration'].mean()
    print('Mean travel time is: ' + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of user types:\n")
    print(user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print("Count of gender types:\n")
        print(gender_types)
    else:
        print('\nGender field is not present for the current dataset')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_yr = int(df['Birth Year'].min())
        youngest_yr = int(df['Birth Year'].max())
        mode_yr = int(df['Birth Year'].mode()[0])
        print('\nEarliest year of birth: '+str(earliest_yr))
        print('\nMost recent year of birth: '+str(youngest_yr))
        print('\nMost common year of birth: '+str(mode_yr))
    else:
        print('\nBirth Year field is not present for the current dataset')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city,month,day = get_filters()
        print(city,month,day)
        df = load_data(city, month, day)
        total_rows = len(df)
        iterate = 5
        i=0

        #prompting user to print raw dataset
        prompt=input("Do you want to view the first 5 rows of raw data, yes or no?\n")
        if total_rows>0:
          while i<=total_rows and prompt =='yes' :
              if i!=0:
                  prompt = input("Do you want to view next 5 rows, yes or no?\n")
              print(df.iloc[i:i+iterate])
              print('\n')
              i+=iterate
          while prompt.lower() == 'yes':
              prompt = input("if you still want to ")
          time_stats(df)
          station_stats(df)
          trip_duration_stats(df)
          user_stats(df)
        else:
          print('Filter dataframe is empty.')

        #prompting user to restart 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
