# CSV Dashboard

A universal data exploration tool built with Python and Streamlit. Upload any CSV file and instantly visualize your data — no configuration needed.

## Features

- **Data preview** — see the first rows of your dataset at a glance
- **Summary statistics** — rows, columns, and descriptive stats
- **Missing value detection** — instantly see which columns have missing data
- **Histogram** — explore the distribution of any numeric column
- **Bar chart** — visualize the most frequent values in any categorical column
- **Pie chart** — see proportions with an adjustable number of slices

## Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

## Getting Started

### Installation

```bash
git clone https://github.com/muecahitg/csv-dashboard.git
cd csv-dashboard
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501` and upload any CSV file.

## Usage

1. Upload a CSV file using the file uploader
2. Explore the data preview and summary statistics
3. Select columns to visualize with the histogram, bar chart, or pie chart
4. Adjust the number of values shown in each chart

## Example Dataset

Try it with the [Amazon Prime Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/amazon-prime-movies-and-tv-shows) dataset from Kaggle.
