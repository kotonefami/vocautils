# Vocautils

<p align="center">
<b>VOCALOID</b> と <b>VOICEROID</b> の便利なコマンドラインツールです。
</p>

---

<p align="center">
<a href="https://github.com/kotonefami/vocautils/blob/master/README.md">EN</a> | JA
</p>

## 必要
* >= Python 2.7 (ただし 2.7 はサポートされていません。3 を使用するのをお勧めします。)

## インストール
```sh
$ pip install git+https://github.com/kotonefami/vocautils
```
## アンインストール
```sh
$ pip uninstall vocautils
$ reboot now
```
## 使い方
### シンガーリスト
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
### シンガー検索
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
### ベンダーリスト
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
## 実装予定の機能
* CeVIO と Synthesizer V のシンガー情報の追加
* 身長や体重などのキャラクター設定情報の追加
* 廃盤か否かの情報の追加
* 所有情報の追加
* エンジン絞り込みオプションの追加
* grep サポート
* シェル補完サポート
* 多言語対応
* Windows サポート