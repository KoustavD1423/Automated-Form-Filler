Here's the content formatted for a README.md file:

---

# Automated Google Form Filler And SMTP Based Email Sender

This project automates the filling and submission of a Google Form using Selenium and provides a Flask web application to send an email with the required files.

## Project Structure

```
selenium_assignment/
├── app.py
├── form.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── confirmation_page.png
    ├── your_resume.pdf
    └── work_samples.zip
```

## Requirements

- Python 3.x
- Flask
- Flask-Mail
- Selenium
- Chrome WebDriver

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/KoustavD1423/selenium_assignment.git
    cd selenium_assignment
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Update email configuration:**
    - Edit `app.py` and update the email configuration (`MAIL_USERNAME`, `MAIL_PASSWORD`, etc.).

4. **Prepare required files:**
    - Ensure `confirmation_page.png`, `resume.pdf`, are placed in the `static` directory.

## Usage

### Running the form-filling script

1. **Execute the `form.py` script to automatically fill out and submit the Google Form. This script will also save a screenshot of the confirmation page in the `static` directory.**

    ```bash
    python form.py
    ```

### Running the Flask application

1. **Start the Flask server by executing the `app.py` script. This will start a local web server.**

    ```bash
    python app.py
    ```

2. **Open your browser and navigate to `http://127.0.0.1:5000/`.**

3. **Click the "Send Email" button to send the email with the required attachments.**

## Author

- [Koustav Das](https://github.com/KoustavD1423)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
