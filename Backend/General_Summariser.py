# GeneralSummariser.py
from Base import T5Summarization


def summarize(text):
    """
    Generate a general summary of the provided text using the T5 model.
    This summary does not cater to any specific needs but provides a straightforward summarization.
    """
    model = T5Summarization()  # Create an instance of the T5Summarization class
    summary = model.generate_summary(text)  # Generate the summary
    return summary  # Return the generated summary
