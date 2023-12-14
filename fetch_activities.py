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
