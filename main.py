import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # فتح متصفح Chromium بخصائص الموبايل
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.210 Mobile Safari/537.36",
            viewport={"width": 390, "height": 844}
        )
        page = await context.new_page()
        
        try:
            print("🚀 Connecting to blog...")
            await page.goto("https://loveoooouuu.blogspot.com/", timeout=60000)
            
            # انتظار 10 ثواني لتحميل إعلانات PopCash بالكامل
            print("⏳ Waiting for ads to load...")
            await page.wait_for_timeout(10000)
            
            # محاكاة الحركة والتفاعل البشري
            await page.mouse.wheel(0, 500)
            await page.wait_for_timeout(2000)
            
            await page.tap("body")
            print("✅ Visit completed successfully!")
            
        except Exception as e:
            print(f"❌ Error during visit: {e}")
            
        finally:
            await context.close()
            await browser.close()

if __name__ == "__main__":
    try:
        asyncio.run(run())
    except Exception as e:
        print(f"Critical script failure: {e}")
        
