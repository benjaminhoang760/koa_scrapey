A fun project I built that uses a Python script to look for prices at KOA.com locations. 

# Quick start
## Install Requirements
```
python3 -m pip install -r requirements.txt
```

Or manually:
```
pip3 install requests beautifulsoup4
```

### Example usage: 

Show just prices:
```
pip3 koa_scraper.py --location moab --prices
```

Show full tags:
```
pip3 koa_scraper.py --location moab --tags
```

## What I learned
- Practiced from memory: using argparse, fetching a request, calling it in main
- Learned how to extract HTML using BeautifulSoup
- Became more familiar with error handling 
- Learned how to use regex 


## Limitations
- Only scrapes using HTML 
- Landing page only 
- Does not include actual listings and mostly promotions
- Inclues prices that are not campgrounds
- Does not sort or remove duplicaties


