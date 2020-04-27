import re
from pyvi import ViTokenizer

"""
Remove image, table, html tags from text
"""
def prepare_content(text):
    img_filter = "<img.*?>"
    table_filter = "<table(.|\n)*?</table>"
    tag_filter = "<.*?>"
    linebreak_filter = "\\n"
    result = text
    result = re.sub(img_filter,"",result)
    result = re.sub(table_filter,"",result)
    result = re.sub(tag_filter,"",result)
    result = re.sub(linebreak_filter,"",result)

    return result

def tokenize_content(text):
    return ViTokenizer.tokenize(text)

