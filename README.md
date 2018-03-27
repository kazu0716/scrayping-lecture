# Crawling & Scraping勉強会(内部向け)

## 事前準備
- MacへPython3のインストール(Python 3.6.4想定: 2018/3/27時点)
    - 参考: http://develtips.com/python/191
- Macへvirtualenv/virtualenvwrapperのインストール
    - 参考: http://salinger.github.io/blog/2013/01/16/2/
- お役立ちライブラリの確認
    - argparse: http://d.hatena.ne.jp/rudi/20100805/1281020304
    - configparser: https://www.python-izm.com/advanced/config_parser/
    - logging: https://qiita.com/amedama/items/b856b2f30c2f38665701
    - TinyDB: https://qiita.com/meznat/items/19cfc3ee2e145d4e5baf

- virtualenv環境の作成

```
kazu0716 $ mkvirtualenv scrayping_lecture -p python3
Running virtualenv with interpreter /usr/local/bin/python3
Using base prefix '/usr/local/Cellar/python/3.6.4_4/Frameworks/Python.framework/Versi
ons/3.6'
New python executable in /Users/01021657/.virtualenvs/scrayping_lecture/bin/python3.6
Also creating executable in /Users/01021657/.virtualenvs/scrayping_lecture/bin/python
Installing setuptools, pip, wheel...done.
kazu0716 $ workon
(scrayping_lecture) kazu0716 $
```

- victim_appsの起動

```
git clone https://github.com/kazu0716/scrayping-lecture.git
cd scrayping-lecture/victim_apps
pip install -r requirement.txt
python manage.py createdb
python manage.py runscript create_users
python manage.py runserver
.....
_d^^^^^^^^^b_
.d''           ``b.
.p'                `q.
.d'                   `b.
.d'                     `b.   * Mezzanine 4.2.3
::                       ::   * Django 1.10.8
::    M E Z Z A N I N E    ::  * Python 3.6.4
::                       ::   * SQLite 3.22.0
`p.                     .q'   * Darwin 16.7.0
`p.                   .q'

`b.                 .d'
`q..          ..p'
^q........p^
''''

Performing system checks...

System check identified no issues (0 silenced).
March 27, 2018 - 13:34:13
Django version 1.10.8, using settings 'vicim_app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## アジェンダ(1回目)
### ゴール: requetstsモジュールを利用し、HTMLが取得できるようになる

- パワーポイントによる基本のレクチャ
- victim appsの起動
- requestsモジュールを用いたcrawilng scriptの作成
     - requests: https://qiita.com/sqrtxx/items/49beaa3795925e7de666
- requestsを利用し `http://127.0.0.1:8000/` のHTMLを取得し、./htmlへhtmlファイルを保存する

## アジェンダ(2回目)
### ゴール: Beautiful Soupを利用し、HTMLの要素を取得できる

- 参考
    - HTMLのScrayping
        - Beautiful Soup: https://qiita.com/itkr/items/513318a9b5b92bd56185
    - Chromeデベロッパーツール
        - https://ferret-plus.com/1880

## アジェンダ(3回目)
### ゴール: ログインを実施し、ログイン後のHTMLの取得

- 参考
    - PythonでSeleniumを使ってスクレイピング (基礎)
        - https://qiita.com/kinpira/items/383b0fbee6bf229ea03d
    - Seleniumとは
        - https://codezine.jp/article/detail/10225
