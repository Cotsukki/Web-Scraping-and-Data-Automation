from playwright.sync_api import sync_playwright
import csv
def fetch_table_data(page, flat_type):
    rows = page.query_selector_all("div#panelResults table.paginated tbody tr")
    data = []
    for row in rows:
        rental_month = row.query_selector('td[data-label="Rental Commencement Month"]').text_content().strip()
        if "Mar 2024" in rental_month:
            block_no = row.query_selector('td[data-label="Block No."]').text_content().strip()
            street_name = row.query_selector('td[data-label="Street Name"]').text_content().strip()
            monthly_rent = row.query_selector('td[data-label="Monthly Rent (S$)"]').text_content().strip()
            data.append([rental_month, block_no, street_name, monthly_rent, flat_type])
    return data

def generate_csv(data, filename="output.csv"):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Rental Commencement Month", "Block No.", "Street Name", "Monthly Rent (S$)", "Flat Type"])
        writer.writerows(data)

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://services2.hdb.gov.sg/webapp/BR12AWRentalEnq/BR12PSearch.jsp")
    
    if page.is_visible('.js-toggle-alert-bar'):
        page.click('.js-toggle-alert-bar')

    town_options = ["AMK", "BD", "BH", "BB", "BM", "BP", "BT", "CT", "CCK", "CL", "GL", "HG", "JE", "JW", "KWN", "MP", "PRC", "PG", "QT", "SB", "SK", "SGN", "TAP", "TG", "TP", "WL", "YS"]
    flat_type_options = ["01", "02", "03", "04", "05", "06", "08"]
    all_data = []

    for town in town_options:
        for flat_type in flat_type_options:
            page.select_option('select#selTown', town)
            page.select_option('select#selFlatType', flat_type)
            page.click("#btnSearch")
            page.wait_for_timeout(5000)
            data = fetch_table_data(page, flat_type)
            all_data.extend(data)
            page.goto("https://services2.hdb.gov.sg/webapp/BR12AWRentalEnq/BR12PSearch.jsp")
            page.wait_for_selector('select#selTown', state="visible")
    generate_csv(all_data, "towns_flat_types_data_output.csv")
    print(f"CSV file has been generated with {len(all_data)} rows.")
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
