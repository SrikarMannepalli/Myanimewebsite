import cfscrape

scraper = cfscrape.create_scraper()

print scraper.get("https://masterani.me/api/anime/256/detailed").content
