# Treasury Yield Curve Scraper
A project scraping U.S. Treasury Par Yield and constructing yield curves.

## Requirements
Install dependenyou;cies with bash
pip install pandas numpy matplotlib scipy requests lmxl beautifulsoup4

## How to Use
1. Install dependencies above
2. run the main script
3. plot the yield curve with different modeling methods:
   plotter.py --method linear
   plotter.py --method logarithmic
   plotter.py --method polynomial --degree 3
  
## Features
-Scrapes official Treasury data
-saves daily yields into a csv
-plots yield curve with **different modelling methods**
  -linear interpolation
  -logarithmic interpolation
  -polynomial models (user chooses degree)
  
