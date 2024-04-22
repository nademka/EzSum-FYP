# ASD_summariser.py
from Base import T5Summarization


class ASDSummarization(T5Summarization):
    def generate_summary(self, text, detail_level='high'):
        """
        Generate a summary of the text using the T5 model, tailored for users with ASD.
        Args:
            text (str): The input text to summarize.
            detail_level (str): 'high' for detailed summaries, 'low' for high-level overviews.
        Returns:
            str: The summary of the input text.
        """
        # Adjust the maximum length parameter based on the desired detail level
        max_length = 150 if detail_level == 'high' else 40  # More detailed or more concise

        # Preprocess and tokenize text using inherited method
        input_ids = self.preprocess_text("summarize: " + text)

        # Generate summary using specified summary lengths
        summary_ids = self.model.generate(
            input_ids,
            max_length=max_length,
            min_length=20,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)


# Public function to be imported by app.py
def summarize(text, detail_level='high'):
    """
    Public function to summarize text based on ASD summarization criteria.
    """
    model = ASDSummarization()
    return model.generate_summary(text, detail_level)
