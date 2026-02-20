import re, requests, argparse 
from bs4 import BeautifulSoup

def parser(): 
    p = argparse.ArgumentParser()
    p.add_argument("--location", default="Moab") 
    return p

def fetch(location): 
    url = f"https://koa.com/campgrounds/{location}/"
    headers = {'User-Agent': "benhoang"}
    print(f'Fetching lowest prices for {url}')
    try: 
        r = requests.get(url, headers=headers,timeout=5)
        r.raise_for_status()
        return r.text
    except requests.RequestException as e: 
        print(f"Error {e}")

def extract_prices(html): 
    soup = BeautifulSoup(str(html), 'html.parser')
    dollar_tags = soup.find_all(string=lambda text: '$' in text)
    campground_name = soup.find('h1').text
    parent_tags = []
    for item in dollar_tags: 
        if re.findall(r"\$\d+(?:\.\d{2})?", str(item)):
            parent_tags.append(item)
    return campground_name, parent_tags

def main(): 
    args = parser().parse_args()
    html = fetch(args.location)
    result = extract_prices(html)
    print(result)

if __name__ == "__main__":
    main()