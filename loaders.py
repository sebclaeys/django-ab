from django.template.loaders.filesystem import Loader
from ab.middleware import get_current_request


class ABLoader(Loader):

    def load_template_source(self, template_name, template_dirs=None):
        request = get_current_request()

        if not request:
            test_template_name = template_name
        else:
            test_template_name = request.ab.run(template_name)

        return super(ABLoader, self).load_template_source(test_template_name, template_dirs=template_dirs)


