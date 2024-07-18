---
### Automated Google Form Filling

1. **Selection of Tools**: 
   - I chose Selenium for web automation due to its capabilities in simulating user interactions with web applications. ChromeDriver was used as the WebDriver to control the Chrome browser.

2. **Setting Up the Environment**: 
   - I ensured that Python and necessary libraries (Selenium, ChromeDriver) were installed.
   - Installed required Python packages using `pip install selenium`.

3. **Writing the Automation Script**:
   - The script `form.py` was written to:
     - Open the Google Form URL.
     - Locate the input fields using appropriate selectors (like XPATH).
     - Enter the required data into these fields.
     - Submit the form and capture a screenshot of the confirmation page.

4. **Running the Script**:
   - Executed the `form.py` script to automatically fill and submit the Google Form, and saved the confirmation screenshot.

### Flask Application for Email Sending

1. **Selection of Tools**:
   - I chose Flask for the web application framework due to its simplicity and Flask-Mail for handling email sending.

2. **Setting Up the Environment**:
   - Installed Flask and Flask-Mail using `pip install Flask Flask-Mail`.
   - Configured the Flask application in `app.py`.

3. **Email Configuration**:
   - Configured SMTP settings for sending emails via Gmail by providing the SMTP server details, port, and login credentials.
   - Enabled "Less secure app access" in my Google account to allow the Flask app to send emails.

4. **Building the Flask App**:
   - Created the `app.py` file to define routes for the Flask application.
   - Set up the `/` route to render an HTML form for email sending.
   - Set up the `/send_email` route to handle the form submission, construct the email with attachments, and send it using Flask-Mail.

5. **Running the Flask Application**:
   - Executed the `app.py` script to start the Flask server.
   - Opened the web browser and navigated to `http://127.0.0.1:5000/` to access the email sending form.
   - Submitted the form to send the email with the attachments, including the screenshot of the Google Form submission confirmation and my resume.

### Final Steps

- Ensured all necessary files (confirmation screenshot, resume, documentation) were placed in the `static` directory for attachment in the email.
- Verified that the email was sent correctly with all the required attachments.

This approach provided a seamless way to automate form submission and email sending using Python's Selenium for web automation and Flask for web application development.

---
