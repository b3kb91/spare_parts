from django import forms


class OrderForm(forms.Form):
    first_name = forms.CharField(label="Имя", max_length=100, required=True)
    last_name = forms.CharField(label="Фамилия", max_length=100, required=True)
    phone = forms.CharField(label="Телефон", max_length=100, required=True)
    email = forms.EmailField(label="Электронная почта", required=True, max_length=100)

    requires_delivery = forms.ChoiceField(
        label="Требуется доставка?",
        choices=[
            ("0", "Нет"),
            ("1", "Да"),
        ],
        required=True,
    )

    delivery_address = forms.CharField(label="Адрес доставки", required=False)

    payment_on_get = forms.ChoiceField(
        label="Оплата при получении?",
        choices=[
            ("0", "Нет"),
            ("1", "Да"),
        ],
        required=True,
    )

    def clean_phone(self):
        data = self.cleaned_data["phone"]

        if not data.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")

        return data
