import requests
from config import ACCESS_TOKEN  # Add other constants as needed


def fetch_all_strava_activities():
    activities = []
    page = 1
    per_page = 200  # adjust as needed

    while True:
        url = 'https://www.strava.com/api/v3/athlete/activities'
        params = {'access_token': ACCESS_TOKEN, 'per_page': per_page, 'page': page}
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


def find_most_kudos_activity(activities):
    """
    Find the activity with the highest kudos count.

    Args:
        activities (list): List of Strava activities.

    Returns:
        dict: Activity with the highest kudos count.
    """
    if not activities:
        return None

    most_kudos_activity = max(activities, key=lambda x: x.get('kudos_count', 0))
    return most_kudos_activity


if __name__ == "__main__":
    activities = fetch_all_strava_activities()

    # Find the most kudos activity
    most_kudos_activity = find_most_kudos_activity(activities)

    if most_kudos_activity:
        print(f"The activity with the most kudos is:")
        print(f"Activity Name: {most_kudos_activity['name']}")
        print(f"Kudos Count: {most_kudos_activity['kudos_count']}")
        print(f"number of activities: {len(activities)}")
    else:
        print("No activities found.")
