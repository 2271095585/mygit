# -*- coding: utf-8 -*-

#安装beautifulsoup
sudo apt-get install python-bs4 python-bs4-doc

#安装搜狗拼音（需要重启）
sudo apt-get install fcitx libssh2-1
wget "http://pinyin.sogou.com/linux/download.php?f=linux&bit=64" -O "sougou_64.deb"
sudo dpkg -i sougou_64.deb

#安装pip
sudo apt-get install python-pip

#安装scrapy
sudo pip install scrapy==0.24.6
#windows7下scrapy安装参照文章如下（相当麻烦）python 2.7.12 32位
http://blog.csdn.net/playstudy/article/details/17296473

#安装beautifulsoup
pip install beautifulsoup4

#安装html5lib
easy_install html5lib (要求setuptools 16.8以上)

#安装git
sudo apt-get install git

#安装vim
sudo apt-get install vim

#install mysql
sudo apt-get install mysql-server -y

#install jdk version 7
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java7-installer -y

#install mysql
sudo apt-get install mysql-server -y

#install jdk version 7
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java7-installer -y


#install vim
sudo apt-get install vim -y --fix-missing

#install pip
sudo apt-get install python-pip -y --fix-missing

#install python-MySQLdb for torndb
sudo apt-get install python-MySQLdb -y

#install tornado:the latest version
sudo apt-get install tornado

#install torndb using pip tool
sudo apt-get install torndb

#install sublime-text-2
sudo add-apt-repository ppa:webupd8team/sublime-text-2 -y
sudo apt-get update
sudo apt-get install sublime-text -y

#install nodejs: the latest version
sudo apt-get install python-software-properties -y
sudo apt-add-repository ppa:chris-lea/node.js
sudo apt-get update

#install浏览器charm
wget -c wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-*.deb
sudo apt-get install -f -y


#安装beanstalkc
sudo pip install pyyaml
sudo pip install beanstalkc

#redis安装
sudo apt-get update
wget http://download.redis.io/releases/redis-2.8.12.tar.gz
tar xzf redis-2.8.12.tar.gz
cd redis-2.8.12
make
sudo apt-get install redis-server
sudo pip install redis   or   sudo easy_install redis
src/redis-server

#celery 安装
sudo pip install Celery



mysql字符转换utf8md4：http://my.oschina.net/leejun2005/blog/343353
http://it2048.cn/
#beanstalkc http://network.51cto.com/art/201503/469834_2.htm
#python class
http://pan.baidu.com/share/link?shareid=118708637&uk=120588894#path=%252FPython  password:298i
#nigix
http://freeloda.blog.51cto.com/2033581/1288553
http://f.dataguru.cn/thread-218822-1-1.html



