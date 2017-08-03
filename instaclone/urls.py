from myapp.views import signup_view
from myapp.views import login_view
from myapp.views import feed_view
from myapp.views import post_view
from myapp.views import like_view
from myapp.views import comment_view

urlpatterns = [url('comment/', comment_view),
               url('like/', like_view),
               url('post/', post_view),
               url('feed/',feed_view),
               url('login/',login_view),
               url('', signup_view)]