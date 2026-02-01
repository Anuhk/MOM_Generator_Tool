
def clean_transcript(text):
    text = text.replace("\n", " ")
    return " ".join(text.split())
