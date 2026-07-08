# Global COVID-19 Tracker Dashboard
## Adnan Awad

---

**Link:** https://covid-tracker-dashboard-gamma.vercel.app/

---

### Description
This is an interactive web dashboard built with Flask and Plotly that visualizes COVID-19 trends. It allows users to filter data by country and toggle between different metrics (like daily cases and rolling averages) without reloading the page.

### Project Structure
- `app.py` — The main Flask application and routing logic.
- `templates/index.html` — The frontend: HTML/CSS layout plus the Plotly.js charting and fetch logic.
- `cleaned_covid_data.csv` — The pre-processed dataset (outliers capped at the 99th percentile, nulls handled).
- `COVID_Country_Sample.csv` — The raw source data.
- `Notebook.ipynb` — The analysis notebook used to explore the data and produce the cleaned CSV.
- `requirements.txt` — Python dependencies.

### Design Decisions
- **Outlier handling:** Daily case/vaccination counts often spike from backlogged administrative reporting. Values were capped at the 99th percentile so these artifacts don't compress the rest of the chart.
- **Rolling averages:** Health data is inherently noisy, so 3-month rolling-average toggles are included to surface the underlying trend rather than day-to-day reporting artifacts.
- **Accessibility:** The palette uses a high-contrast blue and avoids red/green combinations that are problematic for colorblind users.
- **Interaction without reloads:** Country/metric changes fetch new JSON from the Flask backend and redraw the chart client-side, so the page never reloads.

---

### Video Demo
See the following YouTube link: https://youtu.be/vIh3TmV7UtE

---

## Download

In case the website is down, or if you wish to download and run locally.

### Prerequisites
Ensure you have Python 3.x installed on your machine.

### Installation & Setup (Command Line Method)
1. Open your terminal or command prompt.
2. Navigate to the folder containing `app.py`.
3. Install the required Python libraries:

   `pip install -r requirements.txt`

4. Start the Flask server:

   `python app.py`

5. Open your web browser and navigate to the local server address provided in the terminal (usually `http://127.0.0.1:5000/`).

### Running via IDE (PyCharm / VS Code)
If you are running this project from within an IDE like PyCharm:
1. Ensure your project interpreter has the dependencies from `requirements.txt` installed.
2. Open `app.py`.
3. Click the "Run" button (or right-click and select "Run 'app'").
4. Click the local server link that appears in the IDE's run console.