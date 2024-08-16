import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

city = ["Chicago", "New York City", "Washington"]
months ={0:"All",1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June"}
weekdays = {7:"All", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 0:"Sunday"}

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

    # #extracting month, day of week and hour information from start time column
    df['month'] =  df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour

    # #creating total_trip_duration column from end time and start time column
    df['total_trip_duration'] = df['End Time'] - df['Start Time']

    if day!='All':
        df = df[df['day_of_week']==day.title()]
    if month!=0:
        df = df[df['month']==month]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    popular_month = df['month'].mode()[0]
    popular_week = df['day_of_week'].mode()[0]
    popular_start_hour = df['start_hour'].mode()[0]

    return (months[popular_month], popular_week, str(popular_start_hour))

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    popular_st_station = df['Start Station'].mode()[0]
    popular_end_station = df['End Station'].mode()[0]
    df['combine_station'] = df['Start Station'] + ' and ' + df['End Station']
    popular_combination =  df['combine_station'].mode()[0]
    return (popular_st_station, popular_end_station, popular_combination)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    user_types = df['User Type'].value_counts()

    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
    else:
        gender_types = "NA"

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_yr = int(df['Birth Year'].min())
        recent_yr = int(df['Birth Year'].max())
        common_yr = int(df['Birth Year'].mode()[0])
    else:
        earliest_yr = "NA"
        recent_yr = "NA"
        common_yr = "NA"

    return (user_types, gender_types, earliest_yr, recent_yr, common_yr)