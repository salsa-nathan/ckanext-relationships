import ckan.lib.base as base
import ckan.lib.helpers as h
import ckan.logic as logic
import ckan.model as model
import ckan.plugins.toolkit as toolkit

from ckan.common import _, c, request
from ckan.lib.navl.dictization_functions import unflatten
from flask import Blueprint

abort = base.abort
clean_dict = logic.clean_dict
get_action = logic.get_action
NotFound = logic.NotFound
NotAuthorized = logic.NotAuthorized
parse_params = logic.parse_params
render = toolkit.render
tuplize_dict = logic.tuplize_dict

# relationships = Blueprint('relationships', __name__, url_prefix=u'/dataset')
relationships = Blueprint('relationships', __name__)


def index(id):
    context = {'model': model, 'session': model.Session,
               'user': c.user, 'for_view': True,
               'auth_user_obj': c.userobj}
    data_dict = {'id': id}

    extra_vars = {}

    try:
        extra_vars['pkg_dict'] = get_action('package_show')(context, data_dict)
        c.pkg = context['package']
    except (NotFound, NotAuthorized):
        abort(404, _('Dataset not found'))

    return render(
        'package/relationships.html',
        extra_vars=extra_vars
    )


def create(id):
    if request.method == 'POST':
        data_dict = clean_dict(unflatten(tuplize_dict(parse_params(request.form))))

        object = data_dict.get('object', None)
        type = data_dict.get('type', None)

        if object:
            try:
                relationship = get_action('package_relationship_create')({}, {
                    'subject': id,
                    'object': object,
                    'type': type
                })
            except Exception as e:
                # TODO: Deal with exception raised when adding as child_of:
                # 'Parent instance <PackageRelationship at 0x7fd118badb10> is not bound to a Session; lazy load operation of attribute 'subject' cannot proceed'
                print(str(e))

    return h.redirect_to(h.url_for('relationships.index', id=id))


def delete(id, type, object):
    get_action('package_relationship_delete')({}, {
        'subject': id,
        'object': object,
        'type': type
    })
    return h.redirect_to(h.url_for('relationships.index', id=id))


relationships.add_url_rule(u'/dataset/<id>/relationships', view_func=index)
relationships.add_url_rule(u'/dataset/<id>/relationships/create',
                           methods=[u'POST'],
                           view_func=create)
relationships.add_url_rule(u'/dataset/<id>/relationships/delete/<type>/<object>', view_func=delete)