# 🧠 English to Hindi Machine Translation

This project demonstrates a **simple Machine Translation system** using a pre-trained transformer model from **Hugging Face**.  
It translates English sentences into Hindi using the **MarianMT** model architecture.

---

## 🚀 Features

- Translates English text to Hindi
- Uses a pre-trained **Helsinki-NLP/opus-mt-en-hi** model
- Implemented in just a few lines of Python
- Runs locally or in Google Colab / Jupyter Notebook

---

## 🛠️ Requirements

Install the necessary libraries before running the script:

```bash
pip install transformers torch sentencepiece
```

---

## 💻 Usage

Run the script in your terminal or Jupyter Notebook:

```bash
python translate.py
```

or paste this in a Jupyter cell:

```python
from transformers import MarianMTModel, MarianTokenizer

model_name = 'Helsinki-NLP/opus-mt-en-hi'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

text = input("Enter an english sentence: ")
inputs = tokenizer(text, return_tensors="pt", padding=True)
translated = model.generate(**inputs)
translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)

print("English:", text)
print("Hindi:", translated_text[0])
```

---

## 🧩 Example Output

**Input:**

```
Education is the most powerful weapon to change the world.
```

**Output:**

```
Education is the most powerful weapon to change the world.
शिक्षा दुनिया को बदलने का सबसे शक्तिशाली हथियार है।
```

---

## 📚 Model Reference

Model used: [Helsinki-NLP/opus-mt-en-hi](https://huggingface.co/Helsinki-NLP/opus-mt-en-hi)

---

## 👨‍💻 Author

**Karan Singh V**
