from django.shortcuts import render
from .forms import FormularioModelForm
from django.contrib import messages

def index(request):
    form = FormularioModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.send_mail()
            devo = form.save(commit=False)
            devo.save()
            messages.success(request,"Formulário enviado com sucesso")
            form = FormularioModelForm()
        else:
            messages.error(request,"Erro no formulário")
    else:
        form = FormularioModelForm()
    context = {
        'form': form
    }
               
    return render(request,'index.html', context)
            
# Create your views here.
