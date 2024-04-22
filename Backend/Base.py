from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
from torch.utils.data import Dataset, DataLoader
import torch
import re
import nltk
from torch.nn import functional as F

# Ensure nltk is installed and download required resources
nltk.download('punkt', quiet=True)  # Set quiet=True to suppress console messages

class SummarizationDataset(Dataset):
    def __init__(self, texts, summaries, tokenizer, max_length=512):
        self.tokenizer = tokenizer
        self.texts = texts
        self.summaries = summaries
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        summary = self.summaries[idx]
        source = self.tokenizer.encode_plus("summarize: " + text, max_length=self.max_length, padding='max_length', truncation=True, return_tensors="pt")
        target = self.tokenizer.encode_plus(summary, max_length=self.max_length, padding='max_length', truncation=True, return_tensors="pt")
        return source.input_ids.squeeze(), target.input_ids.squeeze()

class T5Summarization:
    def __init__(self, model_name="t5-base"):
        config = T5Config.from_pretrained(model_name, output_hidden_states=True)
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name, config=config)

    def preprocess_text(self, text):
        cleaned_text = re.sub(r'\s+', ' ', text).strip()
        return self.tokenizer.encode("summarize: " + cleaned_text, return_tensors="pt")

    def generate_summary(self, text, max_length=300, min_length=150):
        input_ids = self.preprocess_text(text)
        summary_ids = self.model.generate(
            input_ids,
            max_length=max_length,
            min_length=min_length,
            length_penalty=2.0,  # Slightly reduced
            num_beams=4,  # Reduced for testing
            early_stopping=True
        )
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        # Post-processing to remove any trailing hyphens or repeated phrases
        summary = re.sub(r'(\s*[-–—]\s*)+$', '', summary)  # Remove trailing hyphens
        summary = re.sub(r'(\b\w+\b)( \1\b)+', r'\1', summary)  # Remove immediate repeated words

        return summary

    def fine_tune(self, dataset, num_train_epochs=3, batch_size=8):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model.train().to(device)
        data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
        optimizer = torch.optim.Adam(self.model.parameters(), lr=1e-5)  # Adjusted learning rate

        for epoch in range(num_train_epochs):
            total_loss = 0
            for input_ids, labels in data_loader:
                input_ids = input_ids.to(device)
                labels = labels.to(device)

                outputs = self.model(input_ids=input_ids, labels=labels)
                loss = outputs.loss

                loss.backward()
                optimizer.step()
                optimizer.zero_grad()
                total_loss += loss.item()
                if loss.item() < 0.05:  # Early stopping based on low loss to avoid overfitting
                    break

            if total_loss / len(data_loader) < 0.05:
                print(f"Early stopping at epoch {epoch+1}")
                break

        return total_loss / len(data_loader)  # Optionally return average loss for external use
