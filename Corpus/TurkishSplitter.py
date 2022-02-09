from Corpus.SentenceSplitter import SentenceSplitter
from Language.TurkishLanguage import TurkishLanguage


class TurkishSplitter(SentenceSplitter):

    def upperCaseLetters(self) -> str:
        return TurkishLanguage.UPPERCASE_LETTERS

    def lowerCaseLetters(self) -> str:
        return TurkishLanguage.LOWERCASE_LETTERS

    def shortCuts(self) -> list:
        return ["alb", "bnb", "bkz", "bşk", "co", "dr", "dç", "der", "em", "gn",
                "hz", "kd", "kur", "kuv", "ltd", "md", "mr", "mö", "muh", "müh",
                "no", "öğr", "op", "opr", "org", "sf", "tuğ", "uzm", "vb", "vd",
                "yön", "yrb", "yrd", "üniv", "fak", "prof", "dz", "yd", "krm", "gen",
                "pte", "p", "av", "II", "III", "IV", "VI", "VII", "VIII", "IX",
                "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX",
                "XX", "tuğa", "plt", "tğm", "tic", "srv", "bl", "dipl", "not", "min",
                "cul", "san", "rzv", "or", "kor", "tüm", "st", "sn", "fr", "pl",
                "ka", "tk", "ko", "vs", "yard", "bknz", "doç", "gör", "müz", "oyn",
                "m", "s", "kr", "ms", "hv", "uz", "re", "ph", "mc", "ed",
                "km", "yb", "bk", "jr", "bn", "os", "mrs", "bld", "sen", "alm",
                "sir", "ord", "dir", "yay", "man", "brm", "edt", "dec", "mah", "cad",
                "vol", "kom", "sok", "apt", "elk", "mad", "ort", "cap", "ste", "exc",
                "ef"]
