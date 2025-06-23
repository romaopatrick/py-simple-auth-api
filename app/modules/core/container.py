from lagom import Container

from app.modules.auth.auth_container import auth_container

c = Container()

auth_container(c)