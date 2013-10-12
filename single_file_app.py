from pyramid.response import Response
from pyramid.config import Configurator
from pyramid.view import view_config
from wsgiref.simple_server import make_server
from pyramid_jinja2 import IJinja2Environment #?#?#?
import json
from pyramid.renderers import JSON
#from pyramid.session import UnencryptedCookieSessionFactoryConfig
#from pyramid.authentication import AuthTktAuthenticationPolicy
#from pyramid.authorization import ACLAuthorizationPolicy
 
 
@view_config(route_name='home', renderer='mytemplate.jinja2')
def my_view(request):
    return {'user': {'testkey1':'testvalue1', 'testkey2':'testvalue2'}}
 
def json_dumps(d):
    return JSON(d)

if __name__ == '__main__':
#    authn_policy = AuthTktAuthenticationPolicy(secret='s0secret')
#    authz_policy = ACLAuthorizationPolicy()
#    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config = Configurator(
        settings={},
#        session_factory=session_factory,
#        authentication_policy=authn_policy,
#        authorization_policy=authz_policy
    )
    config.include('pyramid_jinja2')
    jinja_env = config.registry.queryUtility(IJinja2Environment)
    jinja_env.filters['json_dumps'] = json_dumps
    config.add_route('home', '/')
    config.scan('.')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()




