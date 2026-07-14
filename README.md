# Google Maps Data Automation Tool

## Overview

A Python-based automation tool designed to collect and organize business information from Google Maps through browser automation.

The project automates the process of searching for professionals and businesses in specific locations, extracting available information such as names and phone numbers, and exporting the collected data into structured Excel reports.

This project demonstrates practical applications of Python for **web automation, data extraction, data processing, and workflow optimization**.

---

## Features

- Automated Google Maps navigation using Selenium WebDriver
- Dynamic searches based on profession and location
- Extraction of business names and available phone numbers
- Automated organization of collected data
- Excel report generation using Pandas
- Support for multiple search categories in a single execution
- Automated browser interaction without manual intervention

---

## Technologies Used

- **Python 3**
- **Selenium WebDriver**
- **ChromeDriver**
- **webdriver-manager**
- **Pandas**
- **OpenPyXL**

---

## How It Works

The automation workflow follows these steps:

1. Initializes a controlled Chrome browser session using Selenium.
2. Opens Google Maps automatically.
3. Searches for specific professions and locations.
4. Navigates through search results.
5. Extracts available business information.
6. Processes the collected data using Pandas.
7. Generates a structured Excel report.

---

## Example Workflow

### Input

```
Profession: Doctor
Location: Santarém, PA
```

### Process

```
Google Maps Search
        ↓
Automated Browser Navigation
        ↓
Data Extraction
        ↓
Data Processing
        ↓
Excel Report Generation
```

### Output

```
contatos_reais_santarem.xlsx
```

Example data structure:

| Name | Profession | Phone |
|------|------------|-------|
| Example Business | Doctor | +55 XX XXXXX-XXXX |

---

## Project Structure

```
google-maps-data-automation/
│
├── main.py
├── requirements.txt
├── README.md
└── contatos_reais_santarem.xlsx
```

---


## Skills Demonstrated

This project showcases experience with:

- Python automation
- Browser automation using Selenium
- Web data extraction
- Data processing with Pandas
- Spreadsheet generation
- File manipulation
- Structured data handling
- Problem-solving and workflow optimization

---

## Future Improvements

Possible improvements include:

- Implementing a database for data storage
- Adding a graphical user interface (GUI)
- Improving error handling and logging
- Adding configurable search parameters
- Creating asynchronous processing for better performance
- Integrating official APIs when available

---

## Author

**Lucas Bizerra da Silva**

Junior Software Developer

GitHub: https://github.com/Lucasb310
