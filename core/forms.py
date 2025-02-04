from django import forms
from .models import FormularioModel
from django.core.mail import EmailMessage

class FormularioModelForm(forms.ModelForm):
    class Meta:
        model = FormularioModel
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'required': True, 'class': 'custom-date-input'}),
            'turno': forms.Select(attrs={'required': True}),
            'conferente': forms.TextInput(attrs={'placeholder': 'Nome do conferente', 'required': True}),
            'cliente': forms.TextInput(attrs={'placeholder': 'Nome do cliente', 'required': True}),
            'transportadora': forms.TextInput(attrs={'placeholder': 'Nome da transportadora', 'required': True}),
            'num_nota': forms.TextInput(attrs={'placeholder': 'Ex: 000.000.000', 'required': True}),
            'quantidade_cx': forms.NumberInput(attrs={'min': 1, 'max': 4000, 'required': True}),
            'quantidade_recebidas': forms.NumberInput(attrs={'min': 1, 'max': 4000, 'required': True}),
            'motivo': forms.Select(attrs={'required': True}),
            'setor': forms.Select(attrs={'required': True}),
            'valor': forms.NumberInput(attrs={'step': '0.01', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder':'Digite o email que deseja enviar'})
        }
        
    def send_mail(self):
        data = self.cleaned_data['data']
        turno = self.cleaned_data['turno']
        conferente = self.cleaned_data['conferente']
        cliente = self.cleaned_data['cliente']
        transportadora = self.cleaned_data['transportadora']
        num_nota = self.cleaned_data['num_nota']
        quantidade_cx = self.cleaned_data['quantidade_cx']
        quantidade_recebidas = self.cleaned_data['quantidade_recebidas']
        motivo = self.cleaned_data['motivo']
        setor = self.cleaned_data['setor']
        valor = self.cleaned_data['valor']
        email = self.cleaned_data['email']
        
        conteudo = f"""Data: {data}\nTurno: {turno}\nConferente: {conferente}\nCliente: {cliente}\nTransportadora: {transportadora}\nNº da nota: {num_nota}
        \nQuantidade de caixas: {quantidade_cx}\nQuantidade de caixas recebidas: {quantidade_recebidas}\nMotivo: {motivo}\nSetor: {setor}\nValor: {valor}\nEmail: {email}"""
                    
        mail = EmailMessage(
            subject=f'Devolução do cliente {cliente}',
            body=conteudo,
            from_email= 'contato@seudominio.com.br',
            to=['justodeandrade@gmail.com',],
            headers={'reply_to': email},
        )
        
        mail.send()
    