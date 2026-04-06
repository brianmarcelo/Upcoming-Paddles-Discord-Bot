import requests
from bs4 import BeautifulSoup
import time

# UPA-A (United Pickleball Association) Scraper
def scrape_upaa():
    url = "https://upaa.unitedpickleball.com/approved-paddles/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        paddles = []
        table = soup.select_one('table.paddle-listing-table')
        if not table:
            return []
            
        rows = table.select('tbody tr.paddle-row')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 7:
                # Based on observation:
                # 0: empty, 1: img, 2: brand, 3: model, 4: model#, 5: thickness, 6: date
                img_tag = cols[1].find('img')
                brand = cols[2].get_text(strip=True)
                model = cols[3].get_text(strip=True)
                date_added = cols[6].get_text(strip=True)
                
                paddles.append({
                    'source': 'UPA-A',
                    'brand': brand,
                    'model': model,
                    'date_added': date_added,
                    'image_url': img_tag['src'] if img_tag and 'src' in img_tag.attrs else None,
                    'key': f"UPAA-{brand}-{model}"
                })
        return paddles
    except Exception as e:
        print(f"Error scraping UPAA: {e}")
        return []

# USA Pickleball (USAP) Scraper
def scrape_usap(pages=1):
    base_url = "https://equipment.usapickleball.org/paddle-list/"
    # More comprehensive headers to bypass basic anti-bot
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://equipment.usapickleball.org/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }
    
    all_paddles = []
    
    for page in range(1, pages + 1):
        url = f"{base_url}?pagenum={page}"
        try:
            # Using a session might help with cookies
            session = requests.Session()
            response = session.get(url, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Use gv-grid-row as the base for each paddle
            rows = soup.select('.gv-grid-row')
            
            for row in rows:
                brand = ""
                model = ""
                date_added = "Unknown"
                image_url = None
                
                # Robustly find fields by label
                fields = row.select('.gv-field-3-1, .gv-field-3-2, .gv-field-3-48, .gv-field-3-10, [class*="gv-field-"]')
                
                for field in fields:
                    label_tag = field.select_one('.gv-field-label')
                    if not label_tag: continue
                    label = label_tag.get_text(strip=True).lower()
                    value_tag = field.select_one('.gv-grid-value')
                    if not value_tag: continue
                    
                    if "brand" in label:
                        brand = value_tag.get_text(strip=True)
                    elif "model" in label:
                        model = value_tag.get_text(strip=True)
                    elif "added" in label:
                        date_added = value_tag.get_text(strip=True)
                    elif "enlarge" in label or "image" in label:
                        # Image is usually in the link OR an img tag
                        a_tag = value_tag.find('a')
                        img_tag = value_tag.find('img')
                        if a_tag and a_tag.get('href'):
                            image_url = a_tag['href']
                        elif img_tag and img_tag.get('src'):
                            image_url = img_tag['src']
                
                if brand and model:
                    if brand.lower() == 'brand': continue # Skip header if any
                    all_paddles.append({
                        'source': 'USA Pickleball',
                        'brand': brand,
                        'model': model,
                        'date_added': date_added,
                        'image_url': image_url,
                        'key': f"USAP-{brand}-{model}"
                    })
            time.sleep(2) 
        except Exception as e:
            print(f"Error scraping USAP page {page}: {e}")
            break
            
    return all_paddles

if __name__ == "__main__":
    # Test
    print("Testing UPA-A...")
    upaa = scrape_upaa()
    print(f"Found {len(upaa)} paddles from UPA-A.")
    if upaa: print(f"First item: {upaa[0]}")
    
    print("\nTesting USA Pickleball...")
    usap = scrape_usap(pages=1)
    print(f"Found {len(usap)} paddles from USA Pickleball First Page.")
    if usap: print(f"First item: {usap[0]}")
