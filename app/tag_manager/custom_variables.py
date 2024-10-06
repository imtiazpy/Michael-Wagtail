from wagtail_tag_manager.decorators import register_variable
from wagtail_tag_manager.options import CustomVariable

@register_variable
class Variable(CustomVariable):
    name = "Custom variable"
    description = "Returns a custom value."
    key = "custom"

    def get_value(self, request):
        return "This is a custom variable."