hotelbooksystem
==================

基于Django的python信息管理系统，用于酒店预订管理

#环境

Python: 2.7.12

Django:1.10

MySQL:5.1.73

------


#Usage:
1. 克隆项目：
```
git clone git@github.com:williezh/kcsj
```
2. 进入文件夹：
```
cd kcsj
```
3. 建立虚拟环境：
```
virtualenv --python=python2 venv
```
4. 激活虚拟环境：
```
source venv/bin/activate
```
5. 安装必需包（首次运行）：
```
pip install -r requiredments.txt
```
6. 初始化数据库（首次运行）：
```
source migrate.sh
```
7. 运行服务：
```
python manage.py runserver
```
8. 打开如下网址即可看到运行效果：
```
http://127.0.0.1:8000/
```

