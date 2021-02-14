from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from fileHandle import models
from datetime import datetime
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from fileHandle import tools
from django.conf import settings
from django.core import serializers
import os
import PyPDF2
import json


def login(request):
    """登录验证"""
    global response
    user_account = request.POST.get('user_account')
    user_password = request.POST.get('user_password')
    print(user_account, user_password)
    response_dit = {"code": "400", "status": "fail"}

    if request.method == "POST":
        obj = models.User.objects.values().filter(phone=user_account).first()
        print(obj)
        if obj and obj['password'] == user_password:
            response_dit['code'] = 200
            response_dit['status'] = "success"
            response = JsonResponse(response_dit)
            response.set_cookie('user', user_account)
        else:
            response_dit['code'] = 400
            response_dit['status'] = "fail"
            response = JsonResponse(response_dit)
    return response


def register(request):
    """注册账号"""
    user_account = request.POST.get('user_account')
    user_password = request.POST.get('user_password')
    response_dit = {"code": "400", "status": "fail"}
    if request.method == "POST":
        obj = models.User.objects.values().filter(phone=user_account).first()
        if not obj:
            dict = {'phone': user_account, 'password': user_password, 'grade': 1}
            models.User.objects.create(**dict)
            response_dit['code'] = 200
            response_dit['status'] = "success"
            response_dit['msg'] = "用户创建成功"
        else:
            response_dit['msg'] = "用户已存在"
    return JsonResponse(response_dit)


def getfile(request):
    """获取用户材料信息"""
    if request.method == 'GET':
        user_account = request.GET.get('user')
        print(user_account)
        obj = models.User.objects.values().filter(phone=user_account).first()
        print(obj)
        # res = serializers.serialize('json', obj)
        # print(res)
        return JsonResponse(obj, safe=False)
    if request.method == 'POST':
        file_type = request.POST.get('file_type')
        user_account = request.POST.get('user')
        print('POST', file_type, user_account)
        obj = models.User.objects.filter(phone=user_account).first()
        print(obj)
        models_list = [obj.user_id, obj.user_SoftwareCopyright_id, obj.user_patent_id, obj.user_PersonalAwards_id,
                       obj.user_StudentAwards_id, obj.user_book_id.all(), obj.user_other_id, obj.user_HorizontalTopics_id,
                       obj.user_LongitudinalIssues_id]
        res = serializers.serialize('json', models_list[int(file_type) - 1].all())

        print(res)
        return HttpResponse(res)


def deleteFile(request):
    """删除用户文件"""
    if request.method == 'POST':
        pk = request.POST.get('pk')
        file_type = int(request.POST.get('file_type'))
        user = request.POST.get('user')
        response = {'msg': 'fail'}

        models_list = [models.AcademicPaper, models.SoftwareCopyright, models.Patent,
                       models.PersonalAwards, models.StudentAwards, models.Book, models.Other,
                       models.HorizontalTopics, models.LongitudinalIssues]
        ziduan_list = ['academicpaper', 'softwarecopyright', 'patent', 'personalawards', 'studentawards',
                       'book', 'other', 'horizontaltopics', 'longitudinalissues']

        res = models_list[file_type].objects.filter(id=pk).delete()
        if res[0]:
            response['msg'] = 'success'
            count = models.User.objects.values(ziduan_list[file_type]).filter(phone=user).first()
            update_dict = {ziduan_list[file_type]: count[ziduan_list[file_type]] - 1}
            models.User.objects.filter(phone=user).update(**update_dict)
            print('删除成功')
        return JsonResponse(response, safe=False)


def addFile(request):
    """添加用户文件数据"""
    if request.method == 'POST':
        file_list = json.loads(request.POST.get('file_list'))
        file_type = int(request.POST.get('file_type'))
        user = request.POST.get('user')
        pk = models.User.objects.values("id").filter(phone=user)
        print(file_type, user, end='')
        response1 = 'fail'
        ziduan_list = ['academicpaper', 'softwarecopyright', 'patent', 'personalawards', 'studentawards',
                       'book', 'other']

        models_list = [models.AcademicPaper, models.SoftwareCopyright, models.Patent,
                       models.PersonalAwards, models.StudentAwards, models.Book, models.Other,
                       models.HorizontalTopics]

        id_list = ['user_id', 'user_SoftwareCopyright_id', 'user_patent_id', 'user_PersonalAwards_id', '',
                   'user_book_id', 'user_other_id']

        file_list[id_list[file_type - 1]] = pk
        author_info = file_list['data4'][0]
        file_list.update({'chinese_name': author_info.pop('name'), 'company_name': author_info.pop('text'),
                          'author_ship': author_info.pop('identity')})
        print(file_list['data4'], author_info)
        # models_list[int(file_type) - 1].objects.create(**author_info)
        del file_list['data4']
        print(file_list)
        obj = models_list[file_type - 1].objects.create(**file_list)

        if obj:
            response1 = 'success'
            count = models.User.objects.values(ziduan_list[file_type - 1]).filter(phone=user).first()
            update_dict = {ziduan_list[file_type - 1]: (count[ziduan_list[file_type - 1]] + 1)}

            obj1 = models.User.objects.filter(phone=user).update(**update_dict)
            print(update_dict, obj1)
            print('添加成功')
        return HttpResponse(response1)








def uploadFile(request):
    """上传文件，并保存"""
    global url, file_name
    file_list = request.FILES.getlist('files')

    fileUrl_list = []
    print('uploadFile', type(file_list), file_list)
    if file_list:
        for i in range(len(file_list)):
            file_name = os.path.splitext(file_list[i].name)[0]
            md5 = tools.GetFileMd5(file_list[i])
            fileObj = models.UploadFile.objects.filter(filemd5=md5)
            if not fileObj:
                size = file_list[i].size
                if not tools.FileSize(size):
                    info = {'code': 403, 'error': '文件太大!'}
                    return JsonResponse(info)
                ext = os.path.splitext(file_list[i].name)[1]
                if not tools.JudgeFileType(ext[:-1]):
                    info = {'code': 403, 'error': '文件类型错误！'}
                    return JsonResponse(info)
                path = tools.Rename(file_list[i], 'files', file_name)
                create = models.UploadFile.objects.create(filename=file_name, filemd5=md5, filetype=ext,
                                                          filesize=size, filepath=path)
                url = 'http://' + settings.HOST_NAME + "/" + create.filepath
                fileUrl_list.append({"file_name": file_name, "file_url": url})
            else:
                url = 'http://' + settings.HOST_NAME + "/" + fileObj.first().filepath
                fileUrl_list.append({"file_name": file_name, "file_url": url})
        print(fileUrl_list)
        # return JsonResponse({"file_name": file_name, "file_url": url}, json_dumps_params={'ensure_ascii': False})
        return JsonResponse(fileUrl_list, safe=False)


pdfmetrics.registerFont(TTFont("SimSun", "SimSun.ttf"))  # 注册字体
def file_merge(file_list):
    """文件合并成新的PDF"""
    fileNames = ['../file/17034520230 陆良 就业计划书.pdf', '../file/个人简历.pdf']
    merger = PyPDF2.PdfFileMerger()
    file_newName = '《新文件' + datetime.now().strftime("%Y%m%d%H%M%S")+'》'
    base_path = os.path.join(os.path.dirname(os.path.dirname(__file__))) + '/'
    catalog_list = []
    catalog_list_dict = {}
    response = {}
    page_number = 0
    for filename in file_list:
        reader = PyPDF2.PdfFileReader(open(settings.BASE_DIR + '/' + filename['file_url'], 'rb'))
        merger.append(PyPDF2.PdfFileReader(settings.BASE_DIR + '/' + filename['file_url']))

        # print(reader.isEncrypted)  # 判断是否有加密
        # file_newName += filename['file_name']
        catalog_list_dict['file_name'] = filename['file_name']
        page_number += reader.getNumPages()
        catalog_list_dict['page_number'] = page_number
        merger.addBookmark(filename['file_name'], page_number)

        catalog_list.append(catalog_list_dict.copy())
    print('file_merge', catalog_list)
    create_catalog(catalog_list)
    merger.merge(0, settings.BASE_DIR + '/' + "/file/text.pdf")
    merger.write(settings.BASE_DIR + '/' + '/file/{}.pdf'.format(file_newName))
    response['url'] = 'http://' + settings.HOST_NAME + '/file/{}.pdf'.format(file_newName)
    response['name'] = file_newName
    return response


def create_catalog(catalog_list):
    """生成PDF目录"""
    c = canvas.Canvas(os.path.join(os.path.dirname(__file__) + "/../file/text.pdf"))
    c.setFont(psfontname="SimSun", size=24)
    c.drawString(100, 700, "目录")
    c.setFont(psfontname="SimSun", size=12)
    for index, i in enumerate(catalog_list):
        lenTxt = len(i['file_name'])
        lenTxt_utf8 = len(i['file_name'].encode('utf-8'))
        size = int((lenTxt_utf8 - lenTxt) / 2 + lenTxt)
        c.drawString(100, (650 - index * 20), i['file_name'] + "." * (60 - size) + str(i['page_number']))
        c.drawString(300, 20, "--1--")
    c.showPage()
    c.save()

def upload_and_marge(request):
    """上传文件，并合成新的文件"""
    global name
    file_list = request.FILES.getlist('files')
    file_url = request.POST.get('file_url')
    print(file_url)
    fileUrl_list = []
    for i in json.loads(file_url):
        if i['model'] == 'fileHandle.academicpaper':
            name = 'academic_filename'
        elif i['model'] == "fileHandle.softwarecopyright":
            name = 'copyright_name'
        elif i['model'] == "fileHandle.softwarecopyright":
            name = 'copyright_name'
        elif i['model'] == "fileHandle.patent":
            name = 'patent_name'
        elif i['model'] == "fileHandle.personalawards":
            name = 'honor_name'
        elif i['model'] == "fileHandle.studentawards":
            name = 'game_name'
        elif i['model'] == "fileHandle.book":
            name = 'book_name'
        elif i['model'] == "fileHandle.other":
            name = 'achievement_name'

        fileUrl_list.append({"file_name": i['fields'][name], "file_url": i['fields']['filename']})

    print(fileUrl_list)
    file_marge_obj = file_merge(fileUrl_list)
    print('返回数据', file_marge_obj)
    return JsonResponse(file_marge_obj)

    # global url, file_name
    # fileUrl_list = []
    #
    # print('upload_and_marge', type(file_list), file_list)
    # if file_list:
    #     for i in range(len(file_list)):
    #         file_name = os.path.splitext(file_list[i].name)[0]
    #         md5 = tools.GetFileMd5(file_list[i])
    #         fileObj = models.uploadFile.objects.filter(fileMd5=md5)
    #         if not fileObj:
    #             size = file_list[i].size
    #             if not tools.FileSize(size):
    #                 info = {'code': 403, 'error': '文件太大!'}
    #                 return JsonResponse(info)
    #             ext = os.path.splitext(file_list[i].name)[1]
    #             print(ext)
    #             if not tools.JudgeFileType(ext[:-1]):
    #                 info = {'code': 403, 'error': '文件类型错误！'}
    #                 return JsonResponse(info)
    #             path = tools.Rename(file_list[i], 'files', file_name)
    #             create = models.uploadFile.objects.create(fileName=file_name, fileMd5=md5, fileType=ext,
    #                                                       fileSize=size, filePath=path)
    #             url = "../" + create.filePath
    #             fileUrl_list.append({"file_name": file_name, "file_url": url})
    #         else:
    #             url = "../" + fileObj.first().filePath
    #             fileUrl_list.append({"file_name": file_name, "file_url": url})
    # file_marge_obj = file_merge(fileUrl_list)
    # return HttpResponse(file_marge_obj)


def test(request):
    num = 1
    tmp = os.path.join(os.path.dirname(__file__) + "/../file/17034520230 陆良 就业计划书.pdf")
    c = canvas.Canvas(tmp)
    for i in range(0, 2):
        # c.drawString((210//2)*mm, (4)*mm, str(i), mode=0)
        c.drawString(2, 4, 'haha')
        c.beginText(100, 200, 'heihei')
        c.freeTextAnnotation('hihei', DA=1)

        c.showPage()
    c.save()
    # with open(tmp, 'a+') as f:
    #     pdf = PyPDF2.PdfFileReader(f)
    #     layer = pdf.getPage(0)
    # print(layer)
    from matplotlib.backends.backend_pdf import PdfPages
    pp = PdfPages(tmp)
    for n, fig in enumerate(figs):
        fig.text(4.25 / 8.5, 0.5 / 11., str(n + 1), ha='center', fontsize=8)
        pp.savefig(fig)
    pp.close()

    return HttpResponse('ok')
