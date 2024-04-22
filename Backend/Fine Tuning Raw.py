from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset

# Assuming torch and transformers have already been installed as per Step 3

# Load the T5 model and tokenizer
model_name = "t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)


# Define a custom dataset
class SummarizationDataset(Dataset):
    def __init__(self, texts, summaries):
        self.texts = texts
        self.summaries = summaries

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        input_text = self.texts[idx]
        target_text = self.summaries[idx]
        source = tokenizer(input_text, padding='max_length', truncation=True, max_length=512, return_tensors="pt")
        target = tokenizer(target_text, padding='max_length', truncation=True, max_length=128, return_tensors="pt")

        return {
            "input_ids": source.input_ids.squeeze(),  # squeeze to remove the batch dimension
            "attention_mask": source.attention_mask.squeeze(),
            "labels": target.input_ids.squeeze()
        }


# Example data
texts = ["The T5 model is an effective tool for NLP tasks."]
summaries = ["T5 is effective for NLP."]

# Create dataset
train_dataset = SummarizationDataset(texts, summaries)

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',  # output directory
    num_train_epochs=3,  # number of training epochs
    per_device_train_batch_size=8,  # batch size for training
    warmup_steps=500,  # number of warmup steps for learning rate scheduler
    weight_decay=0.01,  # strength of weight decay
    logging_dir='./logs',  # directory for storing logs
    logging_steps=10,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
)

# Start training
trainer.train()

# Save the model
model.save_pretrained("./fine_tuned_t5")

print("Model fine-tuning complete.")

"""
Key Components:
Custom Dataset Class: This class handles the input and label tokenization for summarization tasks. It is crucial for fine-tuning, as it ensures the model learns from a dataset that mirrors the final task.
Training Setup: Uses Hugging Face's Trainer API, which simplifies the process of setting up training routines, including handling the training loop, optimization, and saving checkpoints.
Training Arguments: Configured for the training, including setting directories, batch sizes, and epochs. Adjust these based on your computational resources and dataset size.
Training the Model:
To execute this training script, ensure you have a substantial and relevant dataset for fine-tuning. The example uses dummy data, which is only illustrative. In a real-world scenario, you'd replace texts and summaries with your dataset, potentially split into training and validation sets.
"""
