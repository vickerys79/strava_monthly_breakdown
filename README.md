# Strava Activity Analysis

This Python script fetches Strava activities for a specified date range and provides a breakdown of the distance covered by month for a given sport type.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/strava-activity-analysis.git
    cd strava-activity-analysis
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Update `config.py`:

    Replace the placeholder in `config.py` with your actual Strava API access token.

4. Run the script:

    ```bash
    python strava_analysis.py
    ```

## Configuring Strava API Access Token

- To use the Strava API, you need to obtain an access token. Refer to the video tutorial [here](https://www.youtube.com/watch?v=sgscChKfGyg) for a guide on generating an access token with the required permissions.

- Make sure to request the `activity:read_all` scope when generating the access token. This scope is necessary to read all activity data.

- If your access token expires, you can use the refresh token to obtain a new access token. Refer to the following URL to refresh the token:

    ```
    https://www.strava.com/oauth/token?client_id=your_client_id&client_secret=your_client_secret&refresh_token=your_refresh_token&grant_type=refresh_token
    ```

    Replace `your_client_id`, `your_client_secret`, and `your_refresh_token` with your actual values.

## Usage

1. When prompted, enter the year you want to analyze.

2. Enter the sport type (e.g., 'Run', 'Ride', 'Swim').

3. View the monthly distance breakdown for the specified year and sport type.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
