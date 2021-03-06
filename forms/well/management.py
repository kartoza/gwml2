from django.forms.models import model_to_dict
from gwml2.models.management import Management
from gwml2.forms.well.base import WellBaseForm


class ManagementForm(WellBaseForm):
    """
    Form for management.
    """

    def __init__(self, *args, **kwargs):
        super(ManagementForm, self).__init__(*args, **kwargs)
        self.fields['number_of_users'].widget.attrs['min'] = 0
        self.fields['description'].widget.attrs['maxlength'] = 500
        self.fields['number_of_users'].widget.attrs['maxlength'] = 7

    class Meta:
        model = Management
        fields = ('manager', 'description', 'groundwater_use', 'number_of_users')

    @staticmethod
    def make_from_data(instance, data, files):
        """ Create form from request data
        :param instance: Management object
        :type instance: Management

        :param data: dictionary of data
        :type data: dict

        :param files: dictionary of files that uploaded
        :type files: dict

        :return: Form
        :rtype: ManagementForm
        """

        return ManagementForm(
            data, files, instance=instance)

    @staticmethod
    def make_from_instance(instance):
        """ Create form from instance
        :param instance: Management object
        :type instance: Management

        :return: Form
        :rtype: ManagementForm
        """
        data = {}
        if instance:
            data = model_to_dict(instance)
        return ManagementForm(initial=data)
