from django import forms
import re


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[("0", "False"), ("1", "True")], required=False
    )
    address = forms.CharField(required=False)
    payment = forms.ChoiceField(choices=[("0", "False"), ("1", "True")], required=False)

    def clean_phone_number(self):
        data = self.cleaned_data["phone_number"]

        if not data.isdigit():
            raise forms.ValidationError("Номер телефона має складатися лише з цифр")

        pattern = re.compile(r"^\d{10}$")

        if not pattern.match(data):
            raise forms.ValidationError("Номер телефона має складатися з 10 цифр")

        return data

