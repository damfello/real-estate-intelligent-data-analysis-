# Real Estate Intelligent Data Analysis
### Real Estate in King County, WA, USA.

This repository contains an exploratory data analysis of the King County housing dataset (home sales in and around Seattle, USA). The project focuses on uncovering what drives house prices, evaluating return on investment (ROI) metrics across key dimensions, and turning data-driven insights into actionable recommendations for real estate clients.

# Client's requirements. 

Investor Zachary Brooks:
Looking to invest in real estate with specific requirements:
Historical houses in the best neighborhoods, and with the best ROI, based on the best time to buy a renovated or non renovated house.


### Main Objective: Maximize ROI with following specific requirements:

1. Historical houses
2. Renovated or no?
3. Best neighborhoods
4. Best timing to buy and sell a house within a year

## Project Overview & Methodology

To address the client's primary objective—maximizing return on investment (ROI)—the project connects to a PostgreSQL database, extracts and joins housing details and sales records, and engineers custom profitability metrics.

## Key Findings & Conclusions

## Key Findings & Visual Insights

![Real Estate Investment Insights](https://raw.githubusercontent.com/damfello/real-estate-intelligent-data-analysis-/main/assets/real-estate-insights.JPG)

* **Top ROI Segments:** Analysis indicates that homes built in the 1970s, without significant renovations, purchased in the month of October, and located in regions like South Seattle, generally offer the highest estimated return on investment.
* **Methodological Approach:** To reduce the distortion caused by extreme market outliers while keeping data volume high, a 10% trimmed mean was applied across categorical benchmarks.
* **Future Improvements:** Future phases of this project should implement advanced outlier treatment methods—such as Winsorization, multivariate anomaly detection (Isolation Forest), or log-transformations—to further refine price predictability and handle market skewness.

## Setup & Installation

### Prerequisites
* **Python** `>=3.13` (managed via [uv](https://github.com/astral-sh/uv))

### Quick Start
```bash
git clone <copied-ssh-url>
cd <repo-name>

# Install dependencies and set up the virtual environment
uv sync

### Accessing the Data

You can work with the data in two ways:
1. **Via PostgreSQL Database:** Configure your `.env` file and run.

> [!CAUTION]
> Your local `.env` file holds sensitive database credentials and must never be committed to version control.


2. **Via CSV Files:** Pre-exported CSV tables (`king_county_house_details.csv`, `king_county_house_sales.csv`, and the merged `king_county_house_details_sales.csv`) are already included inside the [**Data**](data/) folder for quick and easy loading without requiring a live database connection.

 Also you can find more details about the dataset in Kaggle: https://www.kaggle.com/datasets/vallabhadattap/kingcountyhousing


