from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    #browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://services2.hdb.gov.sg/webapp/BR12AWRentalEnq/BR12PSearch.jsp")
    if page.is_visible('.js-toggle-alert-bar'):
        page.click('.js-toggle-alert-bar')
        print("Alert Closed")
    page.wait_for_timeout(2000)
    page.select_option('select#selTown', 'AMK')
    page.select_option('select#selFlatType', '02')
    # page.select_option('dteMthFr', 'March 2024')
    # page.select_option('dteMtTo', 'March 2024')
    with page.expect_navigation():
        page.click("#btnSearch")
    if page.is_visible("#btnSearch"):
        page.click("#btnSearch")
        print("Clicked 'I Accept' Button")
    page.wait_for_timeout(2000)    
    #page.select
    #page.fill()
    
    browser.close()

with sync_playwright() as playwright:
    run(playwright)