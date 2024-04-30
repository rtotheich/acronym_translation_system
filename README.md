# Acronym Translation System

We present a system for providing verified translations of acronyms in scientific and technical papers. To do so, a short form (SF)-long form (LF) pair goes through the following steps:

- Input a list of terms from the user

For each term:

- <a href="https://github.com/rtotheich/acronym_translation_system/blob/main/translate.py">Translate</a> a LF-SF pair using the Google Translate API
- Verify that the term is used by domain experts in at least two published works via <a href="https://github.com/rtotheich/acronym_translation_system/blob/main/arXiv_check.py">arxiv_check.py</a> and <a href="https://github.com/rtotheich/acronym_translation_system/blob/main/pubmed_check.py">pubmed_check.py</a>
- If it is not, <a href="https://github.com/rtotheich/acronym_translation_system/blob/main/predict.py">generate</a> a list of five candidate SFs from the LF using a fine-tuned version of SciBERT (see <a href="https://github.com/rtotheich/acronym_translation_system/blob/main/acronym_scibert_fine_tuning.ipynb">acronym_scibert_fine_tuning.ipynb</a>)
- <a href="https://github.com/rtotheich/acronym_translation_system/blob/main/rerank.py">Rerank</a> and select the most likely candidate
- Return a list of verified LF-SF pairs (in the form “cardiopulmonary resuscitation (CPR)") to the user or indicate that the terms were unable to be verified

Incorrect term translations (including SFs) are fatal errors in translation. Translating the French “rétinopathie diabétique” as “diabetic retinopathy (RD)” instead of “diabetic retinopathy (DR)” is akin to writing “AUS” instead of “USA” and saying that the acronym was “close enough”. This system offers a method for reducing the bias of translation systems by focusing on their correctness rather than only on the fluency of generated text.
