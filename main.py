import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # بنفتح متصفح حقيقي (Chromium)
        browser = await p.chromium.launch(headless=True)
        # بنعمل سياق متصفح جديد (موبايل)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.210 Mobile Safari/537.36",
            viewport={"width": 390, "height": 844}
        )
        page = await context.new_page()
        
        # بنزور المدونة
        print("🚀 Visiting blog...")
        await page.goto("https://loveoooouuu.blogspot.com/")
        
        # انتظار 10 ثواني عشان الإعلانات تحمل (أهم خطوة)
        await page.wait_for_timeout(10000)
        
        # بنعمل سكرول خفيف عشان بوب كاش يحس إن فيه حركة
        await page.mouse.wheel(0, 500)
        await page.wait_for_timeout(2000)
        
        # ضغطة واحدة
        await page.tap("body")
        print("✅ Visit done!")
        
        await browser.close()

asyncio.run(run())
