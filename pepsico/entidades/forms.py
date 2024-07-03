from django import forms


class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    stock = forms.IntegerField(required=True)

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True )
    email= forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
   

class PedidoForm(forms.Form):
    descripcion=forms.CharField(max_length=500, required=True)
    direccion=forms.CharField(max_length=100, required=True)
    fechaEntrega=forms.DateField(required=True)
    entregado=forms.BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
   



    
