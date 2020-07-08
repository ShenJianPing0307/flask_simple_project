from flask import Flask

# 将Flask进行实例化，传入响应的参数，其中static_url_path是静态文件地址路径
app = Flask(__name__,template_folder='templates',static_folder='statics',static_url_path='/static')

# 将所有的蓝图导入进来，相当于汇总
from .views.account import account
from .views.blogs import blogs

# 将所有的蓝图再注入到app中，这样进行同一，请求一旦进来，由app统一分发
app.register_blueprint(account) #不加前缀 http://127.0.0.1:5000/login
app.register_blueprint(blogs,url_prefix='/blogs') #可以加入前缀，http://127.0.0.1:5000/blogs/home