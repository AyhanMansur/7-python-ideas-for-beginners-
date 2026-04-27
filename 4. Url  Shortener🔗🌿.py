# url_shortener.py
import requests
import sys

def shorten_url(url):
    api_url = "https://api.tinyurl.com/create"
    headers = {"Content-Type": "application/json"}
    payload = {"url": url}
    
    # Note: TinyURL API requires an API key. For demo, we'll use a free service like 'cutt.ly' or 'bit.ly'
    # Here's an example using 'cutt.ly' (you need a free API key from cutt.ly)
    api_key = "YOUR_CUTTL_API_KEY"  # Replace with your API key
    endpoint = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    
    response = requests.get(endpoint)
    data = response.json()
    
    if data['status'] == 200:
        short_url = data['url']['shortLink']
        print(f"\n✅ Original URL: {url}")
        print(f"🔗 Short URL: {short_url}")
        return short_url
    else:
        print("❌ Error shortening URL.")
        return None

def main():
    url = input("Enter the URL to shorten: ")
    if url.startswith("http://") or url.startswith("https://"):
        shorten_url(url)
    else:
        print("❌ Please enter a valid URL starting with http:// or https://")

if __name__ == "__main__":
    main()