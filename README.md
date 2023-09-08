from github import Github

# Your GitHub personal access token
# Replace with your actual token
access_token = 'YOUR_ACCESS_TOKEN'

# Repository details
owner = 'your-username'
repo_name = 'your-repository'

# README content
README_CONTENT = """
# Quote and System Information Display

This is a Python application that displays a random quote, current time, and battery information on your desktop. It provides a minimalistic and customizable way to keep track of time and battery status while being inspired by random quotes.

## Features

- **Random Quote**: The application displays a random quote with adjustable font size.

- **Digital Clock**: A digital clock is shown with customizable font size.

- **Battery Status**: The current battery percentage and status (charging or discharging) are displayed with customizable font size.

- **Transparency**: The application window supports transparency for a sleek and unobtrusive appearance.

## Getting Started

### Prerequisites

- Python 3.x
- GTK 3 library
- Cairo library
- psutil library

You can install the required libraries using pip:

```bash
pip install pycairo psutil
