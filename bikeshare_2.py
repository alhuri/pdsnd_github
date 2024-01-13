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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        # get user input for month (all, january, february, ... , june)
        city = input('What is the name of the city you want to analyze? ').lower()
        if city not in CITY_DATA:
            continue
        else:
            break
    
    while True: 
        # get user input for day of week (all, monday, tuesday, ... sunday)
        month = input('What month you want to filter by? or "all" to apply no month filter ').capitalize()
        if month not in ['January', 'February', 'March', 'April', 'May', 'June','All']:
            continue
        else:
            break
        
    while True: 
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('What day of week to filter by? or "all" to apply no day filter ').capitalize()
        if day not in ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','All']:
            continue
        else:
            break
               

    print('-'*40)
    print(city, month, day)
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
    df_name= CITY_DATA[city]
    df_name= pd.read_csv(df_name)

    df_name['Start Time'] = pd.to_datetime(df_name['Start Time'])
    df_name['month'] = df_name['Start Time'].dt.month_name()
    df_name['day'] = df_name['Start Time'].dt.day_name()
    df_name['hour'] = df_name['Start Time'].dt.hour

    if month!='All' and day !='All':
        df = df_name[(df_name['month'] == month) & (df_name['day'] == day)]
    elif day !='All' and month =='All':
        df = df_name[df_name['day'] == day]
    elif month !='All' and day =='All':
        df = df_name[(df_name['month'] == month)]
    elif month =='All' and day =='All':
        df = df_name



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    print("the most common month is ",df['month'].mode()[0])


    # display the most common day of week
    print("the most common day is ",df['day'].mode()[0])


    # display the most common start hour
    print("the most common hour is ",df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("the most common start station is ",df['Start Station'].mode()[0])


    # display most commonly used end station
    print("the most common end station is ",df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    df['combination']= df["Start Station"] + " " + df["End Station"]
    print("the most frequent combination of start station and end station trip is ",df['combination'].mode()[0])



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("the total travel time is: " , df['Trip Duration'].sum())


    # display mean travel time
    print("the mean travel time is: " , df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("the count of users are\n" , df['User Type'].value_counts().to_frame())

    print('-'*20)
    
    # Display counts of gender
    print("the count of genders are\n" , df['Gender'].value_counts().to_frame())

    print('-'*20)
    # Display earliest, most recent, and most common year of birth
    # df['Birth Year']=df['Birth Year'].astype('int')

    print("the earliest birth year is " , int(df['Birth Year'].min()))
    print("the most recent birth year is " , int(df['Birth Year'].max()))
    print("the most most common year of birth is " , int(df['Birth Year'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
