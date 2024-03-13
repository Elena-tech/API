Sure, let's update your README file with a more comprehensive guide that incorporates the advancements and clarifications we've discussed. Here's the updated content:

---

# Pexels Image Search Application

This project provides a simple interface for searching and displaying images using the Pexels API. It leverages Flask for the web interface, allowing users to input search queries and view results directly on the webpage.

## Installation

Before you begin, it's recommended to create a new virtual environment for this project to manage dependencies effectively.

### Create a Virtual Environment:

- **For Windows**:
  Open Command Prompt and run:
  ```bash
  python -m venv venv
  ```

- **For macOS/Linux**:
  Open Terminal and run:
  ```bash
  python3 -m venv venv
  ```
  This creates a new virtual environment named `venv`. You can choose a different name if preferred.

### Activate the Virtual Environment:

- **On Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

- **On macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### Clone the Repository:

Replace `your-repository-url` with the URL of your project repository:
```bash
git clone https://your-repository-url.git
cd your-project-directory
```
Ensure `your-project-directory` is the folder containing your project.

### Install Required Packages:

Within the activated virtual environment, install dependencies via:
```bash
pip install -r requirements.txt
```

## Requirements

This project requires Python 3.x and the following libraries:

- `Flask`: For creating the web application.
- `python-dotenv`: To manage environment variables.
- `requests`: For making HTTP requests to the Pexels API.
- `pexels-api`: An optional wrapper for the Pexels API, not used directly in this project due to customization needs.

## Usage

Start the application with:
```bash
python app.py
```

This command launches a Flask server, making the application accessible at `http://127.0.0.1:5000/` by default. Users can search for images via the web interface, with search results dynamically rendered on the same page.

## Project Structure

- `app.py`: Flask application setup, including routes for handling search requests.
- `templates/`: Folder containing HTML templates for the search page and results display.
- `api/connector.py`: Module for interfacing with the Pexels API, customized for specific project needs.
- `requirements.txt`: Lists the Python packages necessary for the project.

### Interacting with the Application

The web interface allows users to input search terms and select filters for image orientation, color, and size. The search results, including image previews and photographer credits, are displayed directly below the search form.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes. For major changes, please open an issue first to discuss what you would like to change.
