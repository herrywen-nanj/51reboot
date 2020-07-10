# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-07-01 16:57'


def help():
    help_info = '''
            帮助信息:
            有效字段依次顺序: 'username', 'age', 'tel', 'email'
            增加:  add monkey 12 13200000001 monkey@51reboot.com
            删除: 
               - delete monkey 
               - delete 1 
            修改: 
               - update monkey set age = 18
               - update monkey set tel = 13200000002
               - update monkey set email = xxx@51reboot.com
            列出: list
            查找: find monkey (用户名模糊查询)
            分页： 
                - display page 2 pagesize 5
                - display page 2
            导出: export
            退出: exit
            '''
    return help_info