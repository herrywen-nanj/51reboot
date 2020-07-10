from django import template
register = template.Library()

@register.filter(name = 'orderfile_name')
def orderfile_name(file_path):
    """
    截取上传文件的文件名
    上传文件数据库中存放的格式：gndenfiles/2019/86/aa.txt
    最终需要的格式：aa.txt
    :return: 文件名
    """
    file_name = str(file_path).split('/')[-1]
    return file_name