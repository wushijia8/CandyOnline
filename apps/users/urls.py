# _*_ encoding:utf-8 _*_

from django.conf.urls import url
from .views import UserInfoView, UploadImageView, UserCourse, UpdatePwdView, UserMessage, SendEmailCodeView
from .views import UserFav, UserFavTeacher, UserFavOrg, UpdateEmailView


urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),
    url(r'^course/$', UserCourse.as_view(), name="user_course"),
    url(r'^fav/$', UserFav.as_view(), name="user_fav"),
    url(r'^teacher/$', UserFavTeacher.as_view(), name="user_teacher"),
    url(r'org/$', UserFavOrg.as_view(), name="user_org"),
    url(r'^message/$', UserMessage.as_view(), name="user_message"),
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

]
