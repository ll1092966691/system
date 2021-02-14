# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime

class AcademicPaper(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, related_name='user_id')
    filename = models.CharField(max_length=50)
    academic_filename = models.CharField(max_length=50)
    academic_type = models.CharField(max_length=20)
    rank = models.CharField(max_length=10, blank=True, null=True)
    corresponding_author = models.CharField(max_length=8, blank=True, null=True)
    publication_name = models.CharField(max_length=50)
    inclusion_search = models.CharField(max_length=50, blank=True, null=True)
    issuing_time = models.DateField()
    doi_number = models.CharField(db_column='DOI_number', max_length=20, blank=True,null=True)  # Field name made lowercase.
    cited = models.IntegerField(blank=True, null=True)
    keywords = models.CharField(max_length=30, blank=True, null=True)
    start_end_page = models.CharField(max_length=20, blank=True, null=True)
    impact_factor = models.FloatField(blank=True, null=True)
    way = models.CharField(max_length=10, blank=True, null=True)
    related_topics = models.CharField(max_length=40, blank=True, null=True)
    author_ship = models.CharField(max_length=20, blank=True, null=True)
    together_fo_one = models.CharField(max_length=8, blank=True, null=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    synchronous_results = models.CharField(max_length=10, blank=True, null=True)
    volume = models.CharField(max_length=200, blank=True, null=True)
    issn_number = models.CharField(max_length=20, blank=True, null=True)
    cn_number = models.CharField(max_length=20, blank=True, null=True)
    note = models.CharField(max_length=50, blank=True, null=True)
    chinese_name = models.CharField(max_length=20, blank=True, null=True)
    internationaljcrpartition = models.CharField(db_column='InternationalJCRPartition', max_length=10, blank=True, null=True)  # Field name made lowercase.
    csciencejcrpartition = models.CharField(db_column='CScienceJCRPartition', max_length=10, blank=True, null=True)  # Field name made lowercase.
    wos = models.CharField(db_column='WOS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    esi = models.CharField(db_column='ESI', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:

        db_table = 'academic_paper'


class Book(models.Model):
    # user_id = models.IntegerField()
    user_book = models.ForeignKey('User', models.DO_NOTHING, related_name='user_book_id')
    filename = models.CharField(max_length=40)
    book_name = models.CharField(max_length=40)
    publication_number = models.CharField(max_length=20, blank=True, null=True)
    identity = models.CharField(max_length=10)
    rank = models.CharField(max_length=10)
    publisher = models.CharField(max_length=20)
    book_type = models.CharField(max_length=15, blank=True, null=True)
    published_date = models.CharField(max_length=15)
    note = models.CharField(max_length=50, blank=True, null=True)
    related_topics = models.CharField(max_length=30, blank=True, null=True)
    sort = models.CharField(max_length=10, blank=True, null=True)
    chinese_name = models.CharField(max_length=10)
    author_ship = models.CharField(max_length=15, blank=True, null=True)
    company_name = models.CharField(max_length=20, blank=True, null=True)
    synchronous_results = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class EducationMaterials(models.Model):
    user_id = models.IntegerField()
    filename = models.CharField(max_length=40)
    material_title = models.CharField(max_length=40)
    training_unit = models.CharField(max_length=20)
    lesson = models.CharField(max_length=5)
    rating_grade = models.CharField(max_length=10, blank=True, null=True)
    get_time = models.CharField(max_length=15)
    note = models.CharField(max_length=50, blank=True, null=True)
    related_topics = models.CharField(max_length=30, blank=True, null=True)
    synchronous_results = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'education_materials'


class FilehandleUserinfo(models.Model):
    useraccount = models.CharField(unique=True, max_length=24)  # Field name made lowercase.
    userpassword = models.CharField(max_length=24)  # Field name made lowercase.
    createtime = models.CharField( max_length=24)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fileHandle_userinfo'


class FileInformation(models.Model):
    user_id = models.IntegerField()
    filename = models.CharField(max_length=40)
    file_title = models.CharField(max_length=40)
    certificate_type = models.CharField(max_length=10, blank=True, null=True)
    get_time = models.CharField(max_length=15)
    certificateno = models.CharField(db_column='certificateNO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    granting_authority = models.CharField(max_length=20, blank=True, null=True)
    note = models.CharField(max_length=50, blank=True, null=True)
    related_topics = models.CharField(max_length=30, blank=True, null=True)
    synchronous_results = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_information'


class HorizontalTopics(models.Model):
    # user_id = models.IntegerField()
    user_HorizontalTopics = models.ForeignKey('User', models.DO_NOTHING, related_name='user_HorizontalTopics_id')
    filename = models.CharField(max_length=40)
    issue_name = models.CharField(max_length=40)
    contract_source = models.CharField(max_length=20)
    contract_number = models.CharField(max_length=15, blank=True, null=True)
    rank = models.CharField(max_length=10)
    money = models.CharField(max_length=10)
    starting_time = models.CharField(max_length=15)
    end_time = models.CharField(max_length=15, blank=True, null=True)
    issue_status = models.CharField(max_length=30, blank=True, null=True)
    note = models.CharField(max_length=50, blank=True, null=True)
    sort = models.CharField(max_length=10, blank=True, null=True)
    chinese_name = models.CharField(max_length=10)
    author_ship = models.CharField(max_length=15, blank=True, null=True)
    company_name = models.CharField(max_length=20, blank=True, null=True)
    synchronous_results = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horizontal_topics'


class LongitudinalIssues(models.Model):
    # user_id = models.IntegerField()
    user_LongitudinalIssues = models.ForeignKey('User', models.DO_NOTHING, related_name='user_LongitudinalIssues_id')
    filename = models.CharField(max_length=50)
    issuename = models.CharField(max_length=50)
    fundname = models.CharField(max_length=30)
    issue_type = models.CharField(max_length=20, blank=True, null=True)
    granting_unit = models.CharField(max_length=20, blank=True, null=True)
    issue_level = models.CharField(max_length=15, blank=True, null=True)
    issue_number = models.CharField(max_length=10, blank=True, null=True)
    money = models.FloatField(blank=True, null=True)
    rank = models.CharField(max_length=10)
    starting_time = models.CharField(max_length=15)
    end_time = models.CharField(max_length=15)
    issue_status = models.CharField(max_length=10, blank=True, null=True)
    note = models.CharField(max_length=50, blank=True, null=True)
    sort = models.CharField(max_length=10, blank=True, null=True)
    chinese_name = models.CharField(max_length=20)
    author_ship = models.CharField(max_length=15, blank=True, null=True)
    company_name = models.CharField(max_length=30, blank=True, null=True)
    synchronous_results = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'longitudinal_issues'


class NewsReport(models.Model):
    user_id = models.IntegerField()
    filename = models.CharField(max_length=40)
    news_name = models.CharField(max_length=40)
    media_name = models.CharField(max_length=20)
    media_level = models.CharField(max_length=15)
    reports_time = models.CharField(max_length=15)
    column_layout = models.CharField(max_length=15, blank=True, null=True)
    link = models.CharField(max_length=30, blank=True, null=True)
    note = models.CharField(max_length=50, blank=True, null=True)
    related_topics = models.CharField(max_length=30, blank=True, null=True)
    synchronous_results = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news_report'


class Other(models.Model):
    # user_id = models.IntegerField()
    user_other = models.ForeignKey('User', models.DO_NOTHING, related_name='user_other_id')
    filename = models.CharField(max_length=40)
    achievement_name = models.CharField(max_length=40)
    rank = models.CharField(max_length=10)
    get_time = models.CharField(max_length=15)
    note = models.CharField(max_length=50, blank=True, null=True)
    related_topics = models.CharField(max_length=30, blank=True, null=True)
    sort = models.CharField(max_length=10, blank=True, null=True)
    chinese_name = models.CharField(max_length=10)
    author_ship = models.CharField(max_length=15, blank=True, null=True)
    company_name = models.CharField(max_length=20, blank=True, null=True)
    synchronous_results = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other'


class Patent(models.Model):
    user_patent = models.ForeignKey('User', models.DO_NOTHING, related_name='user_patent_id')
    filename = models.CharField(max_length=40)
    patent_name = models.CharField(max_length=40)
    patent_type = models.CharField(max_length=15)
    patent_status = models.CharField(max_length=15)
    patent_no = models.CharField(db_column='patent_NO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    get_time = models.CharField(max_length=15, blank=True, null=True)
    apply_no = models.CharField(db_column='apply_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apply_time = models.CharField(max_length=15, blank=True, null=True)
    rank = models.CharField(max_length=10)
    note = models.CharField(max_length=50, blank=True, null=True)
    related_topics = models.CharField(max_length=30, blank=True, null=True)
    sort = models.CharField(max_length=10, blank=True, null=True)
    chinese_name = models.CharField(max_length=10)
    author_ship = models.CharField(max_length=15, blank=True, null=True)
    company_name = models.CharField(max_length=20, blank=True, null=True)
    synchronous_results = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patent'

class PersonalAwards(models.Model):
    # user_id = models.IntegerField()
    user_PersonalAwards = models.ForeignKey('User', models.DO_NOTHING, related_name='user_PersonalAwards_id')
    filename = models.CharField(max_length=40)
    honor_name = models.CharField(max_length=40)
    rank = models.CharField(max_length=10)
    awards = models.CharField(max_length=15, blank=True, null=True)
    level = models.CharField(max_length=15)
    granting_unit = models.CharField(max_length=20)
    award_time = models.CharField(max_length=15)
    note = models.CharField(max_length=50, blank=True, null=True)
    related_topics = models.CharField(max_length=30, blank=True, null=True)
    sort = models.CharField(max_length=10, blank=True, null=True)
    chinese_name = models.CharField(max_length=10)
    author_ship = models.CharField(max_length=15, blank=True, null=True)
    company_name = models.CharField(max_length=20, blank=True, null=True)
    synchronous_results = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_awards'


class SoftwareCopyright(models.Model):
    # user_id = models.IntegerField()
    user_SoftwareCopyright = models.ForeignKey('User', models.DO_NOTHING, related_name='user_SoftwareCopyright_id')
    filename = models.CharField(max_length=50)

    copyright_name = models.CharField(max_length=50)
    certificate_no = models.CharField(db_column='certificate_No', max_length=20)  # Field name made lowercase.
    rank = models.CharField(max_length=10)
    completion_time = models.CharField(max_length=15, blank=True, null=True)
    get_time = models.CharField(max_length=15)
    copyright_type = models.CharField(max_length=15)
    copyright_people = models.CharField(max_length=20)
    related_topics = models.CharField(max_length=30, blank=True, null=True)
    sort = models.CharField(max_length=10, blank=True, null=True)
    chinese_name = models.CharField(max_length=15)
    author_ship = models.CharField(max_length=15, blank=True, null=True)
    company_name = models.CharField(max_length=30, blank=True, null=True)
    synchronous_results = models.CharField(max_length=15, blank=True, null=True)
    note = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'software_copyright'


class StudentAwards(models.Model):
    # user_id = models.IntegerField()
    user_StudentAwards = models.ForeignKey('User', models.DO_NOTHING, related_name='user_StudentAwards_id')
    filename = models.CharField(max_length=40)
    game_name = models.CharField(max_length=40)
    awards_student = models.CharField(max_length=20)
    rank = models.CharField(max_length=10)
    awards = models.CharField(max_length=15)
    level = models.CharField(max_length=15)
    granting_unit = models.CharField(max_length=20)
    award_time = models.CharField(max_length=15)
    note = models.CharField(max_length=50, blank=True, null=True)
    related_topics = models.CharField(max_length=30, blank=True, null=True)
    sort = models.CharField(max_length=10, blank=True, null=True)
    chinese_name = models.CharField(max_length=10)
    author_ship = models.CharField(max_length=15, blank=True, null=True)
    company_name = models.CharField(max_length=20, blank=True, null=True)
    synchronous_results = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_awards'


class UploadFile(models.Model):
    filename = models.CharField(db_column='fileName', max_length=252)  # Field name made lowercase.
    filemd5 = models.CharField(db_column='fileMd5', max_length=128)  # Field name made lowercase.
    filetype = models.CharField(db_column='fileType', max_length=32)  # Field name made lowercase.
    filesize = models.IntegerField(db_column='fileSize')  # Field name made lowercase.
    filepath = models.CharField(db_column='filePath', max_length=128)  # Field name made lowercase.
    filecreated = models.CharField(db_column='fileCreated', default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), max_length=64)  # Field name made lowercase.
    fileupdate = models.CharField(db_column='fileUpdate',default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uploadfile'

class User(models.Model):
    phone = models.CharField(max_length=11, blank=True, null=True)
    password = models.CharField(max_length=20)
    grade = models.IntegerField()
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20, blank=True, null=True)
    academicpaper = models.IntegerField(db_column='academicPaper', blank=True, null=True, default=0)  # Field name made lowercase.
    longitudinalissues = models.IntegerField(db_column='longitudinalIssues', blank=True, null=True, default=0)  # Field name made lowercase.
    softwarecopyright = models.IntegerField(db_column='softwareCopyright', blank=True, null=True, default=0)  # Field name made lowercase.
    patent = models.IntegerField(blank=True, null=True, default=0)
    personalawards = models.IntegerField(db_column='personalAwards', blank=True, null=True, default=0)  # Field name made lowercase.
    studentawards = models.IntegerField(db_column='studentAwards', blank=True, null=True, default=0)  # Field name made lowercase.
    continuingeducationmaterials = models.IntegerField(db_column='continuingEducationMaterials', blank=True, null=True, default=0)  # Field name made lowercase.
    book = models.IntegerField(blank=True, null=True, default=0)
    horizontaltopics = models.IntegerField(db_column='horizontalTopics', blank=True, null=True, default=0)  # Field name made lowercase.
    newsreport = models.IntegerField(db_column='newsReport', blank=True, null=True, default=0)  # Field name made lowercase.
    fileinformation = models.IntegerField(db_column='fileInformation', blank=True, null=True, default=0)  # Field name made lowercase.
    other = models.IntegerField(blank=True, null=True, default=0)
    class Meta:
        managed = False
        db_table = 'user'
