# Task 6: Scrape OWASP Top 10

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

# Headless setup again
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

try:
    driver.get("https://owasp.org/www-project-top-ten/")
    
    # Locate the title and the href link using XPath or find all risk items
    items = driver.find_elements(
        By.XPATH,
        "//h2[@id='top-10-web-application-security-risks']"
        "/following-sibling::ul[1]/li/a"
    )
    print("Vulnerability,URL")
    top10 = []
    for a in items[:10]:
        name = a.text.strip()
        link = a.get_attribute("href")
        top10.append({"Vulnerability": name, "URL": link})
        print(f"{name},{link}")
    
    # Write to CSV
    with open("owasp_top_10.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Vulnerability", "URL"])
        writer.writeheader()
        writer.writerows(top10)
    

finally:
    driver.quit()