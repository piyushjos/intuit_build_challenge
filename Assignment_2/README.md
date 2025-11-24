# Sales Data Analysis (Assignment 2)

Analyze the provided classic cars sales dataset and print summary stats to the console.

## Quick start
- Python 3.8+ recommended (uses only stdlib).
- From the project root, run:  
  `python3 main.py`
- The script automatically reads `data/sales_data_sample.csv` and prints all results.

## Running Tests

This project uses Python’s built-in `unittest` framework.

Run all tests:
python -m unittest discover -s tests




## Sample output
Running `python3 main.py` prints all analyses:
```
=== Sales Analysis Results (Assignment 2) ===
Total revenue: 10032628.85

Revenue by region (COUNTRY):
  Australia: 630623.10
  Austria: 202062.53
  Belgium: 108412.62
  Canada: 224078.56
  Denmark: 245637.15
  Finland: 329581.91
  France: 1110916.52
  Germany: 220472.09
  Ireland: 57756.43
  Italy: 374674.31
  Japan: 188167.81
  Norway: 307463.70
  Philippines: 94015.73
  Singapore: 288488.41
  Spain: 1215686.92
  Sweden: 210014.21
  Switzerland: 117713.56
  UK: 478880.46
  USA: 3627982.83

Revenue by product line (PRODUCTLINE):
  Classic Cars: 3919615.66
  Motorcycles: 1166388.34
  Planes: 975003.57
  Ships: 714437.13
  Trains: 226243.47
  Trucks and Buses: 1127789.84
  Vintage Cars: 1903150.84

Monthly revenue (YYYY-MM):
  2003-01: 129753.60
  2003-02: 140836.19
  2003-03: 174504.90
  2003-04: 201609.55
  2003-05: 192673.11
  2003-06: 168082.56
  2003-07: 187731.88
  2003-08: 197809.30
  2003-09: 263973.36
  2003-10: 568290.97
  2003-11: 1029837.66
  2003-12: 261876.46
  2004-01: 316577.42
  2004-02: 311419.53
  2004-03: 205733.73
  2004-04: 206148.12
  2004-05: 273438.39
  2004-06: 286674.22
  2004-07: 327144.09
  2004-08: 461501.27
  2004-09: 320750.91
  2004-10: 552924.25
  2004-11: 1089048.01
  2004-12: 372802.66
  2005-01: 339543.42
  2005-02: 358186.18
  2005-03: 374262.76
  2005-04: 261633.29
  2005-05: 457861.06

Top 3 product lines by revenue:
  Classic Cars: 3919615.66
  Vintage Cars: 1903150.84
  Motorcycles: 1166388.34
```
