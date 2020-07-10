# GIT新版安装教程

说明为什么要安装？

答：因为在centos6环境中的GIT版本太老了，导致git clone 报错 <font color=#FF0000 > error: while accessing https://xx/xx </font>,所以要安装相对比较新的版本GIT;

## 卸载系统版本git

```shell
yum remove git
```

## 安装依赖包

```
yum install perl-ExtUtils-CBuilder perl-ExtUtils-MakeMaker  nss curl libcurl openssh
```

## 下载GIT

```shell
wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.9.4.tar.gz
```

## 安装配置GIT

```Shell
tar zxvf git-2.9.4.tar.gz
cd git-2.9.4
make prefix=/usr/local/git all
make prefix=/usr/local/git install
echo "export PATH=$PATH:/usr/local/git/bin" >> /etc/profile
source /etc/profile
#验证
git --version
```

## 初次使用Github说明

```shell
#可选，根据个人习惯
mkdir /xxx/homework/lesson01]()
cd  /xxx/homework/lesson01
```

```shell
#必须操作
git clone https://github.com/51reboot/xly1.git
cd xly1/lesson01
mkdir wuxinglai #student`s  name
echo "Good Good Study Python" >> wuxinglai/README.md #testfile
git add .
git config --global user.email "2646956688@qq.com"
git config --global user.name "wuxinglai"
git commit -m "First Commit Add My file:wuxinglai"
git push
```

## 再次使用github说明

```shell
cd xly1/lesson01
git pull 
```

我在web界面上创建了一个文件test,使用git pull 同步一下，如下信息

<font color=#008000 > [vagrant@localhost lesson01]$ git pull
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 5 (delta 2), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (5/5), done.
From https://github.com/51reboot/xly1
   7ccd18e..616a03b  master     -> origin/master
Updating 7ccd18e..616a03b
Fast-forward
 lesson01/wuxinglai/test | 1 +
 1 file changed, 1 insertion(+)</font>

所以避免文件冲入最好是显git pull,在进行新文件的提交

写好作业，然后进行以下操作

```shell
git add .
git commit -m "Add  9x9.py file"
git push
```

#返回信息如下
 git push                                                                                            

Username for 'https://github.com': wuxinglai66
Password for 'https://wuxinglai66@github.com': 
Counting objects: 5, done.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 555 bytes | 0 bytes/s, done.
Total 5 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/51reboot/xly1.git
   616a03b..eac4a1b  master -> master)

