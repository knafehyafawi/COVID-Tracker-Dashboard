# Global COVID-19 Tracker Dashboard
## Adnan Awad
-------------
### Description
This is an interactive web dashboard built with Flask and Plotly that visualizes COVID-19 trends. It allows users to filter data by country and toggle between different metrics (like daily cases and rolling averages) without reloading the page.

### Prerequisites
Ensure you have Python 3.x installed on your machine.

### Installation & Setup (Command Line Method)
1. Open your terminal or command prompt.
2. Navigate to the folder containing `app.py`.
3. Install the required Python libraries by running the following command:
   pip install flask pandas plotly
4. Start the Flask server by running:
   python app.py
5. Open your web browser and navigate to the local server address provided in the terminal (usually http://127.0.0.1:5000/).

### Running via IDE (PyCharm / VS Code)
If you are running this project from within an IDE like PyCharm:
1. Ensure your project interpreter has `flask`, `pandas`, and `plotly` installed.
2. Open `app.py`.
3. Click the "Run" button (or right-click and select "Run 'app'").
4. Click the local server link that appears in the IDE's run console.

### Project Structure
- app.py : The main Flask application and routing logic.
- cleaned_covid_data.csv : The pre-processed dataset (outliers capped, nulls handled).
- clean_data.py : The script used to generate the cleaned CSV.
- templates/index.html : The frontend HTML/JS file containing the Plotly logic and styling.

### Video Demo:
See the following YouTube link: https://youtu.be/vIh3TmV7UtE
