from ibm_watsonx_orchestrate.agent_builder.tools import *
import translators as ts  # https://github.com/UlionTse/translators?tab=readme-ov-file#supported-languages


@tool
def translate(text: str, target_language_code: str) -> str:
    """
    Translates the given text into the specified target language using Google Translate.
    If user specifies a language and not a code, use its two-letter ISO 639-1 code.

    :param text: Text to be translated.
    :param target_language_code: Target two-letter language code, e.g., 'en' for English. of ISO 639 Standard.

    :returns: Translated text in the specified target language.
    """
    return ts.translate_text(
        text, translator="google", to_language=target_language_code
    )
