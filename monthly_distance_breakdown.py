import requests
from datetime import datetime, timedelta
from config import ACCESS_TOKEN


def fetch_strava_activities(start_date, end_date):
    """
    Fetch Strava activities for a specified date range.

    Args:
        start_date (datetime): Start date for fetching activities.
        end_date (datetime): End date for fetching activities.

    Returns:
        list: List of Strava activities.
    """
    activities = []
    page = 1
    per_page = 200  # adjust as needed

    while True:
        url = 'https://www.strava.com/api/v3/athlete/activities'
        params = {'access_token': ACCESS_TOKEN,
                  'after': int(start_date.timestamp()),
                  'before': int(end_date.timestamp()),
                  'per_page': per_page,
                  'page': page}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            current_page_activities = response.json()
            if not current_page_activities:
                break  # No more activities
            activities.extend(current_page_activities)
            page += 1
        else:
            raise Exception(f"Failed to fetch activities: {response.status_code}, {response.text}")

    return activities


def calculate_distance_by_month(activities):
    """
    Calculate the distance covered by month for a given list of Strava activities.

    Args:
        activities (list): List of Strava activities.

    Returns:
        dict: Dictionary with monthly distance breakdown.
    """
    monthly_distance = {}

    for activity in activities:
        activity_date = datetime.strptime(activity['start_date_local'], '%Y-%m-%dT%H:%M:%SZ')
        month_key = (activity_date.year, activity_date.month)

        if month_key not in monthly_distance:
            monthly_distance[month_key] = 0.0

        monthly_distance[month_key] += activity['distance']

    return monthly_distance


if __name__ == "__main__":
    year = int(input("What year do you want to analyze? "))
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)

    sport_type = input("Enter the sport type (e.g., 'Run', 'Ride', 'Swim'): ")
    activities = fetch_strava_activities(start_date, end_date)

    # Filter activities by sport type
    activities = [activity for activity in activities if activity['type'] == sport_type]

    monthly_distance = calculate_distance_by_month(activities)
    total_distance = 0
    # Print the results
    for month, distance in sorted(monthly_distance.items()):
        print(f"{datetime(month[0], month[1], 1).strftime('%B %Y')}: {distance / 1000:.2f} km")
        total_distance += distance

    print(f"Total Yearly Distance: {total_distance / 1000:.2f} km")

