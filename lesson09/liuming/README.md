```python
# 数据库连接地址需要修改, 默认如下
DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'devops',
        'HOST': '192.168.56.101',
        'USER': 'root',
        'PASSWORD': '123456',
        'PORT': 3306,
    }
}
```

```bash
# 用到了 django session 来做登陆认证，所以需要要迁移下数据模型
python3 manage.py makemigrations
python3 manage.py migrate
```

