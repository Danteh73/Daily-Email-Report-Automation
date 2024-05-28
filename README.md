# Daily Email Automator

The Daily Email Automator is a Python script designed to automate the process of sending daily email reports. Whether you need to distribute sales updates, project status summaries, or any other type of daily report, this script simplifies the task by fetching data, generating reports, and sending them via email to specified recipients.

## Purpose

The purpose of this project is to streamline the daily reporting process for individuals and organizations. By automating the generation and distribution of reports, users can save time, reduce manual errors, and ensure timely delivery of essential updates.

## How to Use

1. **Installation**:
   - Clone or download the repository to your local machine.

2. **Dependencies**:
   - Ensure you have Python installed on your system.
   - Install the required dependencies by running:
     ```
     pip install -r requirements.txt
     ```

3. **Configuration**:
   - Open the `config.py` file and update the email configuration settings such as sender email address, SMTP server details, recipients, etc.

4. **Customization**:
   - Customize the email content, attachment, and scheduling options in the `send_email` function within the `daily_email_report.py` script according to your requirements.

5. **Execution**:
   - Run the `daily_email_report.py` script using Python:
     ```
     python daily_email_report.py
     ```

6. **Scheduling**:
   - If desired, use task scheduling tools (e.g., `cron` on Unix-based systems, Task Scheduler on Windows) to automate the execution of the script at your preferred time daily.

## Dependencies

- Python 3.x
- `schedule` library (install via `pip install schedule`)

