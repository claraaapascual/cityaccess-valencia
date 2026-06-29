# CityAccess Valencia

CityAccess Valencia is an interactive civic-tech Streamlit application that uses open data from Valencia to identify neighbourhoods with weaker access to public services and explore where a new public facility could have the greatest potential impact.

## Purpose

The application is designed as a decision-support tool. It helps users:

- detect underserved neighbourhoods;
- compare possible intervention locations;
- estimate the potential impact of a new public facility;
- understand accessibility differences between neighbourhoods.

## Data

The application uses open data from Valencia:

- public facilities;
- neighbourhood boundaries;
- population by neighbourhood.

The data files are stored in the `data/` folder.

## Main Features

- accessibility assessment by public service type;
- priority-area detection;
- candidate-location comparison;
- before-and-after simulation;
- interpretable recommendation;
- monitoring and sensitivity checks.

## Run Locally

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Start the app:

```bash
streamlit run app.py
```

## Deploy On Streamlit Community Cloud

1. Push this repository to GitHub.
2. In Streamlit Community Cloud, create a new app from `claraaapascual/cityaccess-valencia`.
3. Set the main file path to `app.py`.
4. Keep the Python runtime defined in `runtime.txt`.

## Repository Structure

```text
cityaccess-valencia/
  app.py
  data/
  models/
  scripts/
  src/
  requirements.txt
  runtime.txt
```
