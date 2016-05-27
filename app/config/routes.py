"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes


routes['default_controller'] = 'users'
routes['POST']['/register'] = 'users#register'
routes['POST']['/login'] = 'users#login'
routes['/profile/<id>']='users#profile'
routes['/update_display'] = 'users#update_display'
routes['/logout'] = 'users#logout'
routes['POST']['/update/<id>'] = 'users#update'

routes['/creategroup'] = 'rides#creategroup'
routes['/grouppage'] = 'rides#grouppage'
routes['POST']['/newgroup'] = 'rides#newgroup'
routes['/createride'] = 'rides#createride'
routes['POST']['/addrides/<id>']='rides#addrides'
routes['POST']['/joinrides/<id>']='rides#joinrides'
