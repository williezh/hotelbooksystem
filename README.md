# hotelbooksystem
----------------------

基于Django的python信息管理系统，用于酒店预订管理

<br />

 # Base on
============
Python: 2.7.12
Django:1.10
MySQL:5.1.73

# How to Run:
=============
1. 克隆项目：
```
git clone git@github.com:williezh/hotelbooksystem
```
2. 进入文件夹：
```
cd hotelbooksystem
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
6. 由local_settings_sample.py创建local_settings.py
```
cp kcsj/local_settings_sample.py kcsj/local_settings.py
```
7. 修改其中的数据库配置（'USER','PASSWORD')
```
vi kcsj/local_settings.py
```
8. 初始化数据库（首次运行）：
```
source migrate.sh
```
9. 运行服务：
```
python manage.py runserver
```
10. 打开如下网址即可看到运行效果：

http://127.0.0.1:8000/ 
