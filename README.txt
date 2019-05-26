Battery Electric Vehicle (BEV) Ranges

The ranges of all current (as of 2019-05-25) BEVs in the US, according
to the raw data from fueleconomy.gov:

    https://www.fueleconomy.gov/feg/download.shtml

Steps:
* Download the zipped CSV from the URL above
* Filter by fuelType1 = Electric
* Sort by rangeA
* Limited to the following columns:
  - make
  - model
  - rangeA
  - year
* Saved data above as "range.csv"
* Aggregated results that differ only by year and saved results as
  "range-years.csv"
* Saved data above as "range-years.csv"
* Limited to currently sold vehicles and saved results as
  "range-years-current.csv"
