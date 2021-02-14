# 作者    ：LL
# 时间    ：2020/8/1 20:15
# 文件    ：tools.py
import hashlib
import os
import random
import re
import time

from PIL import Image
from django.conf import settings


# 计算文件的md5
def GetFileMd5(file):
    md5Obj = hashlib.md5()
    for chunk in file.chunks():
        md5Obj.update(chunk)
    return md5Obj.hexdigest()


# 文件重命名及写入
def Rename(file, file_or_img, filename):
    times = time.strftime('%Y%m%d%H%M%S')
    times_ymd = time.strftime('%Y-%m-%d')
    ran = random.randint(0, 1000)
    ext = os.path.splitext(file.name)[1]
    if file_or_img == 'files':
        # newFile = "{}{}{}".format(filename, ran, ext)
        newFile = filename+ext
    else:
        newFile = "{}{}{}".format(times, ran, ext)
    file_path = "/{}/{}/".format(file_or_img, times_ymd)
    print(file_path)
    path = os.path.join(settings.MEDIA_ROOT + file_path, newFile).replace('\\', '/')
    path_url = settings.MEDIA_URL + file_path + newFile
    print('rename path', path)
    try:
        with open(path, mode='wb+') as ff:
            for chunk in file.chunks():
                ff.write(chunk)
    except FileNotFoundError:
        os.makedirs("media" + file_path)
        with open(path, mode='wb+') as ff:
            for chunk in file.chunks():
                ff.write(chunk)
        print("文件创建成功！")
    return path_url


# 检测文件类型
def JudgeType(ext):
    ImageType = [".png", ".jpeg", ".jpg", ".gif", ".bmp"]
    if ext in ImageType:
        return True
    return Falsedef

def JudgeFileType(ext):
    fileType = [".txt", ".doc", ".docx", ".xls", ".xlsx", ".pdf", ".ppt", ".pptx"]
    if ext in fileType:
        return True
    return False, ext

# 限制图片大小
def imageSize(image):
    image_size = image.size
    limit = 100 * 1024  # 100k
    if image_size < limit:
        return True
    else:
        compress_image(image)
    return False

def compress_image(infile, outfile='', mb=100, step=10, quality=80):
    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
    o_size = infile.size/1024
    if o_size <= mb:
        return infile
    outfile = get_outfile(infile, outfile)
    while o_size > mb:
        im = Image.open(infile)
        im.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = get_size(outfile)

    return outfile, get_size(outfile)

# 限制文件大小
def FileSize(size):
    limit = 5 * 1024 * 1024  # 5M
    if size < limit:
        return True
    else:
        pass
    return False
