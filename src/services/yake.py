import yake

kw_extractor = yake.KeywordExtractor()

def extaractKeywords(data):
    return kw_extractor.extract_keywords(data)
