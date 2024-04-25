from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world</h1>'

@app.route('/hello')
def hello():
    return '<h1>hello</h1>'

posts = {
    1:"POST1",
    2:"POST2",
}

# string int float
# uuid UUID文字列　オブジェクトを一意に識別するための識別子
# 
# @app.route('/post/<int:post_id>/<post_name>')
# def show_post(post_id,post_name):
#     post = posts.get(post_id)
#     return f"{post}:{post_name}"

# @app.route('/user/<string:user_name>/<int:user_number>/<path:user_path')
# def show_user(user_name,user_number,user_path):
#     user_name_number = f"{user_name}:{user_number}({user_path})"
#     return f"<h1>{user_name_number}</h1>"

if __name__ == '__main__':
    app.run()
