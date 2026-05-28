from scraper import fetch_funded_brands
from emailer import send_email

if __name__ == "__main__":
    print("Fetching funded brand news from the last 24 hours...")
    brands = fetch_funded_brands(hours=24)
    print(f"Found {len(brands)} funding-related articles.")
    send_email(brands)
