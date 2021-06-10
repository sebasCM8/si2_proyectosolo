from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .helper_classes.generic_methods import is_logged
from .models import Persona, Enfermero, Administrador, Usuario
# Create your views here.
def homePage_view(request):
    if request.method == 'GET':
        has_login = False 
        if 'user_id' in request.session:
            has_login = True
        return render(request, 'enfermeriaapp/homePage.html', {'is_logged':has_login})
    else:
        if 'loginBtn' in request.POST:
            return render(request, 'enfermeriaapp/login.html')
        else:
            request.session.flush()
            return HttpResponseRedirect(reverse('enfermeriaapp:homepage_view'))

def login_view(request):
    if request.method == 'POST':
        l_username = request.POST['username']
        l_password = request.POST['password']
        if l_username!="" and l_password!="":
            eusuario = Usuario.objects.filter(usu_username=l_username, usu_password=l_password, usu_estado=1)
            if len(eusuario) == 1:
                the_user = eusuario[0]
                request.session['user_id'] = the_user.id 
                return HttpResponseRedirect(reverse('enfermeriaapp:homepage_view'))
        return render(request, 'enfermeriaapp/login.html', {'msg':'Usuario o contraseña incorrectas'})

def registrar_persona_view(request):
    if request.method == 'GET':
        if is_logged(request.session):
            return render(request, 'enfermeriaapp/registrar_persona.html')
    else:
        if 'registrar' in request.POST:
            nper_nombre = request.POST['per_nombre']
            nper_celular = request.POST['per_celular']
            nper_carnet = request.POST['per_ci']

            nper_apellidoP = request.POST['per_apPaterno']
            nper_apellidoM = request.POST['per_apMaterno']
            nper_direccion = request.POST['per_direccion']
            nper_email = request.POST['per_email']

            usu_nombre =  request.POST['usu_nombre']
            nusu_password = request.POST['usu_password']

            if nper_nombre!="" and nper_celular!="" and nper_carnet!="" and 'per_sexo' in request.POST and nusu_password!="" and usu_nombre!="":
                aper = Persona.objects.filter(per_ci=nper_carnet, per_estado=1)
                nper_sexo  = request.POST['per_sexo']
                if len(aper) == 0:
                    anombre_usuario = Usuario.objects.filter(usu_username=usu_nombre, usu_estado=1)
                    if len(anombre_usuario) == 0:
                        es_enfermero = False
                        es_admin = False
                        if 'admin' in request.POST:
                            es_admin = True
                        if 'enfermero' in request.POST:
                            es_enfermero = True
                        if es_enfermero or es_admin:
                            new_persona = Persona(per_nombre=nper_nombre, per_apellidoP=nper_apellidoP, per_apellidoM=nper_apellidoM, per_celular=nper_celular, per_ci=nper_carnet, per_direccion=nper_direccion, per_email=nper_email, per_sexo=nper_sexo, per_estado=1)
                            new_persona.save()
                            new_usuario = Usuario(usu_username=usu_nombre, usu_password=nusu_password, usu_estado=1, usu_per=new_persona)
                            new_usuario.save()
                            if es_enfermero:
                                nenfermero = Enfermero(enf_estado = 1, enf_per = new_persona)
                                nenfermero.save()
                            if es_admin:
                                nadmin = Administrador(adm_estado = 1, adm_per = new_persona)
                                nadmin.save()
                            msg = "Persona registrada exitosamente"
                            return render(request, 'enfermeriaapp/registrar_persona.html', {'msg':msg, 'ok':True})
                        else:
                            msg = "Seleccione almenos un trabajo"
                            return render(request, 'enfermeriaapp/registrar_persona.html', {'msg':msg, 'ok':False})
                    else:
                        msg = "El nombre de usuario ya esta en uso"
                        return render(request, 'enfermeriaapp/registrar_persona.html', {'msg':msg, 'ok':False})                               
                else:
                    msg = "El carnet ya esta registrado"
                    return render(request, 'enfermeriaapp/registrar_persona.html', {'msg':msg, 'ok':False})              
            else:
                msg = "Rellene todos los datos para registrar la persona"
                return render(request, 'enfermeriaapp/registrar_persona.html', {'msg':msg, 'ok':False})
    return render(request, 'enfermeriaapp/errorPage.html')