# llama-summarizer
Python script for text summarization using Hugging Face BART model.
# LLaMA Summarizer

This repository contains a Python script for text summarization using the BART model (`facebook/bart-large-cnn`) from Hugging Face.

## Overview

The script utilizes the BART (Bidirectional and Auto-Regressive Transformers) model, specifically the `facebook/bart-large-cnn` variant, for summarizing large texts. BART is a state-of-the-art transformer model designed for text generation tasks such as summarization, translation, and more.

## Features

- **Text Summarization**: The script takes an input text and generates a concise summary using the BART model.
- **Easy to Use**: Simply run the script, input the text to be summarized, and receive the output.
- **Customizable**: Modify parameters like `max_new_tokens` to control the length of the generated summary.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- `pip` package manager

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Mominmaqbool/llama-summarizer.git
    cd llama-summarizer
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv llama_env
    llama_env\Scripts\activate  # For Windows
    source llama_env/bin/activate  # For macOS/Linux
    ```

3. Install the required packages:

    ```bash
    pip install transformers torch
    ```

### Usage

1. Run the Python script:

    ```bash
    python llama_summarizer.py
    ```

2. Enter the text you want to summarize when prompted.



