# To check path of stored/ cached transformer models downloaded
# from transformers import file_utils
# print(file_utils.default_cache_path)

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import requests
import random

pos_model = "vblagoje/bert-english-uncased-finetuned-pos"
pos_tokenizer = AutoTokenizer.from_pretrained(pos_model)
pos_model = AutoModelForTokenClassification.from_pretrained(pos_model)
pos_pipeline = pipeline("ner", model=pos_model, tokenizer=pos_tokenizer)

pos_special_tags =  ["NOUN", "VERB", "ADJ"]
pos_sort_order = {pos: i for i, pos in enumerate(pos_special_tags)}

def pos_sort(rec):
  entity = rec['entity']
  if (entity in pos_sort_order):
    return pos_sort_order[entity]
  return len(pos_special_tags)

def score_sort(rec):
  return rec['score']

def only_valid_pos(rec):
  return rec['word'].isalpha()


def extract_fine_pos(prompt):
  extracted_pos = pos_pipeline(prompt)
  sorted_extracted_pos = sorted(extracted_pos, key=score_sort, reverse=True)
  sorted_extracted_pos.sort(key=pos_sort)
  sorted_extracted_pos = list(filter(only_valid_pos, sorted_extracted_pos))
  return sorted_extracted_pos

