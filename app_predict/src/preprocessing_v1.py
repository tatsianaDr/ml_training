import re

def clean_html_string(review):
    return re.sub(r'<br.*?>', ' ', review)

def split_digit_letters_string(review):
    review = re.sub(r'(\d+)', r' \1 ', review)
    return re.sub(r'_+', r' ', review)

def split_ending(review):
    return review.replace('\'', ' ', )

def preprocessing_text(review):
    return clean_html_string(split_digit_letters_string(split_ending(review.lower())))