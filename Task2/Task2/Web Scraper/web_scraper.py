import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin


def scrape_website(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        print("=" * 50)
        print("WEB SCRAPER")
        print("=" * 50)

        # -----------------------------
        # Website Title
        # -----------------------------
        title = soup.title.string.strip() if soup.title else "No Title"
        print("\nWebsite Title:")
        print(title)

        # -----------------------------
        # Headings
        # -----------------------------
        headings = []

        for tag in ["h1", "h2", "h3"]:
            for heading in soup.find_all(tag):
                headings.append({
                    "Tag": tag.upper(),
                    "Heading": heading.get_text(strip=True)
                })

        pd.DataFrame(headings).to_csv("headings.csv", index=False)

        # -----------------------------
        # Paragraphs
        # -----------------------------
        paragraphs = []

        for p in soup.find_all("p"):
            text = p.get_text(strip=True)
            if text:
                paragraphs.append({"Paragraph": text})

        pd.DataFrame(paragraphs).to_csv("paragraphs.csv", index=False)

        # -----------------------------
        # Links
        # -----------------------------
        links = []

        for link in soup.find_all("a", href=True):
            links.append({
                "Text": link.get_text(strip=True),
                "URL": urljoin(url, link["href"])
            })

        pd.DataFrame(links).to_csv("links.csv", index=False)

        # -----------------------------
        # Images
        # -----------------------------
        images = []

        for img in soup.find_all("img"):
            src = img.get("src")
            if src:
                images.append({
                    "Image URL": urljoin(url, src)
                })

        pd.DataFrame(images).to_csv("images.csv", index=False)

        # -----------------------------
        # Summary
        # -----------------------------
        print(f"\nTitle: {title}")
        print(f"Headings Found : {len(headings)}")
        print(f"Paragraphs Found : {len(paragraphs)}")
        print(f"Links Found : {len(links)}")
        print(f"Images Found : {len(images)}")

        print("\nData saved successfully!")
        print("Generated Files:")
        print("1. headings.csv")
        print("2. paragraphs.csv")
        print("3. links.csv")
        print("4. images.csv")

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)

    except requests.exceptions.ConnectionError:
        print("Connection Error! Check your internet connection.")

    except requests.exceptions.Timeout:
        print("Request Timed Out!")

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)


if __name__ == "__main__":
    print("=" * 50)
    print("Python Web Scraper")
    print("=" * 50)

    website = input("Enter Website URL (https://...): ").strip()

    if not website.startswith("http"):
        website = "https://" + website

    scrape_website(website)