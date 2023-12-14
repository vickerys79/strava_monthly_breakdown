from fetch_activities import fetch_all_strava_activities


def hr_data(activities, activity_type):
    highest_hr = 0
    average_hr = 0
    for activity in activities:
        if activity.get('has_heartrate') and activity.get('type') == activity_type:
            if activity.get('max_heartrate') > highest_hr:
                highest_hr = activity['max_heartrate']
                highest_hr_name = activity['name']
                highest_hr_date = activity['start_date']
            if activity.get('average_heartrate') > average_hr:
                average_hr = activity['average_heartrate']
                average_hr_name = activity['name']
                average_hr_date = activity['start_date']

    if highest_hr == 0:
        print("no heartrate data was found for this activity type")
        return highest_hr, None, None, average_hr, None, None

    return highest_hr, highest_hr_name, highest_hr_date, average_hr, average_hr_name, average_hr_date


if __name__ == "__main__":
    activities = fetch_all_strava_activities()
    activity_type = input("Enter the sport type (e.g., 'Run', 'Ride', 'Swim'): ")

    highest_hr, highest_hr_name, highest_hr_date, average_hr, average_hr_name, average_hr_date = hr_data(
        activities,
        activity_type
    )

    if highest_hr > 0:
        print(f"Highest HR: {highest_hr}")
        print(f"Highest HR Activity Name: {highest_hr_name}")
        print(f"Highest HR Activity Date: {highest_hr_date}")
        print(f"Highest Average HR: {average_hr}")
        print(f"Highest Average HR Activity Name: {average_hr_name}")
        print(f"Highest Average HR Activity Date: {average_hr_date}")
