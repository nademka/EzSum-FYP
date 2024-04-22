# ADHD_summariser.py
import nltk
from nltk.tokenize import sent_tokenize
from Base import T5Summarization  # Assuming this module correctly set up and exists

# Ensure nltk resources are downloaded
nltk.download('punkt')


def summarize(text):
    """ Generate a summary and format it in bullet points. """
    model = T5Summarization()
    summary = model.generate_summary(text)
    return format_summary_in_bullets(summary)


def format_summary_in_bullets(summary):
    """ Convert summary text into a bulleted list. """
    sentences = sent_tokenize(summary)
    return "\n".join(f"- {sentence.strip()}" for sentence in sentences)
