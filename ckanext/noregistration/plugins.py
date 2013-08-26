from ckan import plugins

def no_registering(context, data_dict):
    return {'success': False, 'msg': plugins.toolkit._('You cannot register '
        'for this site.')}

class NoSelfRegistration(plugins.SingletonPlugin):
    plugins.implements(plugins.IAuthFunctions, inherit=True)

    def get_auth_functions(self):
        return {
            'user_create': no_registering
        }