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
                    "Voice": "拝郷メイコ",
                    "Date": "2004-11-05"
                },
                {
                    "Name": "MEIKO V3",
                    "Engine": "vocaloid_3",
                    "Vendors": ["crypton"],
                    "Languages": ["JA", "EN"],
                    "Voice": "拝郷メイコ",
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
                    "Voice": "風雅なおと",
                    "Date": "2006-02-17"
                },
                {
                    "Name": "KAITO V3",
                    "Engine": "vocaloid_3",
                    "Vendors": ["crypton"],
                    "Languages": ["JA", "EN"],
                    "Voice": "風雅なおと",
                    "Date": "2013-02-15"
                }
            ],
            "Pair": None
        },
        {
            "Name": "初音ミク",
            "Code": "hatsune_miku",
            "Gender": 2,
            "Products": [
                {
                    "Name": "初音ミク",
                    "Engine": "vocaloid_2",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "藤田咲",
                    "Date": "2007-08-31"
                },
                {
                    "Name": "初音ミク Append",
                    "Engine": "vocaloid_2",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "藤田咲",
                    "Date": "2010-04-30"
                },
                {
                    "Name": "初音ミク V3",
                    "Engine": "vocaloid_3",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "藤田咲",
                    "Date": "2013-09-26"
                },
                {
                    "Name": "初音ミク V3 ENGLISH",
                    "Engine": "vocaloid_3",
                    "Vendors": ["crypton"],
                    "Languages": ["EN"],
                    "Voice": "藤田咲",
                    "Date": "2013-08-31"
                },
                {
                    "Name": "初音ミク V4X",
                    "Engine": "vocaloid_4",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "藤田咲",
                    "Date": "2016-08-31"
                },
                {
                    "Name": "初音ミク V4 ENGLISH",
                    "Engine": "vocaloid_4",
                    "Vendors": ["crypton"],
                    "Languages": ["EN"],
                    "Voice": "藤田咲",
                    "Date": "2016-08-31"
                },
                {
                    "Name": "初音ミク V4 CHINESE",
                    "Engine": "vocaloid_4",
                    "Vendors": ["crypton"],
                    "Languages": ["ZH-CN"],
                    "Voice": "藤田咲",
                    "Date": "2017-08-31"
                }
            ],
            "Pair": None
        },
        {
            "Name": "鏡音リン",
            "Code": "kagamine_rin",
            "Gender": 2,
            "Pair": "kagamine"
        },
        {
            "Name": "鏡音レン",
            "Code": "kagamine_len",
            "Gender": 1,
            "Pair": "kagamine"
        },
        {
            "Name": "巡音ルカ",
            "Code": "megurine_ruka",
            "Gender": 2,
            "Products": [
                {
                    "Name": "巡音ルカ",
                    "Engine": "vocaloid_2",
                    "Vendors": ["crypton"],
                    "Languages": ["JA", "EN"],
					"Voice": "浅川悠",
                    "Date": "2009-01-30"
                },
                {
                    "Name": "巡音ルカ V4X",
                    "Engine": "vocaloid_4",
                    "Vendors": ["crypton"],
                    "Languages": ["JA", "EN"],
                    "Voice": "浅川悠",
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
            "Name": "がくっぽいど",
            "Code": "gackpoid",
            "Gender": 1,
            "Products": [
                {
                    "Name": "がくっぽいど",
                    "Engine": "vocaloid_2",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "GACKT",
                    "Date": "2008-07-31"
                },
                {
                    "Name": "がくっぽいど NATIVE",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "GACKT",
                    "Date": "2012-07-13"
                },
                {
                    "Name": "がくっぽいど NATIVE",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "GACKT",
                    "Date": "2015-04-30"
                },
                {
                    "Name": "がくっぽいど POWER",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "GACKT",
                    "Date": "2012-07-13"
                },
                {
                    "Name": "がくっぽいど POWER",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "GACKT",
                    "Date": "2015-04-30"
                },
                {
                    "Name": "がくっぽいど WHISPER",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "GACKT",
                    "Date": "2012-07-13"
                },
                {
                    "Name": "がくっぽいど WHISPER",
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
					"Voice": "中島愛",
                    "Date": "2009-06-26"
                },
                {
                    "Name": "Megpoid Power",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "中島愛",
                    "Date": "2011-10-21"
                },
                {
                    "Name": "Megpoid Power",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "中島愛",
                    "Date": "2015-11-05"
                },
                {
                    "Name": "Megpoid Whisper",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "中島愛",
                    "Date": "2011-10-21"
                },
                {
                    "Name": "Megpoid Whisper",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "中島愛",
                    "Date": "2015-11-05"
                },
                {
                    "Name": "Megpoid Adult",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "中島愛",
                    "Date": "2011-10-21"
                },
                {
                    "Name": "Megpoid Adult",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "中島愛",
                    "Date": "2015-11-05"
                },
                {
                    "Name": "Megpoid Sweet",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "中島愛",
                    "Date": "2011-10-21"
                },
                {
                    "Name": "Megpoid Sweet",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "中島愛",
                    "Date": "2015-11-05"
                },
                {
                    "Name": "Megpoid Native",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "中島愛",
                    "Date": "2012-03-16"
                },
                {
                    "Name": "Megpoid Native",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "中島愛",
                    "Date": "2015-11-05"
                },
                {
                    "Name": "Megpoid English",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["EN"],
					"Voice": "中島愛",
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
            "Name": "ガチャッポイド",
            "Code": "gachapoid",
            "Gender": 1,
            "Products": [
                {
                    "Name": "ガチャッポイド",
                    "Engine": "vocaloid_2",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "ガチャピン",
                    "Date": "2010-10-08"
                },
                {
                    "Name": "ガチャッポイド V3",
                    "Engine": "vocaloid_3",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "ガチャピン",
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
					"Voice": "喜多村英梨",
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
					"Voice": "伊藤千晃",
                    "Date": "2014-10-16"
                }
            ],
            "Pair": None
        },
        {
            "Name": "音街ウナ",
            "Code": "otomachi_una",
            "Gender": 2,
            "Products": [
                {
                    "Name": "音街ウナ",
                    "Engine": "vocaloid_4",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "田中あいみ",
                    "Date": "2016-07-30"
                },
                {
                    "Name": "音街ウナTalk Ex",
                    "Engine": "voiceroid_2",
                    "Vendors": ["internet"],
                    "Languages": ["JA"],
					"Voice": "田中あいみ",
                    "Date": "2017-04-20"
                }
            ],
            "Pair": None
        },
        {
            "Name": "氷山キヨテル",
            "Code": "hiyama_kiyoteru",
            "Gender": 1,
            "Products": [
                {
                    "Name": "氷山キヨテル",
                    "Engine": "vocaloid_2",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "比山貴咏史",
                    "Date": "2009-12-04"
                },
                {
                    "Name": "氷山キヨテル ナチュラル",
                    "Engine": "vocaloid_4",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "比山貴咏史",
                    "Date": "2015-10-29"
                },
                {
                    "Name": "氷山キヨテル ロック",
                    "Engine": "vocaloid_4",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "比山貴咏史",
                    "Date": "2015-10-29"
                }
            ],
            "Pair": None
        },
        {
            "Name": "歌愛ユキ",
            "Code": "kaai_yuki",
            "Gender": 2,
            "Products": [
                {
                    "Name": "歌愛ユキ",
                    "Engine": "vocaloid_2",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2009-12-04"
                },
                {
                    "Name": "歌愛ユキ ナチュラル",
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
            "Name": "SF-A2 開発コード miki",
            "Code": "miki",
            "Gender": 2,
            "Products": [
                {
                    "Name": "SF-A2 開発コード miki",
                    "Engine": "vocaloid_2",
                    "Vendors": ["yamaha", "ahs"],
                    "Languages": ["JA"],
					"Voice": "フルカワミキ",
                    "Date": "2009-12-04"
                },
                {
                    "Name": "miki ナチュラル",
                    "Engine": "vocaloid_4",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "フルカワミキ",
                    "Date": "2015-06-18"
                }
            ],
            "Pair": None
        },
        {
            "Name": "猫村いろは",
            "Code": "nekomura_iroha",
            "Gender": 2,
            "Products": [
                {
                    "Name": "猫村いろは",
                    "Engine": "vocaloid_2",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "佳館杏ノ助",
                    "Date": "2010-10-22"
                },
                {
                    "Name": "猫村いろは ナチュラル",
                    "Engine": "vocaloid_4",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "佳館杏ノ助",
                    "Date": "2015-06-18"
                },
                {
                    "Name": "猫村いろは ソフト",
                    "Engine": "vocaloid_4",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "佳館杏ノ助",
                    "Date": "2015-06-18"
                }
            ],
            "Pair": None
        },
        {
            "Name": "結月ゆかり",
            "Code": "yuduki_yukari",
            "Gender": 2,
            "Products": [
                {
                    "Name": "結月ゆかり",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "石黒千尋",
                    "Date": "2011-12-22"
                },
                {
                    "Name": "結月ゆかり 純",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "石黒千尋",
                    "Date": "2015-03-18"
                },
                {
                    "Name": "結月ゆかり 穏",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "石黒千尋",
                    "Date": "2015-03-18"
                },
                {
                    "Name": "結月ゆかり 凛",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "石黒千尋",
                    "Date": "2015-03-18"
                },
                {
                    "Name": "VOICEROID+ 結月ゆかり",
                    "Engine": "voiceroid_plus",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "石黒千尋",
                    "Date": "2011-12-22"
                },
                {
                    "Name": "VOICEROID+ EX 結月ゆかり",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "石黒千尋",
                    "Date": "2014-10-30"
                },
                {
                    "Name": "VOICEROID2 結月ゆかり",
                    "Engine": "voiceroid_2",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "石黒千尋",
                    "Date": "2017-06-09"
                }
            ],
            "Pair": None
        },
        {
            "Name": "東北ずん子",
            "Code": "touhoku_zunko",
            "Gender": 2,
            "Products": [
                {
                    "Name": "東北ずん子",
                    "Engine": "vocaloid_3",
                    "Vendors": ["sss", "ahs"],
                    "Languages": ["JA"],
					"Voice": "佐藤聡美",
                    "Date": "2014-06-05"
                },
                {
                    "Name": "東北ずん子 ナチュラル",
                    "Engine": "vocaloid_4",
                    "Vendors": ["sss", "ahs"],
                    "Languages": ["JA"],
					"Voice": "佐藤聡美",
                    "Date": "2016-10-27"
                },
                {
                    "Name": "VOICEROID+ 東北ずん子",
                    "Engine": "voiceroid_plus",
                    "Vendors": ["sss", "ahs"],
                    "Languages": ["JA"],
					"Voice": "佐藤聡美",
                    "Date": "2012-09-28"
                },
                {
                    "Name": "VOICEROID+ EX 東北ずん子",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["sss", "ahs"],
                    "Languages": ["JA"],
					"Voice": "佐藤聡美",
                    "Date": "2014-10-30"
                }
            ],
            "Pair": None
        },
        {
            "Name": "紲星あかり",
            "Code": "kizuna_akari",
            "Gender": 2,
            "Products": [
                {
                    "Name": "紲星あかり",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "米澤円",
                    "Date": "2018-04-26"
                },
                {
                    "Name": "VOICEROID2 紲星あかり",
                    "Engine": "voiceroid_2",
                    "Vendors": ["vocalomakets", "ahs"],
                    "Languages": ["JA"],
					"Voice": "米澤円",
                    "Date": "2017-12-22"
                }
            ],
            "Pair": None
        },
        {
            "Name": "桜乃そら",
            "Code": "haruno_sora",
            "Gender": 2,
            "Products": [
                {
                    "Name": "桜乃そら ナチュラル",
                    "Engine": "vocaloid_5",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "井上喜久子",
                    "Date": "2018-07-26"
                },
                {
                    "Name": "桜乃そら クール",
                    "Engine": "vocaloid_5",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "井上喜久子",
                    "Date": "2018-07-26"
                },
                {
                    "Name": "VOICEROID2 桜乃そら",
                    "Engine": "voiceroid_2",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "井上喜久子",
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
					"Voice": "坂本美雨",
                    "Date": "2011-10-21"
                }
            ],
            "Pair": None
        },
        {
            "Name": "兎眠りおん",
            "Code": "tone_rion",
            "Gender": 2,
            "Products": [
                {
                    "Name": "兎眠りおん",
                    "Engine": "vocaloid_3",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": "夢眠ねむ",
                    "Date": "2011-12-16"
                },
                {
                    "Name": "兎眠りおん",
                    "Engine": "vocaloid_4",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": "夢眠ねむ",
                    "Date": "2017-02-16"
                }
            ],
            "Pair": None
        },
        {
            "Name": "蒼姫ラピス",
            "Code": "aoki_lapis",
            "Gender": 2,
            "Products": [
                {
                    "Name": "蒼姫ラピス",
                    "Engine": "vocaloid_3",
                    "Vendors": ["i_style", "yamaha"],
                    "Languages": ["JA"],
					"Voice": "江口菜子",
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
            "Name": "メルリ",
            "Code": "merli",
            "Gender": 2,
            "Products": [
                {
                    "Name": "メルリ",
                    "Engine": "vocaloid_3",
                    "Vendors": ["i_style", "yamaha"],
                    "Languages": ["JA"],
					"Voice": "鎌田美沙紀",
                    "Date": "2013-12-24"
                }
            ],
            "Pair": None
        },
        {
            "Name": "杏音",
            "Code": "anon",
            "Gender": 2,
            "Pair": "anon_kanon"
        },
        {
            "Name": "鳥音",
            "Code": "kanon",
            "Gender": 2,
            "Pair": "anon_kanon"
        },
        {
            "Name": "ギャラ子 NEO",
            "Code": "galaco_neo",
            "Gender": 2,
            "Products": [
                {
                    "Name": "ギャラ子 NEO",
                    "Engine": "vocaloid_3",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": "柴咲コウ",
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
					"Voice": "小林幸子",
                    "Date": "2015-07-27"
                }
            ],
            "Pair": None
        },
        {
            "Name": "アルスロイド",
            "Code": "arsloid",
            "Gender": 1,
            "Products": [
                {
                    "Name": "アルスロイド",
                    "Engine": "vocaloid_4",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
					"Voice": "神生アキラ",
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
					"Voice": "角元明日香",
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
            "Name": "夢眠ネム",
            "Code": "yumemi_nemu",
            "Gender": 2,
            "Products": [
                {
                    "Name": "夢眠ネム",
                    "Engine": "vocaloid_4",
                    "Vendors": ["dearstage", "yamaha"],
                    "Languages": ["JA", "EN"],
					"Voice": "夢眠ねむ",
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
					"Voice": "大坪由佳",
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
					"Voice": "大橋彩香",
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
            "Name": "歌手音ピコ",
            "Code": "utatane_piko",
            "Gender": 1,
            "Products": [
                {
                    "Name": "歌手音ピコ",
                    "Engine": "vocaloid_2",
                    "Vendors": ["kioon_music"],
                    "Languages": ["JA"],
					"Voice": "ピコ",
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
					"Voice": "다희",
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
            "Name": "洛天依",
            "Code": "luo_tianyi",
            "Gender": 2,
            "Products": [
                {
                    "Name": "洛天依",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "山新",
                    "Date": "2012-07-12"
                },
                {
                    "Name": "洛天依 V4",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "山新",
                    "Date": "2017-12-30"
                },
                {
                    "Name": "洛天依 V4",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["JA"],
					"Voice": "鹿乃",
                    "Date": "2018-05-21"
                }
            ],
            "Pair": None
        },
        {
            "Name": "言和",
            "Code": "yanhe",
            "Gender": 2,
            "Products": [
                {
                    "Name": "言和",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "劉セイラ",
                    "Date": "2013-07-11"
                }
            ],
            "Pair": None
        },
        {
            "Name": "楽正綾",
            "Code": "yuezheng_ling",
            "Gender": 2,
            "Products": [
                {
                    "Name": "楽正綾",
                    "Engine": "vocaloid_3",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "祈Inory",
                    "Date": "2015-07-17"
                }
            ],
            "Pair": None
        },
        {
            "Name": "星塵",
            "Code": "stardust",
            "Gender": 2,
            "Products": [
                {
                    "Name": "星塵",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "茶理理",
                    "Date": "2016-04-13"
                }
            ],
            "Pair": None
        },
        {
            "Name": "楽正龍牙",
            "Code": "yuezheng_longya",
            "Gender": 1,
            "Products": [
                {
                    "Name": "楽正龍牙",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "張傑",
                    "Date": "2017-05-10"
                }
            ],
            "Pair": None
        },
        {
            "Name": "徵羽摩柯",
            "Code": "zhiyumoke",
            "Gender": 1,
            "Products": [
                {
                    "Name": "徵羽摩柯",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "苏尚卿",
                    "Date": "2018-08-02"
                }
            ],
            "Pair": None
        },
        {
            "Name": "墨清弦",
            "Code": "mo_qingxian",
            "Gender": 2,
            "Products": [
                {
                    "Name": "墨清弦",
                    "Engine": "vocaloid_4",
                    "Vendors": ["vocaloid_china"],
                    "Languages": ["ZH-CN"],
					"Voice": "冥月",
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
					"Voice": "森永真由美",
                    "Date": "2012-12-05"
                }
            ],
            "Pair": None
        },
        {
            "Name": "マクネナナ",
            "Code": "macne_nana",
            "Gender": 2,
            "Products": [
                {
                    "Name": "マクネナナ",
                    "Engine": "vocaloid_3",
                    "Vendors": ["macne_nana_project"],
                    "Languages": ["JA"],
					"Voice": "池澤春菜",
                    "Date": "2014-01-31"
                },
                {
                    "Name": "マクネナナ ナチュラル",
                    "Engine": "vocaloid_4",
                    "Vendors": ["macne_nana_project"],
                    "Languages": ["JA"],
					"Voice": "池澤春菜",
                    "Date": "2016-12-15"
                },
                {
                    "Name": "マクネナナ プチ",
                    "Engine": "vocaloid_4",
                    "Vendors": ["macne_nana_project"],
                    "Languages": ["JA"],
					"Voice": "池澤春菜",
                    "Date": "2016-12-15"
                },
                {
                    "Name": "マクネナナ English",
                    "Engine": "vocaloid_3",
                    "Vendors": ["macne_nana_project"],
                    "Languages": ["EN"],
					"Voice": "池澤春菜",
                    "Date": "2014-01-31"
                },
                {
                    "Name": "マクネナナ English",
                    "Engine": "vocaloid_4",
                    "Vendors": ["macne_nana_project"],
                    "Languages": ["EN"],
					"Voice": "池澤春菜",
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
                    "Name": "ガイノイドTalk flower",
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
            "Name": "心華",
            "Code": "xin_hua",
            "Gender": 2,
            "Products": [
                {
                    "Name": "心華",
                    "Engine": "vocaloid_3",
                    "Vendors": ["gynoid"],
                    "Languages": ["ZH-TW", "JA"],
					"Voice": "王文儀",
                    "Date": "2015-02-10"
                },
                {
                    "Name": "心華",
                    "Engine": "vocaloid_4",
                    "Vendors": ["gynoid"],
                    "Languages": ["ZH-TW", "JA"],
					"Voice": "王文儀",
                    "Date": "2017-09-22"
                }
            ],
            "Pair": None
        },
        {
            "Name": "鳴花ヒメ",
            "Code": "meika_hime",
            "Gender": 0,
            "Pair": "meika"
        },
        {
            "Name": "鳴花ミコト",
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
					"Voice": "加隈亜衣",
                    "Date": "2014-09-09"
                },
                {
                    "Name": "Rana V4",
                    "Engine": "vocaloid_4",
                    "Vendors": ["weve"],
                    "Languages": ["JA"],
					"Voice": "加隈亜衣",
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
					"Voice": "大原さやか",
                    "Date": "2017-08-30"
                }
            ],
            "Pair": None
        },
        {
            "Name": "月読アイ",
            "Code": "tsukuyomi_ai",
            "Gender": 2,
            "Products": [
                {
                    "Name": "月読アイ",
                    "Engine": "voiceroid",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2009-12-04"
                },
                {
                    "Name": "VOICEROID+ 月読アイ EX",
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
            "Name": "月読ショウタ",
            "Code": "tsukuyomi_shouta",
            "Gender": 1,
            "Products": [
                {
                    "Name": "月読ショウタ",
                    "Engine": "voiceroid",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": None,
                    "Date": "2009-12-04"
                },
                {
                    "Name": "VOICEROID+ 月読ショウタ EX",
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
            "Name": "秘密結社鷹の爪 吉田くん",
            "Code": "yoshidaroid",
            "Gender": 1,
            "Products": [
                {
                    "Name": "VOICEROID+ 鷹の爪 吉田くん",
                    "Engine": "voiceroid_plus",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "吉田くん",
                    "Date": "2010-10-22"
                },
                {
                    "Name": "VOICEROID+ 鷹の爪 吉田くん EX",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "吉田くん",
                    "Date": None
                }
            ],
            "Pair": None
        },
        {
            "Name": "民安ともえ",
            "Code": "tamiyasu_tomoe",
            "Gender": 2,
            "Products": [
                {
                    "Name": "VOICEROID+ 民安ともえ",
                    "Engine": "voiceroid_plus",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "民安ともえ",
                    "Date": "2010-10-22"
                },
                {
                    "Name": "VOICEROID+ 民安ともえ EX",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "民安ともえ",
                    "Date": None
                }
            ],
            "Pair": None
        },
        {
            "Name": "琴葉茜",
            "Code": "kotonoha_akane",
            "Gender": 2,
            "Pair": "kotonoha"
        },
        {
            "Name": "琴葉葵",
            "Code": "kotonoha_aoi",
            "Gender": 2,
            "Pair": "kotonoha"
        },
        {
            "Name": "水奈瀬コウ",
            "Code": "minase_kou",
            "Gender": 1,
            "Products": [
                {
                    "Name": "VOICEROID+ 水奈瀬コウ EX",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "民安ともえ",
                    "Date": "2015-10-29"
                }
            ],
            "Pair": None
        },
        {
            "Name": "京町セイカ",
            "Code": "kyoumati_seika",
            "Gender": 2,
            "Products": [
                {
                    "Name": "VOICEROID+ 京町セイカ EX",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "立花理香",
                    "Date": "2016-06-10"
                }
            ],
            "Pair": None
        },
        {
            "Name": "東北きりたん",
            "Code": "touhoku_kiritan",
            "Gender": 2,
            "Products": [
                {
                    "Name": "VOICEROID+ 東北きりたん EX",
                    "Engine": "voiceroid_plus_ex",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "茜屋日海夏",
                    "Date": "2016-10-27"
                }
            ],
            "Pair": None
        },
        {
            "Name": "東北イタコ",
            "Code": "touhoku_itako",
            "Gender": 2,
            "Products": [
                {
                    "Name": "VOICEROID2 東北イタコ",
                    "Engine": "voiceroid_2",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "木戸衣吹",
                    "Date": "2018-11-08"
                }
            ],
            "Pair": None
        },
        {
            "Name": "ついなちゃん",
            "Code": "tsuina_chan",
            "Gender": 2,
            "Products": [
                {
                    "Name": "VOICEROID2 ついなちゃん",
                    "Engine": "voiceroid_2",
                    "Vendors": ["ahs"],
                    "Languages": ["JA"],
					"Voice": "門脇舞以",
                    "Date": "2019-11-01"
                }
            ],
            "Pair": None
        },
        {
            "Name": "伊織弓鶴",
            "Code": "iori_yuduru",
            "Gender": 1,
            "Products": [
                {
                    "Name": "VOICEROID2 伊織弓鶴",
                    "Engine": "voiceroid_2",
                    "Vendors": ["ai"],
                    "Languages": ["JA"],
					"Voice": "松浦義之",
                    "Date": "2020-02-27"
                }
            ],
            "Pair": None
        }
    ],
    "Pairs": [
        {
            "Name": "鏡音リン・レン",
            "Code": "kagamine",
            "Products": [
                {
                    "Name": "鏡音リン・レン",
                    "Engine": "vocaloid_2",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "下田麻美",
                    "Date": "2007-12-27"
                },
                {
                    "Name": "鏡音リン・レン act2",
                    "Engine": "vocaloid_2",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "下田麻美",
                    "Date": "2008-07-18"
                },
                {
                    "Name": "鏡音リン・レン Append",
                    "Engine": "vocaloid_2",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "下田麻美",
                    "Date": "2010-12-27"
                },
                {
                    "Name": "鏡音リン・レン V4X",
                    "Engine": "vocaloid_4",
                    "Vendors": ["crypton"],
                    "Languages": ["JA"],
                    "Voice": "下田麻美",
                    "Date": "2015-12-24"
                },
                {
                    "Name": "鏡音リン・レン V4 ENGLISH",
                    "Engine": "vocaloid_4",
                    "Vendors": ["crypton"],
                    "Languages": ["EN"],
                    "Voice": "下田麻美",
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
                    "Voice": "みのルン",
                    "Date": "2013-06-21"
                },
                {
                    "Name": "KYO",
                    "Engine": "vocaloid_3",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
                    "Voice": "なのっくす",
                    "Date": "2013-06-21"
                },
                {
                    "Name": "WIL",
                    "Engine": "vocaloid_3",
                    "Vendors": ["yamaha"],
                    "Languages": ["JA"],
                    "Voice": "まうい",
                    "Date": "2013-06-21"
                }
            ]
        },
        {
            "Name": "杏音鳥音",
            "Code": "anon_kanon",
            "Products": [
                {
                    "Name": "杏音",
                    "Engine": "vocaloid_3",
                    "Vendors": ["anokano_project", "yamaha"],
                    "Languages": ["JA"],
                    "Voice": None,
                    "Date": "2014-03-03"
                },
                {
                    "Name": "鳥音",
                    "Engine": "vocaloid_3",
                    "Vendors": ["anokano_project", "yamaha"],
                    "Languages": ["JA"],
                    "Voice": None,
                    "Date": "2014-03-03"
                }
            ]
        },
        {
            "Name": "鳴花ヒメ・ミコト",
            "Code": "meika",
            "Products": [
                {
                    "Name": "鳴花ヒメ・ミコト",
                    "Engine": "vocaloid_5",
                    "Vendors": ["gynoid"],
                    "Languages": ["JA"],
                    "Voice": "小岩井ことり",
                    "Date": "2019-03-30"
                }
            ]
        },
        {
            "Name": "琴葉茜・葵",
            "Code": "kotonoha",
            "Products": [
                {
                    "Name": "琴葉茜・葵",
                    "Engine": "voiceroid_plus",
                    "Vendors": ["gynoid"],
                    "Languages": ["JA"],
                    "Voice": "榊原ゆい",
                    "Date": "2014-04-25"
                }
            ]
        }
    ],
    "Vendors": [
        {"Name": "ZERO-G", "Code": "zero_g", "Country": "GB"},
        {"Name": "クリプトン・フューチャー・メディア", "Code": "crypton", "Country": "JP"},
        {"Name": "PowerFX", "Code": "powerfx", "Country": "SE"},
        {"Name": "インターネット", "Code": "internet", "Country": "JP"},
        {"Name": "AH-Software", "Code": "ahs", "Country": "JP"},
        {"Name": "ヤマハ", "Code": "yamaha", "Country": "JP"},
        {"Name": "キューンミュージック", "Code": "kioon_music", "Country": "JP"},
        {"Name": "SBS Artech", "Code": "sbs_artech", "Country": "KR"},
        {"Name": "Voctro Labs", "Code": "voctro_labs", "Country": "ES"},
        {"Name": "1st PLACE", "Code": "1st_place", "Country": "JP"},
        {"Name": "上海禾念信息科技有限公司", "Code": "vocaloid_china", "Country": "CN"},
        {"Name": "EXIT TUNES", "Code": "exit_tunes", "Country": "JP"},
        {"Name": "マクネナナプロジェクト", "Code": "macne_nana_project", "Country": "JP"},
        {"Name": "ガイノイド", "Code": "gynoid", "Country": "JP"},
        {"Name": "ウィーヴ", "Code": "weve", "Country": "JP"},
        {"Name": "ST MEDiA", "Code": "st_media", "Country": "KR"},
        {"Name": "アカツキ・ヴァーチャルアーティスツ", "Code": "akatsuki_virtual_artists", "Country": "JP"},
        {"Name": "Avex Group", "Code": "avex", "Country": "JP"},
        {"Name": "Dreamtonics", "Code": "dreamtonics", "Country": "JP"},
        {"Name": "CeVIO Project", "Code": "cevio_project", "Country": "JP", "Companies": [{"Name": "アップフィールド", "Country": "JP"}, {"Name": "ソニー・ミュージックエンタテインメント", "Country": "JP"}, {"Name": "テクノスピーチ", "Country": "JP"}, {"Name": "ブイシンク", "Country": "JP"}, {"Name": "フロンティアワークス", "Country": "JP"}]},
        {"Name": "VOCALOMAKETS", "Code": "vocalomakets", "Country": "JP"},
        {"Name": "SSS合同会社", "Code": "sss", "Country": "JP"},
        {"Name": "ビープラッツ", "Code": "bplats", "Country": "JP"},
        {"Name": "ディアステージ", "Code": "dearstage", "Country": "JP"},
        {"Name": "i-style Project", "Code": "i_style", "Country": "JP", "Companies": [{"Name": "スタジオディーン", "Country": "JP"}, {"Name": "サーファーズパラダイス", "Country": "JP"}]},
        {"Name": "AnoKano Project", "Code": "anokano_project", "Country": "JP", "Companies": [{"Name": "アクセルエンターメディア", "Country": "JP"}]},
        {"Name": "エーアイ", "Code": "ai", "Country": "JP"}
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
