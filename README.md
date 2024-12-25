# Twitter_Sel
### README for Running the Project

#### Project Overview
This project automates the process of logging into Twitter, scraping trending topics, storing them in MongoDB, and displaying the data on a Flask-based web application. It consists of the following components:
1. A **Selenium** script to log into Twitter and scrape trending topics.
2. A **Flask web app** to display the trending topics and execute the scraping script on demand.
3. **MongoDB** for storing the scraped trending topics.

---

### Requirements

1. **Python**: Ensure Python 3.8+ is installed.
2. **ChromeDriver**: Install ChromeDriver and ensure its path is configured correctly.
3. **Google Chrome**: The script uses Chrome for automation.
4. **MongoDB**: Install MongoDB locally or use a remote MongoDB instance.
5. **Environment Variables**:
   - `username`: Your Twitter username/email.
   - `password`: Your Twitter password.
6. **Required Libraries**:
   Install the dependencies using the following command:
   ```bash
   pip install flask pymongo requests selenium python-dotenv
   ```

---

### File Structure
Ensure your files are organized as follows:
```
project/
│
├── main.py                   # Selenium script for scraping
├── server.py                    # Flask application
├── templates/
│   └── index.html            # Frontend template
├── .env                      # Environment variables
├── requirements.txt          # Python dependencies
└── chromedriver              # ChromeDriver binary
```

---

### Steps to Run the Project

#### 1. Setup MongoDB
1. Start your local MongoDB instance:
   ```bash
   mongod
   ```
   By default, MongoDB will run on `localhost:27017`.

2. Create a database and collection:
   - Database: `twitter_scraper`
   - Collection: `trending_topics`

#### 2. Configure Environment Variables
Create a `.env` file in the project directory with the following content:
```
username=your_twitter_username
password=your_twitter_password
```

#### 3. Test the Selenium Script
1. Open `main.py`.
2. Update the path to ChromeDriver (`CHROMEDRIVER_PATH`) if necessary.
3. Run the script to ensure it logs in, scrapes trends, and stores data in MongoDB:
   ```bash
   python main.py
   ```
   You should see the scraped trends printed in the terminal and saved in the `trending_topics` collection in MongoDB.

#### 4. Run the Flask Application
1. Start the Flask app:
   ```bash
   python server.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```
3. You can:
   - View the latest trends stored in MongoDB.
   - Click the "Run Script" button to execute the Selenium scraper and update the database.

#### 5. Access Trending Topics
- The trending topics will be displayed on the homepage.
- Timestamp of the last scrape will also be shown.

---



### Commands for Quick Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start MongoDB:
   ```bash
   mongod
   ```
3. Run the Selenium script:
   ```bash
   python main.py
   ```
4. Start the Flask web app:
   ```bash
   python server.py
   ```

Enjoy exploring Twitter trends!