#coding=utf-8
from django.conf import settings
from .qiniustorage import QiniuStorage
from time import sleep
    
class QiniuPush(QiniuStorage):
    '''
    根据settings中的QINIU_CONF配置七牛云的密钥、空间、域名等
    直接调用该类的类方法即可进行文件上传、显示、删除
    各方法的详细介绍见父类QiniuStorage
    @auth:ZWJ
    '''
    def __init__(self):
        super(QiniuPush,self).__init__(**settings.QINIU_CONF)
            
    @classmethod
    def put_data(cls,name,data):
        '''
        上传内存中的文件流到七牛并返回上传后的url地址
        example:
            f=request.FILES['photo']
            u.headImg=QiniuPush.put_data(f.name, f)
            u.save() #保存到数据库
            -----------------
            #another def 
            uuu = User.objects.get(username=request.session['user_name'])
            uuu.headImg=QiniuPush.private_download_url(uuu.headImg) #生成 
            return render(request, 'account/signup_result.html', {'user': uuu})
        '''
        qn=cls()
        return super(QiniuPush,qn).put_data(name,data)

    @classmethod
    def private_download_url(cls,url,expires=7200):
        '''生成私有资源下载链接'''
        qn=cls()
        return super(QiniuPush,qn).private_download_url(url,expires)
        
    @classmethod            
    def put_file(cls,filePath):
        '''上传本地文件到七牛并返回上传后的url地址'''
        qn=cls()
        return super(QiniuPush,qn).put_file(filePath)
        
    @classmethod
    def exists(cls,key):        
        '''检测七牛云上是否有文件名为key的文件'''
        qn=cls()
        return super(QiniuPush,qn).exists(key)  

    @classmethod
    def get_url(cls,key): 
        '''返回七牛云上文件名为key的文件对应的url地址'''   
        qn=cls()
        return super(QiniuPush,qn).get_url(key)
                
    @classmethod
    def delete(cls,key):  
        '''删除七牛云上文件名为key的文件'''
        qn=cls()
        return super(QiniuPush,qn).delete(key) 
          
    @classmethod
    def ls_files(cls,prefix="", limit=100):
        '''列出七牛云上的文件(前100个)'''
        qn=cls()
        return super(QiniuPush,qn).ls_files()
                 
def main():    
    '''
    用于本地测试：
    不能直接python backend.py
    需在上一级目录python manage.py shell
    ...
    from qiniuyun import backend as ba
    ba.main()
    '''
    for i,f in enumerate(QiniuPush.ls_files(),1):
        print(i,'、',f)
    filePath='/home/willie/Downloads/PG.jpg'
    url=QiniuPush.put_file(filePath) 
    sleep(1)
    with open(filePath,'rb') as f:
        url2=QiniuPush.put_data(filePath,f.read())
        #or: url2=QiniuPush.put_data(filePath.split('/')[-1],f.read())
    print(url,'\n',QiniuPush.private_download_url(url2,expires=7200))
    sleep(3)    
    assert QiniuPush.exists(url)
    for i,f in enumerate(QiniuPush.ls_files(),1):
        print(i,'、',f)
    print(QiniuPush.delete(url))
    assert QiniuPush.exists(url)==False
    assert QiniuPush.delete(url)=='{} not exist in qiniu_cloud'.format(url)
    for i,f in enumerate(QiniuPush.ls_files(),1):
        print(i,'、',f)
 
if __name__=='__main__':
    main()    
