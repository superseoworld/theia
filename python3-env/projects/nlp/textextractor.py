from boilerpy3 import extractors


extractor = extractors.KeepEverythingExtractor()

# From a URL
content = extractor.get_content_from_url("https://www.whitebox.eu")
print(content)
