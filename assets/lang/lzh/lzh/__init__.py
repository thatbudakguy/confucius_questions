from importlib.resources import read_text

import spacy
from spacy.lang.zh import ChineseTokenizer, Segmenter
from spacy.language import Language
from spacy.util import load_config_from_str, registry


class ClassicalChineseDefaults(Language.Defaults):
    config = load_config_from_str(read_text(__name__, "config.cfg"))
    writing_system = {"direction": "ltr", "has_case": False, "has_letters": False}


@registry.tokenizers("spacy.lzh.ClassicalChineseTokenizer")
def create_classical_chinese_tokenizer():
    def classical_chinese_tokenizer_factory(nlp: Language):
        return ChineseTokenizer(nlp.vocab, segmenter=Segmenter.char)

    return classical_chinese_tokenizer_factory


@spacy.registry.languages("lzh")
class ClassicalChinese(Language):
    lang = "lzh"
    Defaults = ClassicalChineseDefaults


__all__ = ["ClassicalChinese"]
