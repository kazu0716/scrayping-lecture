# Crawling & Scraping勉強会(内部向け)

## 事前準備
- VartualBox Installed
    - Windows: http://vboxmania.net/content/virtualbox%E3%82%92windows%E3%81%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB
    - Mac: https://pc-karuma.net/mac-virtualbox-install/
- Vagrant Install
    - Windows: https://weblabo.oscasierra.net/install-vagrant-onto-windows/
    - Mac: https://qiita.com/inouet/items/b36638adc2b5772db457
- お役立ちライブラリの確認
    - argparse: http://d.hatena.ne.jp/rudi/20100805/1281020304
    - configparser: https://www.python-izm.com/advanced/config_parser/
    - logging: https://qiita.com/amedama/items/b856b2f30c2f38665701
    - TinyDB: https://qiita.com/meznat/items/19cfc3ee2e145d4e5baf

- VMの起動

```
# 初回起動方法
(scrayping-lecture) kazu0716 MacBook-Pro-4 $ git clone https://github.com/kazu0716/scrayping-lecture.git
(scrayping-lecture) kazu0716 MacBook-Pro-4 $ cd scrayping-lecture/
(scrayping-lecture) kazu0716 MacBook-Pro-4 $ vagrant up
(scrayping-lecture) kazu0716 MacBook-Pro-4 $ vagrant ssh

# 参考: Vagrantの使い方 : https://qiita.com/skinoshita/items/57ac059ff8b1008f5e1d
```

- victim_appsの起動

```
01021657 CA2842 $ vagrant ssh
ubuntu@ubuntu-xenial:~$ cd scrayping-lecture/victim_apps/
# 下記DBにテーブルを作成&諸々の設定を自動に行う
ubuntu@ubuntu-xenial:~/scrayping-lecture/victim_apps$ python3 manage.py createdb
# 省略 #
Hit enter to use the default (127.0.0.1:8000):

Creating default site record: 127.0.0.1:8000 ...


Creating default account ...

Username (leave blank to use 'ubuntu'):
Email address: admin@example.com
Password:
Password (again):
Superuser created successfully.
Installed 2 object(s) from 1 fixture(s)

Would you like to install some initial demo pages?
Eg: About us, Contact form, Gallery. (yes/no): yes

Creating demo pages: About us, Contact form, Gallery ...

Installed 16 object(s) from 3 fixture(s)
# ユーザアカウントを自動作成するScript実行
ubuntu@ubuntu-xenial:~/scrayping-lecture/victim_apps$ python3 manage.py runscript create_users
# サーバ起動(Backgroundで実行)
ubuntu@ubuntu-xenial:~/scrayping-lecture/victim_apps$ nohup python3 manage.py runserver &
[1] 5332
ubuntu@ubuntu-xenial:~/scrayping-lecture/victim_apps$ nohup: ignoring input and appending output to 'nohup.out'
## エラーだとこの後エラーが出る。何もでなければOK
```

- answer scriptの実行

```
ubuntu@ubuntu-xenial:~/scrayping-lecture/answer$ cd/home/ubuntu/scrayping-lecture/answer
# requestsのレクチャの使い方
ubuntu@ubuntu-xenial:~/scrayping-lecture/answer$ python3 request_crawler.py -h
usage: request_crawler.py [-h] -u URL -f FILE_NAME

requests crawler for internal lecture

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     access url to want to get web-page as htlm file.
  -f FILE_NAME, --filename FILE_NAME
                        filename of output file which got by requetsts access
# scraperの使い方
ubuntu@ubuntu-xenial:~/scrayping-lecture/answer$ python3 scraper.py -h
usage: scraper.py [-h] -f FILE_NAME

scrayping script for internal lecture

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_NAME, --filename FILE_NAME
                        filename of input file to get some tags
# Seleniumの使い方
ubuntu@ubuntu-xenial:~/scrayping-lecture/answer$ python3 selenium_crawler.py
```

- Victimの確認
    - http://127.0.0.1:8000 へブラウザアクセス

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
