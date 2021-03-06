# -*- coding: utf-8 -*-

class Color:
    BLACK     = '\033[30m'
    RED       = '\033[31m'
    GREEN     = '\033[32m'
    YELLOW    = '\033[33m'
    BLUE      = '\033[34m'
    PURPLE    = '\033[35m'
    CYAN      = '\033[36m'
    WHITE     = '\033[37m'
    BG_BLACK  = '\033[40m'
    BG_RED    = '\033[41m'
    BG_GREEN  = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE   = '\033[44m'
    BG_PURPLE = '\033[45m'
    BG_CYAN   = '\033[46m'
    BG_WHITE  = '\033[47m'
    END       = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE   = '\033[07m'

Data = {
    "Singers": [
        {
            "Name": "LEON",
            "Code": "leon",
            "Gender": 1,
            "Products": [
                {
                    "Name": "LEON",
                    "Engine": "vocaloid_1",
                    "Vendors": ["zero_g"],
                    "Languages": ["EN"],
                    "Voice": None,
                    "Date": "2004-01-15"
                }
            ],
            "Pair": None
        },
        {
            "Name": "LOLA",
            "Code": "lola",
            "Gender": 2,
            "Products": [
                {
                    "Name": "LEON",
                    "Engine": "vocaloid_1",
                    "Vendors": ["zero_g"],
                    "Languages": ["EN"],
                    "Voice": None,
                    "Date": "2004-01-15"
                }
            ],
            "Pair": None
        },
        {
            "Name": "MIRIAM",
            "Code": "miriam",
            "Gender": 2,
            "Products": [
                {
                    "Name": "MIRIAM",
                    "Engine": "vocaloid_1",
                    "Vendors": ["zero_g"],
                    "Languages": ["EN"],
                    "Voice": "Miriam Stockley",
                    "Date": "2004-07-01"
                }
            ],
            "Pair": None
        },
        {
            "Name": "PRIMA",
            "Code": "prima",
            "Gender": 2,
            "Products": [
                {
                    "Name": "PRIMA",
                    "Engine": "vocaloid_2",
                    "Vendors": ["zero_g"],
                    "Languages": ["EN"],
                    "Voice": None,
                    "Date": "2008-01-14"
                }
            ],
            "Pair": None
        },
        {
            "Name": "SONIKA",
            "Code": "sonika",
            "Gender": 2,
            "Products": [
                {
                    "Name": "SONIKA",
                    "Engine": "vocaloid_2",
                    "Vendors": ["zero_g"],
                    "Languages": ["EN"],
                    "Voice": None,
                    "Date": "2009-07-15"
                }
            ],
            "Pair": None
        },
        {
            "Name": "TONIO",
            "Code": "tonio",
            "Gender": 1,
            "Products": [
                {
                    "Name": "TONIO",
                    "Engine": "vocaloid_2",
                    "Vendors": ["zero_g"],
                    "Languages": ["EN"],
                    "Voice": None,
                    "Date": "2010-07-13"
                }
            ],
            "Pair": None
        },
        {
            "Name": "AVANNA",
            "Code": "avanna",
            "Gender": 2,
            "Products": [
                {
                    "Name": "AVANNA",
                    "Engine": "vocaloid_3",
                    "Vendors": ["zero_g"],
                    "Languages": ["EN"],
                    "Voice": "Rachel Daigh",
                    "Date": "2012-12-22"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Dex",
            "Code": "dex",
            "Gender": 1,
            "Products": [
                {
                    "Name": "Dex",
                    "Engine": "vocaloid_4",
                    "Vendors": ["zero_g"],
                    "Languages": ["EN"],
                    "Voice": "Sam Blakeslee",
                    "Date": "2015-11-20"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Daina",
            "Code": "daina",
            "Gender": 2,
            "Products": [
                {
                    "Name": "Daina",
                    "Engine": "vocaloid_4",
                    "Vendors": ["zero_g"],
                    "Languages": ["EN"],
                    "Voice": "AkiGlancy",
                    "Date": "2015-11-20"
                }
            ],
            "Pair": None
        },
        {
            "Name": "MEIKO",
            "Code": "meiko",
            "Gender": 2,
            "Products": [
                {
                    "Name": "MEIKO",
                    "Engine": "vocaloid_1",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "???????????????",
                    "Date": "2004-11-05"
                },
                {
                    "Name": "MEIKO V3",
                    "Engine": "vocaloid_3",
                    "Vendors": ["crypton"],
                    "Languages": ["JA", "EN"],
                    "Voice": "???????????????",
                    "Date": "2014-02-04"
                }
            ],
            "Pair": None
        },
        {
            "Name": "KAITO",
            "Code": "kaito",
            "Gender": 1,
            "Products": [
                {
                    "Name": "KAITO",
                    "Engine": "vocaloid_1",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "???????????????",
                    "Date": "2006-02-17"
                },
                {
                    "Name": "KAITO V3",
                    "Engine": "vocaloid_3",
                    "Vendors": ["crypton"],
                    "Languages": ["JA", "EN"],
                    "Voice": "???????????????",
                    "Date": "2013-02-15"
                }
            ],
            "Pair": None
        },
        {
            "Name": "????????????",
            "Code": "hatsune_miku",
            "Gender": 2,
            "Products": [
                {
                    "Name": "????????????",
                    "Engine": "vocaloid_2",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "?????????",
                    "Date": "2007-08-31"
                },
                {
                    "Name": "???????????? Append",
                    "Engine": "vocaloid_2",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "?????????",
                    "Date": "2010-04-30"
                },
                {
                    "Name": "???????????? V3",
                    "Engine": "vocaloid_3",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "?????????",
                    "Date": "2013-09-26"
                },
                {
                    "Name": "???????????? V3 ENGLISH",
                    "Engine": "vocaloid_3",
                    "Vendors": ["crypton"],
                    "Languages": ["EN"],
                    "Voice": "?????????",
                    "Date": "2013-08-31"
                },
                {
                    "Name": "???????????? V4X",
                    "Engine": "vocaloid_4",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "?????????",
                    "Date": "2016-08-31"
                },
                {
                    "Name": "???????????? V4 ENGLISH",
                    "Engine": "vocaloid_4",
                    "Vendors": ["crypton"],
                    "Languages": ["EN"],
                    "Voice": "?????????",
                    "Date": "2016-08-31"
                },
                {
                    "Name": "???????????? V4 CHINESE",
                    "Engine": "vocaloid_4",
                    "Vendors": ["crypton"],
                    "Languages": ["ZH-CN"],
                    "Voice": "?????????",
                    "Date": "2017-08-31"
                }
            ],
            "Pair": None
        },
        {
            "Name": "????????????",
            "Code": "kagamine_rin",
            "Gender": 2,
            "Pair": "kagamine"
        },
        {
            "Name": "????????????",
            "Code": "kagamine_len",
            "Gender": 1,
            "Pair": "kagamine"
        },
        {
            "Name": "????????????",
            "Code": "megurine_ruka",
            "Gender": 2,
            "Products": [
                {
                    "Name": "????????????",
                    "Engine": "vocaloid_2",
                    "Vendors": ["crypton"],
                    "Languages": ["JA", "EN"],
					"Voice": "?????????",
                    "Date": "2009-01-30"
                },
                {
                    "Name": "???????????? V4X",
                    "Engine": "vocaloid_4",
                    "Vendors": ["crypton"],
                    "Languages": ["JA", "EN"],
                    "Voice": "?????????",
                    "Date": "2015-03-19"
                }
            ],
            "Pair": None
        },
        {
            "Name": "SWEET ANN",
            "Code": "sweet_ann",
            "Gender": 2,
            "Products": [
                {
                    "Name": "SWEET ANN",
                    "Engine": "vocaloid_2",
                    "Vendors": ["powerfx"],
                    "Languages": ["EN"],
					"Voice": "Jody",
                    "Date": "2007-06-29"
                }
            ],
            "Pair": None
        },
        {
            "Name": "BIG-AL",
            "Code": "big_al",
            "Gender": 1,
            "Products": [
                {
                    "Name": "BIG-AL",
                    "Engine": "vocaloid_2",
                    "Vendors": ["powerfx"],
                    "Languages": ["EN"],
					"Voice": "Frank Sanderson",
                    "Date": "2009-12-22"
                }
            ],
            "Pair": None
        },
        {
            "Name": "OLIVER",
            "Code": "oliver",
            "Gender": 1,
            "Products": [
                {
                    "Name": "OLIVER",
                    "Engine": "vocaloid_3",
                    "Vendors": ["powerfx"],
                    "Languages": ["EN"],
					"Voice": None,
                    "Date": "2011-12-21"
                }
            ],
            "Pair": None
        },
        {
            "Name": "YOHIOloid",
            "Code": "yohioloid",
            "Gender": 1,
            "Products": [
                {
                    "Name": "YOHIOloid",
                    "Engine": "vocaloid_3",
                    "Vendors": ["powerfx"],
                    "Languages": ["JA", "EN"],
					"Voice": "YOHIO",
                    "Date": "2013-09-10"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Ruby",
            "Code": "ruby",
            "Gender": 2,
            "Products": [
                {
                    "Name": "Ruby",
                    "Engine": "vocaloid_4",
                    "Vendors": ["powerfx"],
                    "Languages": ["EN"],
					"Voice": "Misha",
                    "Date": "2015-10-07"
                }
            ],
            "Pair": None
        },
        {
            "Name": "??????????????????",
            "Code": "gackpoid",
            "Gender": 1,
            "Products": [
                {
                    "Name": "??????????????????",
                    "Engine": "vocaloid_2",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "GACKT",
                    "Date": "2008-07-31"
                },
                {
                    "Name": "?????????????????? NATIVE",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "GACKT",
                    "Date": "2012-07-13"
                },
                {
                    "Name": "?????????????????? NATIVE",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "GACKT",
                    "Date": "2015-04-30"
                },
                {
                    "Name": "?????????????????? POWER",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "GACKT",
                    "Date": "2012-07-13"
                },
                {
                    "Name": "?????????????????? POWER",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "GACKT",
                    "Date": "2015-04-30"
                },
                {
                    "Name": "?????????????????? WHISPER",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "GACKT",
                    "Date": "2012-07-13"
                },
                {
                    "Name": "?????????????????? WHISPER",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "GACKT",
                    "Date": "2015-04-30"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Megpoid",
            "Code": "megpoid",
            "Gender": 2,
            "Products": [
                {
                    "Name": "Megpoid",
                    "Engine": "vocaloid_2",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "?????????",
                    "Date": "2009-06-26"
                },
                {
                    "Name": "Megpoid Power",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "?????????",
                    "Date": "2011-10-21"
                },
                {
                    "Name": "Megpoid Power",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "?????????",
                    "Date": "2015-11-05"
                },
                {
                    "Name": "Megpoid Whisper",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "?????????",
                    "Date": "2011-10-21"
                },
                {
                    "Name": "Megpoid Whisper",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "?????????",
                    "Date": "2015-11-05"
                },
                {
                    "Name": "Megpoid Adult",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "?????????",
                    "Date": "2011-10-21"
                },
                {
                    "Name": "Megpoid Adult",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "?????????",
                    "Date": "2015-11-05"
                },
                {
                    "Name": "Megpoid Sweet",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "?????????",
                    "Date": "2011-10-21"
                },
                {
                    "Name": "Megpoid Sweet",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "?????????",
                    "Date": "2015-11-05"
                },
                {
                    "Name": "Megpoid Native",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "?????????",
                    "Date": "2012-03-16"
                },
                {
                    "Name": "Megpoid Native",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "?????????",
                    "Date": "2015-11-05"
                },
                {
                    "Name": "Megpoid English",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["EN"],
					"Voice": "?????????",
                    "Date": "2013-02-28"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Lily",
            "Code": "lily",
            "Gender": 2,
            "Products": [
                {
                    "Name": "Lily",
                    "Engine": "vocaloid_2",
                    "Vendors": ["avex", "yamaha", "internet"],
                    "Languages": ["JA"],
					"Voice": "yuri",
                    "Date": "2010-08-25"
                },
                {
                    "Name": "Lily",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "yuri",
                    "Date": "2012-04-19"
                }
            ],
            "Pair": None
        },
        {
            "Name": "?????????????????????",
            "Code": "gachapoid",
            "Gender": 1,
            "Products": [
                {
                    "Name": "?????????????????????",
                    "Engine": "vocaloid_2",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2010-10-08"
                },
                {
                    "Name": "????????????????????? V3",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2014-09-17"
                }
            ],
            "Pair": None
        },
        {
            "Name": "CUL",
            "Code": "cul",
            "Gender": 2,
            "Products": [
                {
                    "Name": "CUL",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2011-12-22"
                }
            ],
            "Pair": None
        },
        {
            "Name": "kokone",
            "Code": "kokone",
            "Gender": 2,
            "Products": [
                {
                    "Name": "kokone",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2014-02-14"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Chika",
            "Code": "chika",
            "Gender": 2,
            "Products": [
                {
                    "Name": "Chika",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2014-10-16"
                }
            ],
            "Pair": None
        },
        {
            "Name": "????????????",
            "Code": "otomachi_una",
            "Gender": 2,
            "Products": [
                {
                    "Name": "????????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2016-07-30"
                },
                {
                    "Name": "????????????Talk Ex",
                    "Engine": "voiceroid_2",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2017-04-20"
                }
            ],
            "Pair": None
        },
        {
            "Name": "??????????????????",
            "Code": "hiyama_kiyoteru",
            "Gender": 1,
            "Products": [
                {
                    "Name": "??????????????????",
                    "Engine": "vocaloid_2",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2009-12-04"
                },
                {
                    "Name": "?????????????????? ???????????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2015-10-29"
                },
                {
                    "Name": "?????????????????? ?????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2015-10-29"
                }
            ],
            "Pair": None
        },
        {
            "Name": "????????????",
            "Code": "kaai_yuki",
            "Gender": 2,
            "Products": [
                {
                    "Name": "????????????",
                    "Engine": "vocaloid_2",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2009-12-04"
                },
                {
                    "Name": "???????????? ???????????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2015-10-29"
                }
            ],
            "Pair": None
        },
        {
            "Name": "SF-A2 ??????????????? miki",
            "Code": "miki",
            "Gender": 2,
            "Products": [
                {
                    "Name": "SF-A2 ??????????????? miki",
                    "Engine": "vocaloid_2",
                    "Vendors": ["yamaha", "ahs"],
                    "Languages": ["JA"],
					"Voice": "??????????????????",
                    "Date": "2009-12-04"
                },
                {
                    "Name": "miki ???????????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "??????????????????",
                    "Date": "2015-06-18"
                }
            ],
            "Pair": None
        },
        {
            "Name": "???????????????",
            "Code": "nekomura_iroha",
            "Gender": 2,
            "Products": [
                {
                    "Name": "???????????????",
                    "Engine": "vocaloid_2",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2010-10-22"
                },
                {
                    "Name": "??????????????? ???????????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2015-06-18"
                },
                {
                    "Name": "??????????????? ?????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2015-06-18"
                }
            ],
            "Pair": None
        },
        {
            "Name": "???????????????",
            "Code": "yuduki_yukari",
            "Gender": 2,
            "Products": [
                {
                    "Name": "???????????????",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2011-12-22"
                },
                {
                    "Name": "??????????????? ???",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2015-03-18"
                },
                {
                    "Name": "??????????????? ???",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2015-03-18"
                },
                {
                    "Name": "??????????????? ???",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2015-03-18"
                },
                {
                    "Name": "VOICEROID+ ???????????????",
                    "Engine": "voiceroid_plus",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2011-12-22"
                },
                {
                    "Name": "VOICEROID+ EX ???????????????",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2014-10-30"
                },
                {
                    "Name": "VOICEROID2 ???????????????",
                    "Engine": "voiceroid_2",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2017-06-09"
                }
            ],
            "Pair": None
        },
        {
            "Name": "???????????????",
            "Code": "touhoku_zunko",
            "Gender": 2,
            "Products": [
                {
                    "Name": "???????????????",
                    "Engine": "vocaloid_3",
                    "Vendors": ["sss", "ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2014-06-05"
                },
                {
                    "Name": "??????????????? ???????????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["sss", "ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2016-10-27"
                },
                {
                    "Name": "VOICEROID+ ???????????????",
                    "Engine": "voiceroid_plus",
                    "Vendors": ["sss", "ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2012-09-28"
                },
                {
                    "Name": "VOICEROID+ EX ???????????????",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["sss", "ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2014-10-30"
                }
            ],
            "Pair": None
        },
        {
            "Name": "???????????????",
            "Code": "kizuna_akari",
            "Gender": 2,
            "Products": [
                {
                    "Name": "???????????????",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "?????????",
                    "Date": "2018-04-26"
                },
                {
                    "Name": "VOICEROID2 ???????????????",
                    "Engine": "voiceroid_2",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "?????????",
                    "Date": "2017-12-22"
                }
            ],
            "Pair": None
        },
        {
            "Name": "????????????",
            "Code": "haruno_sora",
            "Gender": 2,
            "Products": [
                {
                    "Name": "???????????? ???????????????",
                    "Engine": "vocaloid_5",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2018-07-26"
                },
                {
                    "Name": "???????????? ?????????",
                    "Engine": "vocaloid_5",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2018-07-26"
                },
                {
                    "Name": "VOICEROID2 ????????????",
                    "Engine": "voiceroid_2",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2018-07-26"
                }
            ],
            "Pair": None
        },
        {
            "Name": "VY1",
            "Code": "vy1",
            "Gender": 2,
            "Products": [
                {
                    "Name": "VY1",
                    "Engine": "vocaloid_2",
                    "Vendors": ["bplats", "yamaha"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2010-09-11"
                },
                {
                    "Name": "VY1V3",
                    "Engine": "vocaloid_3",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2011-10-21"
                },
                {
                    "Name": "VY1V4",
                    "Engine": "vocaloid_4",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2014-12-17"
                },
                {
                    "Name": "VY1",
                    "Engine": "vocaloid_5",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2018-07-12"
                }
            ],
            "Pair": None
        },
        {
            "Name": "VY2",
            "Code": "vy2",
            "Gender": 1,
            "Products": [
                {
                    "Name": "VY2",
                    "Engine": "vocaloid_2",
                    "Vendors": ["bplats", "yamaha"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2011-04-25"
                },
                {
                    "Name": "VY2V3",
                    "Engine": "vocaloid_3",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2012-10-19"
                },
                {
                    "Name": "VY2",
                    "Engine": "vocaloid_5",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2018-07-12"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Mew",
            "Code": "mew",
            "Gender": 2,
            "Products": [
                {
                    "Name": "Mew",
                    "Engine": "vocaloid_3",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2011-10-21"
                }
            ],
            "Pair": None
        },
        {
            "Name": "???????????????",
            "Code": "tone_rion",
            "Gender": 2,
            "Products": [
                {
                    "Name": "???????????????",
                    "Engine": "vocaloid_3",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2011-12-16"
                },
                {
                    "Name": "???????????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2017-02-16"
                }
            ],
            "Pair": None
        },
        {
            "Name": "???????????????",
            "Code": "aoki_lapis",
            "Gender": 2,
            "Products": [
                {
                    "Name": "???????????????",
                    "Engine": "vocaloid_3",
                    "Vendors": ["i_style", "yamaha"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2012-04-06"
                }
            ],
            "Pair": None
        },
        {
            "Name": "YUU",
            "Code": "yuu",
            "Gender": 1,
            "Pair": "zola_project"
        },
        {
            "Name": "KYO",
            "Code": "kyo",
            "Gender": 1,
            "Pair": "zola_project"
        },
        {
            "Name": "WIL",
            "Code": "wil",
            "Gender": 1,
            "Pair": "zola_project"
        },
        {
            "Name": "?????????",
            "Code": "merli",
            "Gender": 2,
            "Products": [
                {
                    "Name": "?????????",
                    "Engine": "vocaloid_3",
                    "Vendors": ["i_style", "yamaha"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2013-12-24"
                }
            ],
            "Pair": None
        },
        {
            "Name": "??????",
            "Code": "anon",
            "Gender": 2,
            "Pair": "anon_kanon"
        },
        {
            "Name": "??????",
            "Code": "kanon",
            "Gender": 2,
            "Pair": "anon_kanon"
        },
        {
            "Name": "???????????? NEO",
            "Code": "galaco_neo",
            "Gender": 2,
            "Products": [
                {
                    "Name": "???????????? NEO",
                    "Engine": "vocaloid_3",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2014-08-05"
                }
            ],
            "Pair": None
        },
        {
            "Name": "CYBER DIVA",
            "Code": "cyber_diva",
            "Gender": 2,
            "Products": [
                {
                    "Name": "CYBER DIVA",
                    "Engine": "vocaloid_4",
                    "Vendors": ["yamaha"],
                    "Languages": ["EN"],
					"Voice": "Jenny Shima",
                    "Date": "2015-02-05"
                },
                {
                    "Name": "CYBER DIVA II",
                    "Engine": "vocaloid_5",
                    "Vendors": ["yamaha"],
                    "Languages": ["EN"],
					"Voice": "Jenny Shima",
                    "Date": "2018-07-12"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Sachiko",
            "Code": "sachiko",
            "Gender": 2,
            "Products": [
                {
                    "Name": "Sachiko",
                    "Engine": "vocaloid_4",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2015-07-27"
                }
            ],
            "Pair": None
        },
        {
            "Name": "??????????????????",
            "Code": "arsloid",
            "Gender": 1,
            "Products": [
                {
                    "Name": "??????????????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2015-09-23"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Unity-chan!",
            "Code": "unity_chan",
            "Gender": 2,
            "Products": [
                {
                    "Name": "Unity-chan!",
                    "Engine": "vocaloid_4",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2016-01-14"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Fukase",
            "Code": "fukase",
            "Gender": 1,
            "Products": [
                {
                    "Name": "Fukase",
                    "Engine": "vocaloid_4",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA", "EN"],
					"Voice": "Fukase",
                    "Date": "2016-01-28"
                }
            ],
            "Pair": None
        },
        {
            "Name": "CYBER SONGMAN",
            "Code": "cyber_songman",
            "Gender": 1,
            "Products": [
                {
                    "Name": "CYBER SONGMAN",
                    "Engine": "vocaloid_4",
                    "Vendors": ["yamaha"],
                    "Languages": ["EN"],
					"Voice": None,
                    "Date": "2016-10-31"
                },
                {
                    "Name": "CYBER SONGMAN II",
                    "Engine": "vocaloid_5",
                    "Vendors": ["yamaha"],
                    "Languages": ["EN"],
					"Voice": None,
                    "Date": "2018-07-12"
                }
            ],
            "Pair": None
        },
        {
            "Name": "????????????",
            "Code": "yumemi_nemu",
            "Gender": 2,
            "Products": [
                {
                    "Name": "????????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["dearstage", "yamaha"],
                    "Languages": ["JA", "EN"],
					"Voice": "????????????",
                    "Date": "2017-02-16"
                }
            ],
            "Pair": None
        },
        {
            "Name": "AZUKI",
            "Code": "azuki",
            "Gender": 2,
            "Products": [
                {
                    "Name": "AZUKI",
                    "Engine": "vocaloid_4",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2017-07-12"
                }
            ],
            "Pair": None
        },
        {
            "Name": "MATCHA",
            "Code": "matcha",
            "Gender": 2,
            "Products": [
                {
                    "Name": "MATCHA",
                    "Engine": "vocaloid_4",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2017-07-12"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Amy",
            "Code": "amy",
            "Gender": 2,
            "Products": [
                {
                    "Name": "Amy",
                    "Engine": "vocaloid_5",
                    "Vendors": ["yamaha"],
                    "Languages": ["EN"],
					"Voice": None,
                    "Date": "2018-07-12"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Chris",
            "Code": "chris",
            "Gender": 1,
            "Products": [
                {
                    "Name": "Chris",
                    "Engine": "vocaloid_5",
                    "Vendors": ["yamaha"],
                    "Languages": ["EN"],
					"Voice": None,
                    "Date": "2018-07-12"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Kaori",
            "Code": "kaori",
            "Gender": 2,
            "Products": [
                {
                    "Name": "Kaori",
                    "Engine": "vocaloid_5",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2018-07-12"
                }
            ],
            "Pair": None
        },
        {
            "Name": "Ken",
            "Code": "ken",
            "Gender": 1,
            "Products": [
                {
                    "Name": "Ken",
                    "Engine": "vocaloid_5",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2018-07-12"
                }
            ],
            "Pair": None
        },
        {
            "Name": "???????????????",
            "Code": "utatane_piko",
            "Gender": 1,
            "Products": [
                {
                    "Name": "???????????????",
                    "Engine": "vocaloid_2",
                    "Vendors": ["kioon_music"],
                    "Languages": ["JA"],
					"Voice": "??????",
                    "Date": "2010-12-08"
                }
            ],
            "Pair": None
        },
        {
            "Name": "SeeU",
            "Code": "seeu",
            "Gender": 2,
            "Products": [
                {
                    "Name": "SeeU",
                    "Engine": "vocaloid_3",
                    "Vendors": ["sbs_artech"],
                    "Languages": ["KO", "JA"],
					"Voice": "??????",
                    "Date": "2011-10-21"
                }
            ],
            "Pair": None
        },
        {
            "Name": "BRUNO",
            "Code": "bruno",
            "Gender": 1,
            "Products": [
                {
                    "Name": "BRUNO",
                    "Engine": "vocaloid_3",
                    "Vendors": ["voctro_labs"],
                    "Languages": ["ES"],
					"Voice": None,
                    "Date": "2011-12-23"
                }
            ],
            "Pair": None
        },
        {
            "Name": "CLARA",
            "Code": "clara",
            "Gender": 2,
            "Products": [
                {
                    "Name": "CLARA",
                    "Engine": "vocaloid_3",
                    "Vendors": ["voctro_labs"],
                    "Languages": ["ES"],
					"Voice": None,
                    "Date": "2011-12-23"
                }
            ],
            "Pair": None
        },
        {
            "Name": "MAIKA",
            "Code": "maika",
            "Gender": 2,
            "Products": [
                {
                    "Name": "MAIKA",
                    "Engine": "vocaloid_3",
                    "Vendors": ["voctro_labs"],
                    "Languages": ["ES", "PT", "IT", "CA", "EN", "JA"],
					"Voice": None,
                    "Date": "2013-12-18"
                }
            ],
            "Pair": None
        },
        {
            "Name": "IA",
            "Code": "ia",
            "Gender": 2,
            "Products": [
                {
                    "Name": "IA",
                    "Engine": "vocaloid_3",
                    "Vendors": ["1st_place"],
                    "Languages": ["JA"],
					"Voice": "Lia",
                    "Date": "2012-01-27"
                },
                {
                    "Name": "IA ROCKS",
                    "Engine": "vocaloid_3",
                    "Vendors": ["1st_place"],
                    "Languages": ["JA"],
					"Voice": "Lia",
                    "Date": "2014-06-27"
                }
            ],
            "Pair": None
        },
        {
            "Name": "?????????",
            "Code": "luo_tianyi",
            "Gender": 2,
            "Products": [
                {
                    "Name": "?????????",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "??????",
                    "Date": "2012-07-12"
                },
                {
                    "Name": "????????? V4",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "??????",
                    "Date": "2017-12-30"
                },
                {
                    "Name": "????????? V4",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["JA"],
					"Voice": "??????",
                    "Date": "2018-05-21"
                }
            ],
            "Pair": None
        },
        {
            "Name": "??????",
            "Code": "yanhe",
            "Gender": 2,
            "Products": [
                {
                    "Name": "??????",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "????????????",
                    "Date": "2013-07-11"
                }
            ],
            "Pair": None
        },
        {
            "Name": "?????????",
            "Code": "yuezheng_ling",
            "Gender": 2,
            "Products": [
                {
                    "Name": "?????????",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "???Inory",
                    "Date": "2015-07-17"
                }
            ],
            "Pair": None
        },
        {
            "Name": "??????",
            "Code": "stardust",
            "Gender": 2,
            "Products": [
                {
                    "Name": "??????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "?????????",
                    "Date": "2016-04-13"
                }
            ],
            "Pair": None
        },
        {
            "Name": "????????????",
            "Code": "yuezheng_longya",
            "Gender": 1,
            "Products": [
                {
                    "Name": "????????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "??????",
                    "Date": "2017-05-10"
                }
            ],
            "Pair": None
        },
        {
            "Name": "????????????",
            "Code": "zhiyumoke",
            "Gender": 1,
            "Products": [
                {
                    "Name": "????????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "?????????",
                    "Date": "2018-08-02"
                }
            ],
            "Pair": None
        },
        {
            "Name": "?????????",
            "Code": "mo_qingxian",
            "Gender": 2,
            "Products": [
                {
                    "Name": "?????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "??????",
                    "Date": "2018-08-02"
                }
            ],
            "Pair": None
        },
        {
            "Name": "MAYU",
            "Code": "mayu",
            "Gender": 2,
            "Products": [
                {
                    "Name": "MAYU",
                    "Engine": "vocaloid_3",
                    "Vendors": ["exit_tunes"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2012-12-05"
                }
            ],
            "Pair": None
        },
        {
            "Name": "???????????????",
            "Code": "macne_nana",
            "Gender": 2,
            "Products": [
                {
                    "Name": "???????????????",
                    "Engine": "vocaloid_3",
                    "Vendors": ["macne_nana_project"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2014-01-31"
                },
                {
                    "Name": "??????????????? ???????????????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["macne_nana_project"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2016-12-15"
                },
                {
                    "Name": "??????????????? ??????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["macne_nana_project"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2016-12-15"
                },
                {
                    "Name": "??????????????? English",
                    "Engine": "vocaloid_3",
                    "Vendors": ["macne_nana_project"],
                    "Languages": ["EN"],
					"Voice": "????????????",
                    "Date": "2014-01-31"
                },
                {
                    "Name": "??????????????? English",
                    "Engine": "vocaloid_4",
                    "Vendors": ["macne_nana_project"],
                    "Languages": ["EN"],
					"Voice": "????????????",
                    "Date": "2016-12-15"
                }
            ],
            "Pair": None
        },
        {
            "Name": "v flower",
            "Code": "v_flower",
            "Gender": 2,
            "Products": [
                {
                    "Name": "v flower",
                    "Engine": "vocaloid_3",
                    "Vendors": ["gynoid"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2014-05-09"
                },
                {
                    "Name": "v4 flower",
                    "Engine": "vocaloid_4",
                    "Vendors": ["gynoid"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2015-07-16"
                },
                {
                    "Name": "???????????????Talk flower",
                    "Engine": "voiceroid_2",
                    "Vendors": ["gynoid"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2020-04-03"
                }
            ],
            "Pair": None
        },
        {
            "Name": "??????",
            "Code": "xin_hua",
            "Gender": 2,
            "Products": [
                {
                    "Name": "??????",
                    "Engine": "vocaloid_3",
                    "Vendors": ["gynoid"],
                    "Languages": ["ZH-TW", "JA"],
					"Voice": "?????????",
                    "Date": "2015-02-10"
                },
                {
                    "Name": "??????",
                    "Engine": "vocaloid_4",
                    "Vendors": ["gynoid"],
                    "Languages": ["ZH-TW", "JA"],
					"Voice": "?????????",
                    "Date": "2017-09-22"
                }
            ],
            "Pair": None
        },
        {
            "Name": "????????????",
            "Code": "meika_hime",
            "Gender": 0,
            "Pair": "meika"
        },
        {
            "Name": "???????????????",
            "Code": "meika_mikoto",
            "Gender": 0,
            "Pair": "meika"
        },
        {
            "Name": "Rana",
            "Code": "rana",
            "Gender": 2,
            "Products": [
                {
                    "Name": "Rana",
                    "Engine": "vocaloid_3",
                    "Vendors": ["weve"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2014-09-09"
                },
                {
                    "Name": "Rana V4",
                    "Engine": "vocaloid_4",
                    "Vendors": ["weve"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2015-12-01"
                }
            ],
            "Pair": None
        },
        {
            "Name": "UNI",
            "Code": "uni",
            "Gender": 2,
            "Products": [
                {
                    "Name": "UNI",
                    "Engine": "vocaloid_4",
                    "Vendors": ["weve"],
                    "Languages": ["KO"],
					"Voice": None,
                    "Date": "2017-02-14"
                }
            ],
            "Pair": None
        },
        {
            "Name": "LUMi",
            "Code": "lumi",
            "Gender": 2,
            "Products": [
                {
                    "Name": "LUMi",
                    "Engine": "vocaloid_4",
                    "Vendors": ["akatsuki_virtual_artists"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2017-08-30"
                }
            ],
            "Pair": None
        },
        {
            "Name": "????????????",
            "Code": "tsukuyomi_ai",
            "Gender": 2,
            "Products": [
                {
                    "Name": "????????????",
                    "Engine": "voiceroid",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2009-12-04"
                },
                {
                    "Name": "VOICEROID+ ???????????? EX",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": None
                }
            ],
            "Pair": None
        },
        {
            "Name": "??????????????????",
            "Code": "tsukuyomi_shouta",
            "Gender": 1,
            "Products": [
                {
                    "Name": "??????????????????",
                    "Engine": "voiceroid",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2009-12-04"
                },
                {
                    "Name": "VOICEROID+ ?????????????????? EX",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": None
                }
            ],
            "Pair": None
        },
        {
            "Name": "????????????????????? ????????????",
            "Code": "yoshidaroid",
            "Gender": 1,
            "Products": [
                {
                    "Name": "VOICEROID+ ????????? ????????????",
                    "Engine": "voiceroid_plus",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2010-10-22"
                },
                {
                    "Name": "VOICEROID+ ????????? ???????????? EX",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": None
                }
            ],
            "Pair": None
        },
        {
            "Name": "???????????????",
            "Code": "tamiyasu_tomoe",
            "Gender": 2,
            "Products": [
                {
                    "Name": "VOICEROID+ ???????????????",
                    "Engine": "voiceroid_plus",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2010-10-22"
                },
                {
                    "Name": "VOICEROID+ ??????????????? EX",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": None
                }
            ],
            "Pair": None
        },
        {
            "Name": "?????????",
            "Code": "kotonoha_akane",
            "Gender": 2,
            "Pair": "kotonoha"
        },
        {
            "Name": "?????????",
            "Code": "kotonoha_aoi",
            "Gender": 2,
            "Pair": "kotonoha"
        },
        {
            "Name": "???????????????",
            "Code": "minase_kou",
            "Gender": 1,
            "Products": [
                {
                    "Name": "VOICEROID+ ??????????????? EX",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2015-10-29"
                }
            ],
            "Pair": None
        },
        {
            "Name": "???????????????",
            "Code": "kyoumati_seika",
            "Gender": 2,
            "Products": [
                {
                    "Name": "VOICEROID+ ??????????????? EX",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2016-06-10"
                }
            ],
            "Pair": None
        },
        {
            "Name": "??????????????????",
            "Code": "touhoku_kiritan",
            "Gender": 2,
            "Products": [
                {
                    "Name": "VOICEROID+ ?????????????????? EX",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "???????????????",
                    "Date": "2016-10-27"
                }
            ],
            "Pair": None
        },
        {
            "Name": "???????????????",
            "Code": "touhoku_itako",
            "Gender": 2,
            "Products": [
                {
                    "Name": "VOICEROID2 ???????????????",
                    "Engine": "voiceroid_2",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2018-11-08"
                }
            ],
            "Pair": None
        },
        {
            "Name": "??????????????????",
            "Code": "tsuina_chan",
            "Gender": 2,
            "Products": [
                {
                    "Name": "VOICEROID2 ??????????????????",
                    "Engine": "voiceroid_2",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2019-11-01"
                }
            ],
            "Pair": None
        },
        {
            "Name": "????????????",
            "Code": "iori_yuduru",
            "Gender": 1,
            "Products": [
                {
                    "Name": "VOICEROID2 ????????????",
                    "Engine": "voiceroid_2",
                    "Vendors": ["ai"],
                    "Languages": ["JA"],
					"Voice": "????????????",
                    "Date": "2020-02-27"
                }
            ],
            "Pair": None
        }
    ],
    "Pairs": [
        {
            "Name": "?????????????????????",
            "Code": "kagamine",
            "Products": [
                {
                    "Name": "?????????????????????",
                    "Engine": "vocaloid_2",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "????????????",
                    "Date": "2007-12-27"
                },
                {
                    "Name": "????????????????????? act2",
                    "Engine": "vocaloid_2",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "????????????",
                    "Date": "2008-07-18"
                },
                {
                    "Name": "????????????????????? Append",
                    "Engine": "vocaloid_2",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "????????????",
                    "Date": "2010-12-27"
                },
                {
                    "Name": "????????????????????? V4X",
                    "Engine": "vocaloid_4",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "????????????",
                    "Date": "2015-12-24"
                },
                {
                    "Name": "????????????????????? V4 ENGLISH",
                    "Engine": "vocaloid_4",
                    "Vendors": ["crypton"],
                    "Languages": ["EN"],
                    "Voice": "????????????",
                    "Date": "2015-12-24"
                }
            ]
        },
        {
            "Name": "ZOLA PROJECT",
            "Code": "zola_project",
            "Products": [
                {
                    "Name": "YUU",
                    "Engine": "vocaloid_3",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
                    "Voice": "????????????",
                    "Date": "2013-06-21"
                },
                {
                    "Name": "KYO",
                    "Engine": "vocaloid_3",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
                    "Voice": "???????????????",
                    "Date": "2013-06-21"
                },
                {
                    "Name": "WIL",
                    "Engine": "vocaloid_3",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
                    "Voice": "?????????",
                    "Date": "2013-06-21"
                }
            ]
        },
        {
            "Name": "????????????",
            "Code": "anon_kanon",
            "Products": [
                {
                    "Name": "??????",
                    "Engine": "vocaloid_3",
                    "Vendors": ["anokano_project", "yamaha"],
                    "Languages": ["JA"],
                    "Voice": None,
                    "Date": "2014-03-03"
                },
                {
                    "Name": "??????",
                    "Engine": "vocaloid_3",
                    "Vendors": ["anokano_project", "yamaha"],
                    "Languages": ["JA"],
                    "Voice": None,
                    "Date": "2014-03-03"
                }
            ]
        },
        {
            "Name": "????????????????????????",
            "Code": "meika",
            "Products": [
                {
                    "Name": "????????????????????????",
                    "Engine": "vocaloid_5",
                    "Vendors": ["gynoid"],
                    "Languages": ["JA"],
                    "Voice": "??????????????????",
                    "Date": "2019-03-30"
                }
            ]
        },
        {
            "Name": "???????????????",
            "Code": "kotonoha",
            "Products": [
                {
                    "Name": "???????????????",
                    "Engine": "voiceroid_plus",
                    "Vendors": ["gynoid"],
                    "Languages": ["JA"],
                    "Voice": "????????????",
                    "Date": "2014-04-25"
                }
            ]
        }
    ],
    "Vendors": [
        {"Name": "ZERO-G", "Code": "zero_g", "Country": "GB"},
        {"Name": "???????????????????????????????????????????????????", "Code": "crypton", "Country": "JP"},
        {"Name": "PowerFX", "Code": "powerfx", "Country": "SE"},
        {"Name": "?????????????????????", "Code": "internet", "Country": "JP"},
        {"Name": "AH-Software", "Code": "ahs", "Country": "JP"},
        {"Name": "?????????", "Code": "yamaha", "Country": "JP"},
        {"Name": "??????????????????????????????", "Code": "kioon_music", "Country": "JP"},
        {"Name": "SBS Artech", "Code": "sbs_artech", "Country": "KR"},
        {"Name": "Voctro Labs", "Code": "voctro_labs", "Country": "ES"},
        {"Name": "1st PLACE", "Code": "1st_place", "Country": "JP"},
        {"Name": "????????????????????????????????????", "Code": "vocaloid_china", "Country": "CN"},
        {"Name": "EXIT TUNES", "Code": "exit_tunes", "Country": "JP"},
        {"Name": "?????????????????????????????????", "Code": "macne_nana_project", "Country": "JP"},
        {"Name": "???????????????", "Code": "gynoid", "Country": "JP"},
        {"Name": "????????????", "Code": "weve", "Country": "JP"},
        {"Name": "ST MEDiA", "Code": "st_media", "Country": "KR"},
        {"Name": "???????????????????????????????????????????????????", "Code": "akatsuki_virtual_artists", "Country": "JP"},
        {"Name": "Avex Group", "Code": "avex", "Country": "JP"},
        {"Name": "Dreamtonics", "Code": "dreamtonics", "Country": "JP"},
        {"Name": "CeVIO Project", "Code": "cevio_project", "Country": "JP", "Companies": [{"Name": "????????????????????????", "Country": "JP"}, {"Name": "?????????????????????????????????????????????????????????", "Country": "JP"}, {"Name": "?????????????????????", "Country": "JP"}, {"Name": "???????????????", "Country": "JP"}, {"Name": "??????????????????????????????", "Country": "JP"}]},
        {"Name": "VOCALOMAKETS", "Code": "vocalomakets", "Country": "JP"},
        {"Name": "SSS????????????", "Code": "sss", "Country": "JP"},
        {"Name": "??????????????????", "Code": "bplats", "Country": "JP"},
        {"Name": "?????????????????????", "Code": "dearstage", "Country": "JP"},
        {"Name": "i-style Project", "Code": "i_style", "Country": "JP", "Companies": [{"Name": "????????????????????????", "Country": "JP"}, {"Name": "?????????????????????????????????", "Country": "JP"}]},
        {"Name": "AnoKano Project", "Code": "anokano_project", "Country": "JP", "Companies": [{"Name": "????????????????????????????????????", "Country": "JP"}]},
        {"Name": "????????????", "Code": "ai", "Country": "JP"}
    ],
    "Engine": [
        {"Name": "VOCALOID1", "Code": "vocaloid_1", "Vendor": "yamaha"},
        {"Name": "VOCALOID2", "Code": "vocaloid_2", "Vendor": "yamaha"},
        {"Name": "VOCALOID3", "Code": "vocaloid_3", "Vendor": "yamaha"},
        {"Name": "VOCALOID4", "Code": "vocaloid_4", "Vendor": "yamaha"},
        {"Name": "VOCALOID5", "Code": "vocaloid_5", "Vendor": "yamaha"},

        {"Name": "VOICEROID", "Code": "voiceroid", "Vendor": "ahs"},
        {"Name": "VOICEROID+", "Code": "voiceroid_plus", "Vendor": "ahs"},
        {"Name": "VOICEROID+ EX", "Code": "voiceroid_plus_ex", "Vendor": "ahs"},
        {"Name": "VOICEROID2", "Code": "voiceroid_2", "Vendor": "ahs"},

        {"Name": "CeVIO Creative Studio", "Code": "cevio_cs", "Vendor": "cevio_project"},
        {"Name": "CeVIO AI", "Code": "cevio_ai", "Vendor": "cevio_project"},
        {"Name": "CeVIO Pro", "Code": "cevio_pro", "Vendor": "cevio_project"},

        {"Name": "Synthesizer V R1", "Code": "synthv_r1", "Vendor": "dreamtonics"},
        {"Name": "Synthesizer V R2", "Code": "synthv_r2", "Vendor": "dreamtonics"},
        {"Name": "Synthesizer V R2 Lite", "Code": "synthv_r2lite", "Vendor": "dreamtonics"},
        {"Name": "Synthesizer V AI", "Code": "synthv_ai", "Vendor": "dreamtonics"},
        {"Name": "Synthesizer V AI Lite", "Code": "synthv_ailite", "Vendor": "dreamtonics"}
    ],
    "Update-Date": "2021-05-04",
    "Version": 1,
    "Credits": [
        "https://vocadb.net/",
        "https://ja.wikipedia.org/wiki/VOCALOID",
        "https://ja.wikipedia.org/wiki/VOICEROID",
        "https://ja.wikipedia.org/wiki/CeVIO",
        "https://ja.wikipedia.org/wiki/Synthesizer V",
        "https://dic.pixiv.net/a/VOICEROID"
    ]
}
