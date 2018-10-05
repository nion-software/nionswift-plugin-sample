# standard libraries
import gettext

from samplelib import sampler

_ = gettext.gettext



class SampleMenuItemDelegate:

    def __init__(self, api):
        self.__api = api
        self.menu_id = "example_menu"  # required, specify menu_id where this item will go
        self.menu_name = _("Examples")  # optional, specify default name if not a standard menu
        self.menu_before_id = "window_menu"  # optional, specify before menu_id if not a standard menu
        self.menu_item_name = _("Run Sample")  # menu item name

    def menu_item_execute(self, window):
        sampler.sample_function()


class MenuSampleExtension:

    # required for Swift to recognize this as an extension class.
    extension_id = "sample.menu_item_call_sample"

    def __init__(self, api_broker):
        # grab the api object.
        api = api_broker.get_api(version="~1.0")
        # be sure to keep a reference or it will be closed immediately.
        self.__menu_item_ref = api.create_menu_item(SampleMenuItemDelegate(api))

    def close(self):
        self.__menu_item_ref.close()
        self.__menu_item_ref = None
