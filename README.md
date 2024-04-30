# Acronym Translation System

We present a system for providing verified translations of acronyms in scientific and technical papers. To do so, a short form (SF)--long form (LF) pair goes through the following steps:

- Input a list of terms from the user
For each term:
- Generate a SF from the LF using a fine-tuned version of SciBERT
- Verify that the term is used by domain experts in at least two published works
- Return a list of verified LF-SF pairs (in the form "cardiopulmonary resuscitation (CPR)") to the user or indicate that the terms were unable to be verified

Incorrect translations are fatal errors in translation. Translating the French "rétinopathie diabétique" as "diabetic retinopathy (RD)" instead of "diabetic retinopathy (DR)" is akin to writing "AUS" instead of "USA" and saying that the acronym was "close enough". This system offers a method for improving translation systems by focusing on their correctness rather than only on the fluency of generated text.
