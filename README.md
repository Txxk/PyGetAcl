PyGetAcl
========

python使用prettytable模块生成Linux下目录的ACL权限表格

1、依赖安装：pip install prettytable

2、获取权限getfacl -R /aaa > ${real_path}/aaa_per.list 
    
    注意1、如果要获取/data/bbb,需要cd /data/ && getfacl -R bbb/ > ${real_path}/bbb_per.list。不然不能正常获取权限。
      2、获取的权限文件bbb_per.list命名格式需要以_分割，生成的表格文件名字会是_符号前面的字符串加上.txt, 例如bbb.txt。
        
3、生成的.list文件名需要保存到per_file.txt内。可使用ls *.list > per_file.txt。

4、运行start_showtable.sh脚本即可生成权限表格
