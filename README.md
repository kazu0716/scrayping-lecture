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
pip install -r requirements.txt
python manage.py createdb
Operations to perform:
  Apply all migrations: admin, auth, blog, conf, contenttypes, core, django_comments, forms, galleries, generic, pages, redirects, sessions, sites, twitter
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sites.0001_initial... OK
  Applying blog.0001_initial... OK
  Applying blog.0002_auto_20150527_1555... OK
  Applying conf.0001_initial... OK
  Applying core.0001_initial... OK
  Applying core.0002_auto_20150414_2140... OK
  Applying django_comments.0001_initial... OK
  Applying django_comments.0002_update_user_email_field_length... OK
  Applying django_comments.0003_add_submit_date_index... OK
  Applying pages.0001_initial... OK
  Applying forms.0001_initial... OK
  Applying forms.0002_auto_20141227_0224... OK
  Applying forms.0003_emailfield... OK
  Applying forms.0004_auto_20150517_0510... OK
  Applying forms.0005_auto_20151026_1600... OK
  Applying galleries.0001_initial... OK
  Applying galleries.0002_auto_20141227_0224... OK
  Applying generic.0001_initial... OK
  Applying generic.0002_auto_20141227_0224... OK
  Applying pages.0002_auto_20141227_0224... OK
  Applying pages.0003_auto_20150527_1555... OK
  Applying redirects.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying sites.0002_alter_domain_unique... OK
  Applying twitter.0001_initial... OK

A site record is required.
Please enter the domain and optional port in the format 'domain:port'.
For example 'localhost:8000' or 'www.example.com'.
Hit enter to use the default (127.0.0.1:8000):

Creating default site record: 127.0.0.1:8000 ...


Creating default account ...

Username (leave blank to use 'kazu0716'): admin
Email address: admin@example.com
Password:
Password (again):
Superuser created successfully.
Installed 2 object(s) from 1 fixture(s)

Would you like to install some initial demo pages?
Eg: About us, Contact form, Gallery. (yes/no): yes

Creating demo pages: About us, Contact form, Gallery ...

Installed 16 object(s) from 3 fixture(s)

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
    - ChromeDriverのインストール(必須)
        - brew install chromedriver
