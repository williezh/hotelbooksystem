# hotelbooksystem
----------------------

基于Django的python信息管理系统，用于酒店预订管理

<br />

# Base on

Python: 2.7/3.6

Django:1.10.6

MySQL

# Run at local:

1. 克隆项目：
```
git clone https://github.com/williezh/hotelbooksystem
```
2. 进入文件夹：
```
cd hotelbooksystem
```
3. 建立虚拟环境：
```
virtualenv --python=python2.7 venv
```
4. 激活虚拟环境：
```
source venv/bin/activate
```
5. 安装必需包（首次运行）：
```
pip install -r requirements.txt
```
6. 由local_settings_sample.py创建local_settings.py
```
cp kcsj/local_settings_sample.py kcsj/local_settings.py
```
7. 修改其中的配置（数据库、邮箱和七牛云)
```
vi kcsj/local_settings.py
```
8. 初始化数据库（首次运行）：
```
source migrate.sh
```
9. 创建管理员账户：
```
python manage.py createsuperuser
```
10. 登录管理员，然后再进入上传页面：

http://127.0.0.1:8000/admin

http://127.0.0.1:8000/upload

11. 上传图片到七牛云存储（七牛上需有local_settings.py中对应的私有空间）：
- 图片在static/pic 
- Name输入框需留空
- 一个个来并且全部上传

12. 运行服务：
```
python manage.py runserver
```
13. 打开如下网址即可看到运行效果：

http://127.0.0.1:8000/ 
