# Battery Electric Vehicle (BEV) Range 

The range of all BEVs available in the US, according to the data from
fueleconomy.gov:

<https://www.fueleconomy.gov/feg/download.shtml>

The data is current as of 2019-05-25.

# Steps:
1. Download the zipped CSV from the URL above.
2. Filter by `fuelType1 = Electric`.
3. Sort by `rangeA` in descending order.
4. Show the following columns: `make`, `model`, `rangeA`, and `year`.
5. Save as `range.csv`.
6. Group by make, model, range, and aggregate years.
7. Save as `range-years.csv`.
8. Limited to currently sold vehicles and save as range-years-current.csv`.
9. Save as `range-years-current.csv`.
10. ./plot.py range-years-current.csv chart,svg
11. convert -antialias -scale 1024x1024 chart.{svg,png}
