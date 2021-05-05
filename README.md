# Vocautils

<p align="center">
Useful command line tool for <b>VOCALOID</b> and <b>VOICEROID</b>.
</p>

---

<p align="center">
EN | <a href="https://github.com/kotonefami/vocautils/blob/master/README.ja.md">JA</a>
</p>

## Requirements
* \>= Python 2.7 (But 2.7 is not supported. It is recommended to use Python 3.)

## Installation
```sh
$ pip install git+https://github.com/kotonefami/vocautils
```
## Uninstallation
```sh
$ pip uninstall vocautils
$ reboot now
```
## Usage
### Singers list
```sh
$ voca singers
初音ミク  ♀ 
- Products:
    初音ミク
      Engine: VOCALOID2 (ヤマハ)
      Vendor: クリプトン・フューチャー・メディア (JP)
      Language: JA
      Voice: 藤田咲
      Release Date: 2007-08-31
    初音ミク Append
      Engine: VOCALOID2 (ヤマハ)
      Vendor: クリプトン・フューチャー・メディア (JP)
      Language: JA
      
      (and more)
```
```sh
$ voca singers -s
初音ミク  ♀ 
鏡音リン  ♀ 
鏡音レン  ♂ 
巡音ルカ  ♀ 
SWEET ANN  ♀ 
BIG-AL  ♂ 
OLIVER  ♂ 
YOHIOloid  ♂ 
Ruby  ♀ 
がくっぽいど  ♂ 

(and more)
```
### Search singer
```sh
$ voca flower
v flower  ♀ 
- Products:
    v flower
      Engine: VOCALOID3 (ヤマハ)
      Vendor: ガイノイド (JP)
      Language: JA
      Voice: Unpublished
      Release Date: 2014-05-09
    v4 flower
      Engine: VOCALOID4 (ヤマハ)
      Vendor: ガイノイド (JP)
      Language: JA
      Voice: Unpublished
      Release Date: 2015-07-16
    ガイノイドTalk flower
      Engine: VOICEROID2 (AH-Software)
      Vendor: ガイノイド (JP)
      Language: JA
      Voice: Unpublished
      Release Date: 2020-04-03
- Pair:
    Not a pair
```
### Vendors list
```sh
$ voca vendors
ZERO-G (GB)
クリプトン・フューチャー・メディア (JP)
PowerFX (SE)
インターネット (JP)
AH-Software (JP)
ヤマハ (JP)
キューンミュージック (JP)
SBS Artech (KR)
Voctro Labs (ES)
1st PLACE (JP)
上海禾念信息科技有限公司 (CN)
EXIT TUNES (JP)
マクネナナプロジェクト (JP)
ガイノイド (JP)

(and more)
```
### API
```python
>>> from vocautils.data import Data
>>> Data
{...}
```
## Features to be implemented
* Add product information for CeVIO and Synthesizer V products.
* Add information such as height and weight
* Add information on discontinued products
* Add ownership information settings
* Add option for narrow down engine
* grep support
* Completion support
* Multilingual support
* Windows support