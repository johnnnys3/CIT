# Chronic Illness Tracker Web App

## Overview

This web application helps patients with chronic autoimmune and invisible illnesses improve their symptoms by tracking their symptom severity, treatments, and potential environmental triggers. The app allows users to record daily symptoms, treatments, and environmental factors, and provides visualizations to help them understand and manage their health better.

## Features

- **User Authentication**: Register and log in to manage your personal data.
- **Symptom Tracking**: Log and track symptoms, their severity, and potential triggers.
- **Data Visualization**: View trends and summaries of your symptoms, treatments, and triggers using interactive charts.
- **Profile Management**: Update your profile information and manage your account details.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/johnnys3/chronic-illness-tracker.git
    ```

2. Navigate to the project directory:

    ```sh
    cd chronic-illness-tracker
    ```

3. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

5. Set up the database:

    ```sh
    flask db upgrade
    ```

6. Run the application:

    ```sh
    flask run
    ```

7. Open your browser and go to `http://127.0.0.1:5000` to access the app.

## Usage

- **Register**: Create a new account by providing your username, email, and password.
- **Login**: Access your account with your email and password.
- **Track Symptoms**: Use the form to log your symptoms, severity, date, and potential triggers.
- **View Symptoms**: Check your symptom list and dashboard to see your symptom history and visualizations.
- **Update Profile**: Manage your account details and update your information as needed.

## Project Structure

- `app/`: Contains the application code.
  - `__init__.py`: Initializes the Flask app and database.
  - `models.py`: Defines the database models.
  - `routes.py`: Contains the route handlers.
  - `templates/`: HTML templates for rendering views.
    - `base.html`: Base template with common layout.
    - `index.html`: Home page.
    - `symptoms.html`: Page for viewing symptoms.
    - `symptom_form.html`: Form for adding or editing symptoms.
    - `register.html`: User registration page.
    - `login.html`: User login page.
    - `profile.html`: User profile page.
  - `static/`: Static files (CSS, JavaScript).
    - `css/`: Stylesheets.
    - `js/`: JavaScript files.
    - `bootstrap/`: Bootstrap CSS and JS files.
  - `config.py`: Configuration settings for the app.
  - `database.db`: SQLite database file.
  - `tests/`: Test cases for the app.
    - `test_models.py`: Tests for database models.
    - `test_routes.py`: Tests for routes.
  - `README.md`: Project documentation.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your branch.
4. Create a pull request with a description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Flask documentation and community
- Bootstrap for styling
- Chart.js for data visualization

