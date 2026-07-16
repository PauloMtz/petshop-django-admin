from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.template.loader import render_to_string

from setup import settings
from ..forms import consulta_forms
from ..services import pet_service, consulta_service
from ..entidades import consulta

@user_passes_test(lambda u: u.cargo == 'Veterinário', login_url='login')
def inserir_consulta(request, id):
    if request.method == "POST":
        form_consulta = consulta_forms.ConsultaPetForm(request.POST)
        pet = pet_service.buscar_pet_id(id)
        if form_consulta.is_valid():
            motivo_consulta = form_consulta.cleaned_data["motivo_consulta"]
            peso_atual = form_consulta.cleaned_data["peso_atual"]
            medicamento_atual = form_consulta.cleaned_data["medicamento_atual"]
            medicamentos_prescritos = form_consulta.cleaned_data["medicamentos_prescritos"]
            exames_prescritos = form_consulta.cleaned_data["exames_prescritos"]
            consulta_nova = consulta.ConsultaPet(pet=pet, motivo_consulta=motivo_consulta,
                peso_atual=peso_atual, medicamento_atual=medicamento_atual,
                medicamentos_prescritos=medicamentos_prescritos,
                exames_prescritos=exames_prescritos)
            consulta_service.cadastrar_consulta(consulta_nova)
            return redirect('buscar_pet_id', pet.id)
    else:
        form_consulta = consulta_forms.ConsultaPetForm()
    return render(request, 'consultas/form_consulta.html', {'form_consulta': form_consulta})

@login_required(login_url='login')
def buscar_consulta_id(request, id):
    consulta = consulta_service.buscar_consulta(id)
    return render(request, 'consultas/consulta_detalhes.html', {'consulta': consulta})

@login_required(login_url='login')
def enviar_email_consulta(request, id):
    consulta = consulta_service.buscar_consulta(id)
    pet_consulta = pet_service.buscar_pet_id(consulta.pet.id)
    assunto = "Detalhes da Consulta do Pet"
    html_conteudo = render_to_string('consultas/envio_email_consulta.html', {'consulta': consulta})
    corpo_email = 'Resumo de sua consulta.'
    email_remetente = settings.EMAIL_HOST_USER
    email_destinatario = pet_consulta.dono.email
    send_mail(assunto, corpo_email, email_remetente, [email_destinatario], html_message=html_conteudo)
    return redirect('buscar_consulta_id', id=id)
