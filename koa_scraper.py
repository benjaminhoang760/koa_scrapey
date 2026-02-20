import re, requests, argparse 
from bs4 import BeautifulSoup

def parser(): 
    p = argparse.ArgumentParser()
    p.add_argument("--location", default="Moab") 
    p.add_argument("--prices", action="store_true", help="Extracts only the price")
    p.add_argument("--tags", action="store_true", help="includes parent tag")
    p.add_argument("--save", action="store_true", help="saves file to koa_prices.txt")
    return p

def fetch(location): 
    url = f"https://koa.com/campgrounds/{location}/"
    headers = {'User-Agent': "benhoang"}
    print(f'...Fetching lowest prices on {url}')
    try: 
        r = requests.get(url, headers=headers,timeout=10)
        r.raise_for_status()
        return r.text
    except requests.RequestException as e: 
        print(f"Error {e}")
        return None

def extract_prices(html): 
    try: 
        soup = BeautifulSoup(str(html), 'html.parser')
        dollar_tags = soup.find_all(string=lambda text: '$' in text)
        campground_name = soup.find('h1').text
        parent_tags = []
        prices = re.findall(r"\$\d+(?:\.\d{2})?", str(dollar_tags))
        for item in dollar_tags: 
            if re.findall(r"\$\d+(?:\.\d{2})?", str(item)):
                parent_tags.append(item)
        return campground_name, parent_tags, prices
    except AttributeError as e: 
        print(f"Error: {e}")
        return "Unknown campground", [], []
    
def save_file(path, data): 
    with open(path, 'w') as file: 
        file.write(data)

def main(): 
    args = parser().parse_args()
    html = fetch(args.location)
    name, tags, price = extract_prices(html)
    if args.prices or not args.tags:
        for item in price:
            print(item)
    if args.tags:
        print(f"Campground name: {name}")
        for item in tags:
            print(f"{item}")
    if args.save and html is not None: 
        with open('koa_prices.txt', 'w',) as file: 
            file.write(f"Campground: {name}\n")
            file.write(f"Tags: {tags}\n")
            file.write(f"Prices: {price}")
        print(f"File saved to: koa_prices.txt")

if __name__ == "__main__":
    main()