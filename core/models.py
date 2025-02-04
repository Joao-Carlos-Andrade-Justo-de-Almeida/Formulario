from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class FormularioModel(models.Model):
    TURNO = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    ]
    
    SETOR = [
        ('Logística', 'Logística'),
        ('Comercial', 'Comercial'),
        ('Fábrica', 'Fábrica'),
        ('Cliente', 'Cliente')
    ]
    
    Motivo = [
        ('Avaria', 'Avaria'),
        ('Inversão', 'Inversão'),
        ('Sem Pedido', 'Sem Pedido'),
        ('Sem Espaço', 'Sem Espaço'),  
    ]
    
    data = models.DateField('Data')
    turno = models.CharField('Turno:', max_length=1, choices=TURNO, default='A')
    conferente = models.CharField('Conferente:', max_length=50)
    cliente = models.CharField('Cliente:', max_length= 100)
    transportadora = models.CharField('Transportadora:', max_length=100)
    num_nota = models.CharField('Número da nota:', max_length=11)
    quantidade_cx = models.IntegerField('Quantidade de caixas na nota:', validators=[MinValueValidator(1), MaxValueValidator(4000)])
    quantidade_recebidas = models.IntegerField('Quantidade de caixas recebidas:', validators=[MinValueValidator(1), MaxValueValidator(4000)])
    motivo = models.CharField('Motivo da devolução:', max_length=11, choices=Motivo, default='Avaria')
    setor = models.CharField('Setor que causou a devolução:',  max_length=9, choices=SETOR, default='Logística')
    valor = models.DecimalField('Valor da devolução:', decimal_places=2, max_digits=10)
    email = models.EmailField('Email', max_length=50)