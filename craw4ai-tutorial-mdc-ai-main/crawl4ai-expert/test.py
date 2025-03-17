import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

async def main():
    # Browser Configuration
    browser_config = BrowserConfig(
        headless=False,  # Show browser for debugging
        viewport_width=1366,
        viewport_height=768,
        text_mode=False,  # Keep images enabled
        java_script_enabled=True,
        verbose=True
    )

    # Crawl Run Configuration
    run_config = CrawlerRunConfig(
        word_count_threshold=50,        # Minimum words per content block
        exclude_external_links=True,    # Remove external links
        remove_overlay_elements=True,   # Remove popups/modals
        process_iframes=True            # Process iframe content
    )

    # Initialize the AsyncWebCrawler with the browser configuration
    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Run the crawl and fetch the content
        result = await crawler.arun(
            url="https://www.nbcnews.com/artificial-intelligence",
            config=run_config
        )
        print(result.markdown)  # Print clean markdown content

# Run the asyncio loop
if __name__ == "__main__":
    asyncio.run(main())
