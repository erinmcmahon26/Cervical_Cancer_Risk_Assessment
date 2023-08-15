# Cervical_Cancer_Risk_Assessment
       
## Cervical Cancer Image Model
* <b>CervicalCancerImages_EDA.ipynb</b>:  

## Cervical Cancer Risk Factors Model
* <b>RiskFactorEDA.ipynb</b>: Julia's initial work with the tabular dataset from Kaggle. Plan to continue working with it on Wednesday. Data sourced from the kaggle dataset linked in project goals: https://www.kaggle.com/code/mlalasa2170277/rf-cervical-cancer-classification-99-acc 

## Find a Provider Near You
* <b>npi_filtering.ipynb</b>: Initial exploration and filtering of raw NPI data.  Data is filtered from 7.6 million entries down to ~400k and from 330 columns down to 32.  Resulting data includes only physicians actively practicing in the US who could be reasonably expected to perform pap smears (i.e. OB/GYNs, Family, and Internal Medicine). Note: Raw data for the NPI Registry can be found here: https://download.cms.gov/nppes/NPI_Files.html

* <b>prepare_database.ipynb</b>: This notebook sets up batch geocoding scripts, merging the resulting data, and column manipulations for formatting, aggregations, and more descriptive content.  At the end, the prepared data is pushed into a PostgreSQL database table.

* <b>geospatial_queries.ipynb</b>: Testing geospatial queries and features for the streamlit app.

<b> TEST part 2 </b>

* <b>streamlit_test.py</b>: Minimal streamlit app containing all functionality for the find a provider feature.  Includes functionality to search by address or search by current location, and outputs an interactive map and table.
