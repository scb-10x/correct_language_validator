# Overview

| Developed by | SCB10x |
| --- | --- |
| Date of development | Feb 15, 2024 |
| Validator type | Quality |
| Blog | - |
| License | Apache 2 |
| Input/Output | Output |

# Description

Validates that an LLM-generated text is in the expected language. If the text
is not in the expected language, the validator will attempt to translate it
to the expected language.

Uses the `fast-langdetect` library to detect the language of the input text,
and the `iso-language-codes` library to get the language names from the ISO codes.

Meta AI's `facebook/nllb-200-distilled-600M` translation model (available on Huggingface)
is used to translate the text from the detected language to the expected language.

## Intended use

- Primary intended uses: This validator is useful when you’re using multiple languages in an LLM application.
- Out-of-scope use cases: N/A

## Resources required

- Dependencies:
    - fast_langdetect
    - iso_language_codes
    - transformers HuggingFace library
    - facebook/nllb-200-distilled-600M translation model
- Foundation model access keys: HuggingFace

# **Example Usage Guide**

### Installation

```bash
$ guardrails hub install hub://guardrails/correct_language

```

### Initialization

```python
from guardrails.hub import CorrectLanguage

# Create validator
language_validator = CorrectLanguage(expected_language_iso="en", threshold=0.75)

# Create Guard with Validator
guard = Guard.from_string(
    validators=[language_validator, ...],
    num_reasks=2,
)

```

### Invocation

```python
guard.parse("Translated_text")

guard("Translate this to english: Danke")
```

## API Ref

N/A

## Expected deployment metrics

|  | CPU | GPU |
| --- | --- | --- |
| Latency |  | - |
| Memory |  | - |
| Cost |  | - |
| Expected quality |  | - |

## Resources required

- Dependencies:
    - fast_langdetect
    - iso_language_codes
    - transformers HuggingFace library
    - facebook/nllb-200-distilled-600M translation model
- Foundation model access keys: Huggingface auth
- Compute: Yes

## Validator Performance

### Evaluation Dataset

N/A

### Model Performance Measures

| Accuracy | - |
| --- | --- |
| F1 Score | - |

### Decision thresholds

0.7
