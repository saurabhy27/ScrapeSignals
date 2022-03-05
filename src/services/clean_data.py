import pandas as pd
from boilerpy3.extractors import ArticleExtractor

extractor = ArticleExtractor()


def clean_data(file_name):
    df = pd.read_csv(file_name)
    for i in range(1, len(df)):
        yield extractor.get_content(df.iloc[i, 2])
