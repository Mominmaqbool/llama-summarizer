from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch  # Add this import

# Load the BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_text(text):
    # Tokenize input text
    inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)

    # Generate summary
    with torch.no_grad():
        # You can choose one of these two lines
        output_ids = model.generate(inputs, max_new_tokens=50)

    summary = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return summary

if __name__ == "__main__":
    long_text = input("Enter the text to summarize: ")
    print("Original Text:", long_text)
    summary = summarize_text(long_text)
    print("Summary:", summary)
