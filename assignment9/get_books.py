
# Task 3: Write a Program to Extract this Data

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json

# Set up headless driver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

try:
    # Load the search results page
    driver.get(
        "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
    )
    
    # Find all result entries by the class in Task 2
    entries = driver.find_elements(
        By.CSS_SELECTOR,
        "li.cp-search-result-item"  
    )
    print(f"Found {len(entries)} entries")

    results = []
    for li in entries:
        # Get the book title
        title_el = li.find_element(
            By.CSS_SELECTOR,
            "h2.cp-title a span.title-content"  
        )
        title = title_el.text.strip()
        
        # Get author(s)
        author_els = li.find_elements(
            By.CSS_SELECTOR,
            "span.cp-by-author-block a"
        )
        authors = "; ".join(a.text.strip() for a in author_els)
        
        # Get format and year
        fmt_el = li.find_element(
            By.CSS_SELECTOR,
            "span.display-info-primary"
        )
        fmt_year = fmt_el.text.strip()
        
        results.append({
            "Title": title,
            "Author": authors,
            "Format-Year": fmt_year
        })
    
    # Turn into DataFrame and print
    df = pd.DataFrame(results)
    print(df)
    
    # Task 4: Write out the Data (Save to CSV and JSON)
    df.to_csv("get_books.csv", index=False)
    with open("get_books.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

finally:
    driver.quit()










