from django.contrib.gis.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from gwml2.models.general import Quantity
from gwml2.models.term import (
    TermConstructionStructureType, TermReferenceElevationType)


class Construction(models.Model):
    """ Construction
    """
    pump_installer = models.CharField(
        null=True, blank=True, max_length=512,
        help_text="Name of the company or person who installed the pump."
    )
    pump_description = models.TextField(
        null=True,
        blank=True,
        help_text="Any relevant information on the pump (e.g. model, capacity, energy supply, depth)."
    )

    class Meta:
        db_table = 'construction'


class ConstructionStructure(models.Model):
    """
    Structure of construction
    """
    construction = models.ForeignKey(
        Construction, on_delete=models.CASCADE,
        null=True, blank=True
    )
    type = models.ForeignKey(
        TermConstructionStructureType, on_delete=models.SET_NULL,
        null=True, blank=True
    )
    reference_elevation = models.ForeignKey(
        TermReferenceElevationType, on_delete=models.SET_NULL,
        null=True, blank=True
    )

    # information
    material = models.CharField(
        null=True, blank=True, max_length=512
    )
    description = models.TextField(
        null=True,
        blank=True)

    # position
    top_depth = models.OneToOneField(
        Quantity, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='structure_top_depth'
    )
    bottom_depth = models.OneToOneField(
        Quantity, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='structure_bottom_depth'
    )
    diameter = models.OneToOneField(
        Quantity, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='structure_diameter'
    )

    class Meta:
        db_table = 'construction_structure'


@receiver(post_delete, sender=ConstructionStructure)
def delete_structure(sender, instance, **kwargs):
    if instance.top_depth:
        instance.top_depth.delete()
    if instance.bottom_depth:
        instance.bottom_depth.delete()
    if instance.diameter:
        instance.diameter.delete()
