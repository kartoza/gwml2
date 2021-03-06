from django.urls import reverse
from gwml2.forms import WellLevelMeasurementForm
from gwml2.models.well import WellLevelMeasurement
from gwml2.views.form_group.form_group import FormGroupGet, FormGroupCreate


class LevelMeasurementGetForms(FormGroupGet):
    """ Collection form for general information section """

    def get(self):
        """ return forms in dictionary
        :return: dictionary of forms
        :rtype: dict
        """
        form = WellLevelMeasurementForm()
        if self.well.id:
            form.url_chart = reverse(
                'well-measurement-chart',
                kwargs={
                    'id': self.well.id, 'model': 'WellLevelMeasurement'})
        return {
            'level_measurement': form,  # manytomany form
        }


class LevelMeasurementCreateForm(FormGroupCreate):
    """ Collection form for general information section """
    well_level = None
    measurements = []

    def create(self):
        """ create form from data
        """
        self.measurements = []
        if self.data.get('level_measurement', None):
            for measurement in self.data['level_measurement']:
                if not measurement['time']:
                    return
                obj = WellLevelMeasurement.objects.get(
                    id=measurement['id']) if measurement['id'] else WellLevelMeasurement()

                self.measurements.append(
                    self._make_form(
                        obj, WellLevelMeasurementForm, measurement
                    )
                )

    def save(self):
        """ save all available data """
        for measurement in self.measurements:
            measurement.instance.well = self.well
            if not measurement.instance.created_by:
                measurement.instance.created_by = self.well.created_by
            measurement.instance.last_edited_by = self.well.last_edited_by
            measurement.instance.last_edited_at = self.well.last_edited_at
            measurement.save()
