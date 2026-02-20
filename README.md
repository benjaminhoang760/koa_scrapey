A fun project I built that uses a Python script to look for prices at KOA.com locations. 

# Quick start
## Install Requirements
```
python3 install -r requirements.txt
```

Or manually:
```
python3 install requests beautifulsoup4
```

### Example usage: 

Show just prices:
```
python3 koa_scraper.py --location moab --prices
```

Show full tags:
```
python3 koa_scraper.py --location moab --tags
```

## What I learned
- Practiced from memory: using argparse, fetching a request, calling it in main
- Learned how to extract HTML using BeautifulSoup
- Became more familiar with error handling 
- Learned how to use regex 




