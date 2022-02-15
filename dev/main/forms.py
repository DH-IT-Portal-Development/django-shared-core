from django import forms
from django.utils.safestring import mark_safe

from cdh.core import fields as core_fields
from cdh.files.forms import FileField, TrackedFileField


class FormStylesForm(forms.Form):
    text = forms.CharField()

    textarea = forms.CharField(
        widget=forms.Textarea
    )

    django_date = forms.DateField(
        help_text="Using django's version of the field"
    )

    django_time = forms.TimeField(
        help_text="Using django's version of the field"
    )

    django_datetime = forms.DateTimeField(
        help_text="Using django's version of the field"
    )

    django_split_datetime = forms.SplitDateTimeField(
        help_text="Using django's version of the field"
    )

    core_date = core_fields.DateField(
        help_text="Using core's version of the field"
    )

    core_time = core_fields.TimeField(
        help_text="Using core's version of the field"
    )

    core_datetime = core_fields.DateTimeField(
        help_text="Using core's version of the field"
    )

    core_split_datetime = core_fields.SplitDateTimeField(
        help_text="Using django's version of the field"
    )

    checkbox = forms.BooleanField()

    choice = forms.ChoiceField(choices=[
        (1, "Train"),
        (2, "Bus"),
        (3, "Aeroplane"),
        (4, "Bike"),
        (5, "Feet"),
        (6, "Magical Unicorn"),
        (6, "Broom"),
        (6, "Thestrals"),
    ])

    typed_choice = forms.TypedChoiceField(choices=[
        (1, "Train"),
        (2, "Bus"),
        (3, "Aeroplane"),
        (4, "Bike"),
        (5, "Feet"),
        (6, "Magical Unicorn"),
        (6, "Broom"),
        (6, "Thestrals"),
    ])

    radio = forms.TypedChoiceField(
        choices=[
            (1, "Train"),
            (2, "Bus"),
            (3, "Aeroplane"),
            (4, "Bike"),
            (5, "Feet"),
            (6, "Magical Unicorn"),
            (6, "Broom"),
            (6, "Thestrals"),
        ],
        widget=forms.RadioSelect
    )

    integer = forms.IntegerField()

    float = forms.FloatField(help_text="Floating away")

    decimal = forms.DecimalField()

    email = forms.EmailField()

    telephone = core_fields.TelephoneField()

    color = core_fields.ColorField()

    image = forms.ImageField()

    file = forms.FileField(help_text="Not an UiL.files field ;)")

    uil_file = FileField(None)

    uil_tracked_file = TrackedFileField(None)

    IP = forms.GenericIPAddressField()

    url = forms.URLField()

    UUID = forms.UUIDField()

    password = core_fields.PasswordField()


class CustomTemplateFormStylesForm(forms.Form):
    template_name = 'cdh.core/form_template.html'

    text = forms.CharField(
        label="Onderzoeksprojectnaam",
        help_text="Deze naam wordt ook gebruikt als naam voor deze verwerking",
    )

    supervisor = forms.CharField(
        label="Eindverantwoordelijke",
    )

    date_start = core_fields.DateField(
        label="Begin Datum",
        help_text="Op deze datum wordt de verwerking actief in het register "
                  "van verwerkingen"
    )

    date_end = core_fields.DateField(
        label="Eind Datum",
        help_text=mark_safe("Dit is de datum waarop de resultaten worden "
                            "gepubliceerd."
                            "<br/>"
                            "Op deze datum gaat de archiveringstermijn van de "
                            "onderzoeksdata in")
    )


class JqueryUIFormStylesForm(forms.Form):
    date = forms.DateField()

