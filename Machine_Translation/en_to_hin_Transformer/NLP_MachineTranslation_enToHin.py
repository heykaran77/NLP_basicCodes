from transformers import MarianMTModel, MarianTokenizer

model_name = 'Helsinki-NLP/opus-mt-en-hi'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

text = input("Enter an english sentence: ")
inputs = tokenizer(text, return_tensors = "pt", padding=True)
translated = model.generate(**inputs)
translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)

print("English: ", text)
print("Hindi: ", translated_text[0])
