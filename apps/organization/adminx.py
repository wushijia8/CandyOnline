# _*_ encoding:utf-8 _*_
import xadmin

from .models import CityDict, CurseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_num', 'fav_num']
    search_fields = ['name', 'desc', 'click_num', 'fav_num']
    list_filter = ['name', 'desc', 'click_num', 'fav_num']
    relfield_style = 'fk-ajax'


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org', 'name', 'work_years', 'work_company']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CurseOrg, CityDictAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
