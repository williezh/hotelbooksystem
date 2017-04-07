#coding=utf-8
from __future__ import absolute_import, unicode_literals
# https://github.com/qiniu/python-sdk/blob/master/qiniu/services/storage/uploader.py
# https://developer.qiniu.com/kodo/sdk/python
from qiniu import Auth,put_file,put_data,BucketManager
from .utils import QiniuError, bucket_lister
from os.path import basename,splitext
from datetime import datetime
  
class QiniuStorage(object):
    '''
    七牛云的文件上传、显示、删除
    @auth:ZWJ
    '''
    def __init__(self,access_key,secret_key,bucket_name,bucket_domain):
        """                                      
        @para:            
            access_key:公钥    
            secret_key:私钥                 
            bucket_name: 要上传的空间
            bucket_domain:获取文件url路径时对应的私有域名
        """ 
        self.auth=Auth(access_key,secret_key)
        self.bucket_name = bucket_name
        self.bucket_domain = bucket_domain
        self.bucket_manager = BucketManager(self.auth)
    
    def put_data(self,name,data):
        """
        @def:put_data
        @def_fun: 文件流上传
            空间里的文件名不能重复，所以用_newname生成新文件名                                  
        @para:            
            name: 文件名   
            data: 上传二进制流                      
        @ret:上传后的url路径        
        """               
        #上传到七牛后保存的文件名
        key = self._newname(name)  
        #生成上传 Token，可以指定过期时间等
        token=self.auth.upload_token(self.bucket_name,key) 
        if hasattr(data,'chunks'):
            data = b''.join(c for c in data.chunks())
        ret, info = put_data(token, key, data)  #上传文件流到七牛
        if ret is None or ret['key'] != key:
            raise QiniuError(info)
        return self.get_url(key)
        
    def _newname(self,name):
        '''加上6位日期和6位时间标识 PG.jpg --> PG_170211_044217.jpg '''
        root,ext=splitext(basename(name))
        time=datetime.now().strftime('_%y%m%d_%H%M%S')
        return '{}{}{}'.format(root,time,ext)

    def get_url(self,key): 
        '''        
        @def:get_url
        @def_fun: 返回七牛云上文件名为key的文件对应的url地址
           如果是公有空间，该地址可以直接访问文件；私有空间则需用private_download_url                                  
        @para:            
            key: 七牛云上的文件名                                    
        @ret:域名加文件名生成的url路径
        '''   
        url='http://{}/{}'.format(self.bucket_domain,key)
        return url 

    def private_download_url(self,url,expires=7200):
        """
        @def:private_download_url
        @def_fun: 生成私有资源下载链接                                       
        @para:            
            url: 私有空间资源的原始URL   
            expires: 下载凭证有效期，默认为7200s                     
        @ret:私有资源的下载链接        
        """               
        return self.auth.private_download_url(url,expires)
                    
    def put_file(self,filePath):
        """
        @def:put_file
        @def_fun: 本地文件上传
            空间里的文件名不能重复，所以用_newname生成新文件名                                  
        @para:            
            filePath: 待上传文件在磁盘中的绝对路径                              
        @ret:上传后的url路径        
        """
        key = self._newname(filePath)  
        token=self.auth.upload_token(self.bucket_name,key) 
        ret, info = put_file(token, key, filePath)  
        if ret is None or ret['key'] != key:
            raise QiniuError(info)
        return self.get_url(key)
    
    def exists(self,key):        
        '''检测七牛云上是否有文件名为key的文件'''
        bucket=self.bucket_manager
        ret, info = bucket.stat(self.bucket_name, key.split('/')[-1])
        return ret is not None  

    def delete(self,key):  
        '''删除七牛云上文件名为key的文件'''
        if not self.exists(key):
            return '{} not exist in qiniu_cloud'.format(key)  
        bm=self.bucket_manager
        ret, info = bm.delete(self.bucket_name, key.split('/')[-1])
        if ret == {}:
            return 'success to delete {} in qiniu_cloud'.format(key)
        else:
            return info    

    def ls_files(self,prefix="", limit=None):
        """
        @def:ls_file
        @def_fun: 显示七牛云上的文件名
        具体规格参考:
        http://developer.qiniu.com/docs/v6/api/reference/rs/list.html                                   
        @para:            
            prefix:     列举前缀            
            limit:      单次列举个数限制                            
        @ret:  文件名组成的set()集合    
        """  
        files=set() 
        dirlist = bucket_lister(self.bucket_manager, self.bucket_name,
                                prefix,limit) 
        for item in dirlist:
            files.add(item['key'])        
        return files
                 

