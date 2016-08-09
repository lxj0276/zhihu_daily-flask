# 知乎日报网页版

基于Flask的知乎日报网页版，思路和大部分代码来源于[JobsDong/zhihudaily](https://github.com/JobsDong/zhihudaily)

## 项目结构

        ├── app
        │   ├── crawl               知乎日报API
        │   ├── fetch.py            插入数据
        │   ├── main                视图函数
        │   ├── models.py           ORM定义
        │   ├── static              静态资源
        │   └── templates           模板
        ├── config.py               项目配置
        ├── manage.py               管理脚本
        ├── migrations              数据库迁移 -- Flask-Migrate
        ├── README.md               项目介绍
        ├── requirements.txt        项目依赖

## 实现说明


## 安装与运行

* 依赖安装

        pip install -r requirements.txt

* 数据库初始化

        python manage.py db init

* 数据抓取

        python manage.py fetch

* 运行

        python manage.py runserver
