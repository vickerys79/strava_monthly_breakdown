from fetch_activities import fetch_all_strava_activities


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
    else:
        print("No activities found.")
