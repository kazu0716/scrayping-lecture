Mezzanine Test
====

## Overview

Victim application in penetration test of password list attack for my understanding by using Mezzanine like "Wordpress"
http://mezzanine.jupo.org/docs/

## Requirement
- python3
- pip3
- git

## Usage

- basic usage
    - modify "account_list.csv" file
    
```
(victim-app) kazu0716 MacBook-Pro-4 $ head -n 10 account_list.csv
richard59,richard59@green.biz,@2~OMZ025
melindajones,melindajones@lane.com,k9N?OPj76*fO
scottaguirre,scottaguirre@parker.com,4w7^1}43HNJ
fschmidt,fschmidt@osborn-hill.com,i%@9j~AJA^ja=O7
jamesvictor,jamesvictor@gmail.com,/p2].HI|zU
fyoung,fyoung@yahoo.com,"S,J|$<s7hE"
danielrodriguez,danielrodriguez@hughes-robinson.com,"F7,8uM8o3_Rl~6)"
juan28,juan28@patterson.com,DIj<5kK$W
cookdestiny,cookdestiny@lozano.org,}Qz26=$wA~
vsilva,vsilva@orr.org,z1^@G|MVH0m@Y
```

- admin page(CMS)
  - http://127.0.0.1:8000/admin/

- Other pages
  - http://127.0.0.1:8000/

## Install

```
git clone https://github.com/kazu0716/mezzanine-test.git
cd mezzanine-test/
pip3 install -r requirement.txt
python3 manage.py createdb
python manage.py runscript create_users
python3 manage.py runserver
```
