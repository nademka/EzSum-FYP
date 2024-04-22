# Dyslexia_summariser.py
from Base import T5Summarization
import re


class DyslexiaSummarization(T5Summarization):
    def find_first_syllable(self, text):
        """ Finds the first syllable in a text string using a regular expression. """
        match = re.search(r'\b\w*[aeiouAEIOU]\w*', text)
        return match.group(0) if match else ""

    def simplify_text(self, text):
        """ Generate a simplified summary of the text to make it easier to read for users with dyslexia. """
        input_ids = self.preprocess_text("summarize: " + text)
        simplified_ids = self.model.generate(
            input_ids, max_length=80, min_length=30, length_penalty=1.0, num_beams=4, early_stopping=True
        )
        simplified_text = self.tokenizer.decode(simplified_ids[0], skip_special_tokens=True)
        first_syllable = self.find_first_syllable(simplified_text)
        # Bold the first syllable for emphasis
        return re.sub(re.escape(first_syllable), f"**{first_syllable}**", simplified_text,
                      1) if first_syllable else simplified_text


# Public function to be imported by app.py
def summarize(text):
    """ Public function to simplify text based on dyslexia summarization criteria. """
    model = DyslexiaSummarization()
    return model.simplify_text(text)
