from django.shortcuts import render
from django.http import HttpResponse


def testing(self):
    return HttpResponse("""<H2>Welcome to Guide, Some endpoints
    </br>admin name:admin, password:123456</br>
                        admin/ --populate data in download infos  to see the effect when caling stats api
                        </br>
                        --media infos consists of media details, primary key is name
                        </br>
                        </br>
                        auth/ -- ------
                        </br>
                        http://127.0.0.1:8000/auth/nope/
                        </br>
http://127.0.0.1:8000/auth/users/   --create users
</br>
http://127.0.0.1:8000/auth/token/login/    --use this endpoint for user authetication token
</br>
http://127.0.0.1:8000/auth/users/login/    --to login
</br>
http://127.0.0.1:8000/auth/token/logout/    --logout
</br>
http://127.0.0.1:8000/auth/users/logout/  
</br></br>
                        
                        </br>
                        media/ --
                        </br>
                        MediaInfoViewSet/pk , where pk is song name, it's a get api for media details, from here media file will be downloaded example MediaInfoViewSet/song1
                        </br></br></br>
                        download/   -----</br>
                        urlpatterns = [
    path('', testing),</br>
    path('DownloadListPost', DownloadListPost.as_view()), post request to post user download info in db</br>
    path('DownloadListShow', DownloadListShow.as_view()), get request to get data of logged in user</br>
 This data will be used for calculating montly and daily downloads of user</br>
 by summing the media_size, and favourite media etc will also be found using this.</br>

]
</br></br>
                       -------
                       Authorization is commented, simply uncomment permission_classes to start permission.
                       Verified uisng admin.
</br>
                       Make sure to logout admin when checking for permissions.

        </H2>
                        """)
