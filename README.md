# MEAL Data Analysis Project (World Bank Indicators)

This project demonstrates a simple, donor-ready MEAL (Monitoring, Evaluation, Accountability & Learning)
data pipeline using **public World Bank indicators**.

## What this project does

1. Downloads poverty and unemployment data for Kenya
2. Cleans and validates the data (MEAL-style checks)
3. Computes trends and year-on-year change
4. Produces clean visualizations
5. Exports CSV and Parquet files for reporting / Power BI

## How to run

### Using Docker

Ensure Docker is installed and running.

Build and run with Docker Compose:

```bash
docker-compose up --build
```

Or manually:

```bash
docker build -t meal-worldbank .
docker run -v $(pwd)/outputs:/app/outputs meal-worldbank
```

## Outputs folder 
- After runing the projects visit the output and data folder to see results folder 
- Additionally there is a power point file that explain the finding of the project. 

- CSV files → outputs /csv/
- Parquet files → outputs/parquet/
- Charts → outputs/ (PNG files)

This structure mirrors how MEAL teams organize analytical work for donors.
