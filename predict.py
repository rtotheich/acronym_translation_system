import sys
import numpy as np
from transformers import TFAutoModelForMaskedLM
from transformers import AutoTokenizer
import tensorflow as tf

# Insert path to the model
model_path = ''
model = TFAutoModelForMaskedLM.from_pretrained(model_path)

tokenizer = AutoTokenizer.from_pretrained(model_path)

model.summary()

def predict(lf):
    inputs = tokenizer(lf, return_tensors="np")
    token_logits = model(**inputs).logits
    
    mask_token_index = np.argwhere(inputs["input_ids"] == tokenizer.mask_token_id)[0, 1]
    mask_token_logits = token_logits[0, mask_token_index, :]

    top_token_index_1 = np.argsort(-mask_token_logits)[0]
    second_token_index_1 = np.argsort(-mask_token_logits)[1]
    second_token_1 = tokenizer.decode(second_token_index_1)
    if second_token_1.startswith('##'):
        second_token_1 = second_token_1[2:]
    
    lf = lf.replace(tokenizer.mask_token, tokenizer.decode(top_token_index_1).upper())
    predict_1 = lf
    
    lf = lf.replace(")", " " + tokenizer.mask_token + ")")
    inputs = tokenizer(lf, return_tensors="np")
    token_logits = model(**inputs).logits
    mask_token_index2 = mask_token_index + 1
    mask_token_logits2 = token_logits[0, mask_token_index2, :]
    top_token_index_2 = np.argsort(-mask_token_logits2)[0]
    second_token_index_2 = np.argsort(-mask_token_logits2)[1]
    second_token_2 = tokenizer.decode(second_token_index_2)
    if second_token_2.startswith('##'):
        second_token_2 = second_token_2[2:]
    lf = lf.replace(" " + tokenizer.mask_token, tokenizer.decode(top_token_index_2)[2:].upper())
    predict_2 = lf

    lf = lf.replace(")", " " + tokenizer.mask_token + ")")
    inputs = tokenizer(lf, return_tensors="np")
    token_logits = model(**inputs).logits
    mask_token_index3 = mask_token_index2 + 1
    mask_token_logits3 = token_logits[0, mask_token_index3, :]
    top_token_index_3 = np.argsort(-mask_token_logits3)[0]
    lf = lf.replace(" " + tokenizer.mask_token, tokenizer.decode(top_token_index_3)[2:].upper())
    predict_3 = lf

    predict_4 = f"{lf.split('(')[0]} ({second_token_1.upper()})"
    predict_5 = f"{lf.split('(')[0]} ({second_token_1.upper()}{second_token_2.upper()})"

    print([predict_1, predict_2, predict_3, predict_4, predict_5])
    return [predict_1, predict_2, predict_3, predict_4, predict_5]

if __name__ == "__main__":
    predict(sys.argv[1])
