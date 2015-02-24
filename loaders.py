from django.template.loaders.filesystem import Loader
from ab.middleware import get_current_request


class ABLoader(Loader):

    def load_template_source(self, template_name, template_dirs=None):
        request = get_current_request()
        test_template_name = template_name

        if request and not request.user_agent.is_bot:
            if 'exp' in request.GET:
                # If exp is provided, the experiment is not activated but the specific temnpalte is loaded
                test_template_name = request.ab.get_by_idx(template_name, int(request.GET['exp']))
            else:
                test_template_name = request.ab.run(template_name)

        return super(ABLoader, self).load_template_source(test_template_name, template_dirs=template_dirs)


