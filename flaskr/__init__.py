import os
from flask import Flask

# ORM TESTING OUTSIDE OF APP
# from datetime import date
# from post import Post
# from base import Session, engine, Base
#
# session = Session()
# posts = session.query(Post).all()
# print ('\nAll posts titles:')
# for post in posts:
#         print(f'{post.title}: {post.body}.')
# session.close()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

        # hello world page
    @app.route('/hello')
    def hello():
        session = Session()
        posts = session.query(Post).all()
        print ('\nAll posts titles:')
        for post in posts:
                print(f'{post.title}: {post.body}.')

        return f'Hello, World! {posts}.'
        session.close()



    from base import Session, engine, Base
    from post import Post

    from . import auth
    app.register_blueprint(auth.bp)

    from . import db
    db.init_app(app)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
