Rental Listings Data Automation Project

## Project Overview

This project involves the development of a web scraping and automation script to extract rental listing data from a government housing website. The goal was to collect detailed information on rental prices, block numbers, street names, and flat types for various towns, focusing specifically on listings commencing in March 2024. The data extracted through this automated process is structured and saved into CSV files for easy analysis and insights.

## Technologies Used

- **Language**: Python 3.11.8
- **Web Scraping Framework**: Playwright
- **Data Handling**: CSV module for Python

## Features

- Automates web navigation and interacts with dropdown menus to select various town and flat type combinations.
- Extracts rental listing information, including rental commencement month, block number, street name, and monthly rent.
- Filters listings based on a specific rental commencement month ("March 2024").
- Generates a comprehensive CSV file containing all collected data for further analysis.

## How to Run the Script

### Prerequisites

Ensure you have Python 3.8 or later installed on your system. Additionally, you will need to install Playwright. This can be done by running the following command in your terminal:

```
pip install playwright
playwright install
```

### Running the Script

1. Clone the repository or download the script to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using Python:

```
python SyncHDBSGAutomation.py
```

### Output

The script will generate a CSV file named `towns_flat_types_data_output.csv` in the same directory from which the script is run. This file contains the structured data extracted from the website, including the additional column indicating the flat type for each listing.

Feel free to modify the README file to include any additional sections you think are necessary, such as a section on challenges faced during the project, lessons learned, or future improvements you might consider.
