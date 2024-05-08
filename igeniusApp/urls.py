from django.urls import path
from igeniusApp import views

urlpatterns = [

    # <<<<<<< Website Url >>>>>>>>
    # path('',views.demo),
    path('',views.homepage,name='homepage'),
    path('course/',views.course,name='course'),
    path('abacus/',views.abacus,name='abacus'),
    path('achivephotos/',views.achive_photos,name='achivephotos'),
    path('achivevideo/',views.achive_video,name='achivevideo'),
    path('award/',views.award,name='award'),
    path('news/',views.news,name='news'),
    path('career/',views.career,name='career'),
    path('contact-us/',views.contact_us,name='contact-us'),
    path('about-us/',views.about_us,name='about_us'),
    path('franchise/',views.franchise,name='franchise'),
    path('blog/',views.blog,name='blog'),
    path('find-us/',views.find_us,name='find_us'),
    path('our-team/',views.our_team,name='our_team'),
    
    # Social Media Link URL
    path('whatsapp-chat/', views.whatsapp_chat, name='whatsapp_chat'),
    path('instagram/',views.instagram,name='instagram'),
    path('facebook/',views.facebook,name='facebook'),
    path('youtube/',views.youtube,name='youtube'),

    # <<<<<<< Dashboard Url >>>>>>>>

    path('master/',views.card,name='card'),


]
