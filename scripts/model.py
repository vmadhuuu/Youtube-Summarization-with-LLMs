from transformers import BartForConditionalGeneration, BartTokenizer

class SummarizationModel:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.tokenizer = BartTokenizer.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name)

    def generate_summary(self, text_input):
        inputs = self.tokenizer([text_input], max_length=1024, return_tensors="pt", truncation=True)
        summary_ids = self.model.generate(inputs["input_ids"], max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
