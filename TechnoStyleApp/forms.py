from django import forms

class FormularioAgregar(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    categoria = forms.CharField()
    precio = forms.IntegerField()

class FormularioAgregarCliente(forms.Form):
    nombre = forms.CharField()
    dni = forms.IntegerField()
    correo = forms.CharField()
    telefono = forms.IntegerField()

class FormularioAgregarSucursal(forms.Form):
    nombre = forms.CharField()
    numero_sucursal = forms.IntegerField()
    direccion = forms.CharField()


class BuscaProductos(forms.Form):
    marca = forms.CharField()