from src.services import allservices


def extract_keywords_from_website(website):
    return allservices.extract_keywords_from_website(website)


if __name__ == '__main__':
    website = "https://saurabhy27.github.io"
    print(extract_keywords_from_website(website))