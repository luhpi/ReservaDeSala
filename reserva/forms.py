from django import forms


class SolicitanteForm(forms.Form):
    curso = forms.CharField(label='Curso', max_length=100)
    nome_sol = forms.CharField(label='Nome do solicitante', max_length=100)
    tel = forms.CharField(label='Curso', max_length=20)
    email = forms.CharField(label='Curso', max_length=100)


class AtividadeForm(forms.Form):
    CHOICES = [('Biomedicina', 'Biomedicina'),
               ('Enfermagem', 'Enfermagem'),
               ('Fisioterapia', 'Fisioterapia')
               ('Fonoaudiologia', 'Fonoaudiologia'),
               ('Medicina', 'Medicina'),
               ('Nutrição', 'Nutrição'),
               ('Psicologia', 'Psicologia'),
               ('Especialização', 'Especialização'),
               ('Residência Médica', 'Residência Médica'),
               ('Pós-Graduação', 'Pós-Graduação'),
               ('Outro', 'Outro')]
    atividade = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    outros = forms.CharField(max_length=100)
    data_req_ini = forms.DateField('data inicio')


class ReservaForm(forms.Form):
    sala = forms.CharField(max_length=10)
