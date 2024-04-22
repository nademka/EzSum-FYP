# Anxiety_Summarizer.py
from Base import T5Summarization
import re


class AnxietyDisorderSummarization(T5Summarization):
    def __init__(self, model_name="t5-base"):
        super().__init__(model_name=model_name)

    def generate_anxiety_friendly_summary(self, text, max_length=150, min_length=40):
        """
        Generate a summary that considers the sensitivities of users with anxiety disorders.
        """
        processed_text = self.preprocess_for_anxiety(text)
        input_ids = self.preprocess_text(processed_text)

        summary_ids = self.model.generate(
            input_ids,
            max_length=max_length,
            min_length=min_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    def preprocess_for_anxiety(self, text):
        """
        Adjust text to avoid triggers and emphasize positive information.
        """
        triggers = ["crash", "death", "violence"]
        for trigger in triggers:
            text = re.sub(r"\b{}\b".format(trigger), "[sensitive content]", text)

        positive_replacements = {
            "challenges": "opportunities",
            "difficult": "interesting",
            "problem": "opportunity"
        }
        for word, replacement in positive_replacements.items():
            text = text.replace(word, replacement)

        return text


# Instantiate the model globally to reuse it across calls
anxiety_model = AnxietyDisorderSummarization()


# Public function to be imported by app.py
def summarize(text):
    """
    Public function to generate anxiety-friendly summaries using the globally instantiated model.
    This avoids the inefficiency of re-instantiating the model on every function call.
    """
    return anxiety_model.generate_anxiety_friendly_summary(text)
