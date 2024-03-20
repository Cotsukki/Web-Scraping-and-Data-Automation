from playwright.async_api import async_playwright

async def run(playwright):
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto("https://services2.hdb.gov.sg/webapp/BR12AWRentalEnq/BR12PSearch.jsp")
    if await page.is_visible('.js-toggle-alert-bar'):
        await page.click('.js-toggle-alert-bar')
        print("Alert Closed")
    await page.wait_for_timeout(2000)
    await page.select_option('select#selTown', 'AMK')
    await page.select_option('select#selFlatType', '02')
    await page.select_option('#dteMthFr', 'March 2024')
    await page.select_option('#dteMtTo', 'March 2024')
    async with page.expect_navigation(wait_until="networkidle"):
        await page.click("#btnSearch")
    print("Clicked 'I Accept' Button and waited for the page to reload")
    await page.wait_for_timeout(2000)
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

import asyncio
asyncio.run(main())
