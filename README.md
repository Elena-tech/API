## Installation

Before you begin, it's recommended to create a new virtual environment for this project. This helps keep dependencies required by different projects separate by creating isolated environments for them.

1. **Create a Virtual Environment:**
   
   - **For Windows**, open Command Prompt and run:
     ```bash
     python -m venv venv
     ```
   
   - **For macOS/Linux**, open Terminal and run:
     ```bash
     python3 -m venv venv
     ```
   This command creates a new virtual environment named `venv` in your project directory. Feel free to replace `venv` with a different name if desired.

2. **Activate the Virtual Environment:**
   
   - **On Windows**, execute:
     ```bash
     .\venv\Scripts\activate
     ```
   
   - **On macOS/Linux**, use:
     ```bash
     source venv/bin/activate
     ```
   Once activated, your shell prompt will include the name of the virtual environment, indicating all Python and pip commands are isolated to this environment.

3. **Clone the Repository:**

   Replace `your-repository-url` with the actual URL of your project repository:
   ```bash
   git clone https://your-repository-url.git
   cd your-project-directory
   ```
   Change `your-project-directory` to the name of the folder where your project is located.

4. **Install Required Packages:**
   
   Within the activated virtual environment, install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Requirements

This project requires the following Python libraries:

- `python-dotenv`: For loading environment variables.
- `requests`: To make HTTP requests.
- `pexels_api`: A wrapper for the Pexels API.

Ensure Python 3.x is installed on your machine to successfully run the project.

## Usage

To start the application, execute the following command from the root directory of the project:
```bash
python main.py
```

This script initializes the application, fetching images based on the specified search query within `main.py`. By default, the application searches for "cats". Adjust the search query in the `search_api` parameter of `main.py` to explore different content.

## Project Structure

- `main.py`: The main Python script that executes the application logic.
- `api/connector.py`: Contains the `pexel` class for interacting with the Pexels API.
- `requirements.txt`: Lists all the necessary Python packages.

### Interacting with the Application

Once the application is running, it will print out details for each fetched image, including the photographer's name, photo URL, and the URL for the original image size.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes. For major changes, please open an issue first to discuss what you would like to change.
