# 本次作业
1、九九乘法表
2、猜数字游戏

## 附： git使用

第一次使用
git clone https://github.com/51reboot/xly1.git
cd xly1/lesson01/
mkdir woniu
echo  print 123 >> woniu/zuoye.py
git add .
git config --global user.email "597004635@qq.com"
git config --global user.name "denghonglin"
git commit -m "first commit:joy:"
git pull								# 防止冲突,每次push之前先pull
git push

后面写好作业后，只需要下面三行即可
git add .
git commit -m "first commit"						# 引号内为本次提交的描述,请自行更改
git pull								# 防止冲突,每次push之前先pull
git push 
