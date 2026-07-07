from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the cleaned dataset once when the app starts
# Make sure 'cleaned_covid_data.csv' is in the exact same folder as app.py
try:
    df = pd.read_csv('cleaned_covid_data.csv')
except FileNotFoundError:
    print("Error: cleaned_covid_data.csv not found. Did you run the cleaning script?")
    df = pd.DataFrame()  # Fallback to prevent immediate crash


@app.route('/')
def index():
    """
    Part B: Root route that renders the HTML template.
    Passes the countries list and date range to the frontend.
    """
    if df.empty:
        return "Data not found. Please process the CSV first."

    # 1. Get a sorted list of unique countries for the HTML dropdown
    countries = sorted(df['country'].unique().tolist())

    # 2. Calculate the date range for the summary section
    min_date = df['date'].min()
    max_date = df['date'].max()
    date_range = f"{min_date} to {max_date}"

    # Render the template and inject our Python variables into the HTML
    return render_template('index.html', countries=countries, date_range=date_range)


@app.route('/data')
def get_data():
    """
    Part D: Event Interaction Route.
    Accepts URL parameters (e.g., /data?country=Canada&metric=new_cases)
    and returns the filtered data as JSON for Plotly to draw.
    """
    if df.empty:
        return jsonify({'error': 'No data available'})

    # 1. Grab the user's choices from the URL (default to Canada and new_cases)
    selected_country = request.args.get('country', 'Canada')
    selected_metric = request.args.get('metric', 'new_cases')

    # 2. Filter the master dataframe down to just the selected country
    country_data = df[df['country'] == selected_country].copy()

    # Ensure chronological order so the Plotly line chart doesn't zig-zag backward
    country_data = country_data.sort_values(by='date')

    # 3. Extract just the X (dates) and Y (metric values) columns into native Python lists
    dates = country_data['date'].tolist()
    values = country_data[selected_metric].tolist()

    # Return a JSON dictionary that our JavaScript fetch() will easily read
    return jsonify({
        'dates': dates,
        'values': values,
        'country': selected_country,
        'metric': selected_metric
    })


if __name__ == '__main__':
    app.run(debug=True)
