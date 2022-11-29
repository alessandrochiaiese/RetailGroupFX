from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("about/", hello.views.about, name="about"),
    path("contact/", hello.views.contact, name="contact"),
    path("facts/", hello.views.facts, name="facts"),
    path("feature/", hello.views.feature, name="feature"),
    path("project/", hello.views.project, name="project"),
    path("service/", hello.views.service, name="service"),
    path("team/", hello.views.team, name="team"),
    path("terms/", hello.views.terms, name="terms"),
    path("testimonial/", hello.views.testimonial, name="testimonial"),
    path("404/", hello.views.error_404, name="error_404"),
    path("support/", hello.views.support, name="support"),
    #path("admin/", admin.site.urls),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()