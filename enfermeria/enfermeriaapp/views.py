from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .helper_classes.generic_methods import is_logged, is_not_empty, es_decimal, es_natural
from .models import Persona, Enfermero, Administrador, Usuario, Servicio
# ========================================
#  HOME PAGE Y LOGIN 
# ========================================
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
        if is_not_empty(l_username) and is_not_empty(l_password):
            eusuario = Usuario.objects.filter(usu_username=l_username, usu_password=l_password, usu_estado=1)
            if len(eusuario) == 1:
                the_user = eusuario[0]
                request.session['user_id'] = the_user.id 
                return HttpResponseRedirect(reverse('enfermeriaapp:homepage_view'))
        return render(request, 'enfermeriaapp/login.html', {'msg':'Usuario o contraseña incorrectas'})

# ========================================
#  GESTIONAR PERSONAL
# ========================================
def gestionar_personal_view(request):
    if request.method == 'GET':
        if is_logged(request.session):
            the_user = Usuario.objects.filter(usu_estado=1, id=request.session['user_id'])[0]
            if the_user.es_admin():
                return render(request, 'enfermeriaapp/gestionar_personal.html')
            else:
                return render(request, 'enfermeriaapp/errorPage.html')
    return render(request, 'enfermeriaapp/errorPage.html')

def ver_personal_view(request):
    if request.method == 'GET':
        if is_logged(request.session):
            the_user = Usuario.objects.filter(usu_estado=1, id=request.session['user_id'])[0]
            if the_user.es_admin():
                personal = Usuario.objects.filter(usu_estado=1)
                return render(request, 'enfermeriaapp/ver_personal.html', {'personal':personal})
            else:
                return render(request, 'enfermeriaapp/errorPage.html')
    else:
        if 'ver' in request.POST:
            the_user = Usuario.objects.filter(usu_estado=1, id=request.POST['ver'])[0]
            return render(request, 'enfermeriaapp/personal_detalle.html', {'user':the_user})
        elif 'eliminar' in request.POST:
            the_user = Usuario.objects.filter(usu_estado=1, id=request.POST['eliminar'])[0]
            return render(request, 'enfermeriaapp/personal_eliminar.html', {'user':the_user})
        elif 'si_eliminar' in request.POST:
            the_user = Usuario.objects.filter(usu_estado=1, id=request.POST['si_eliminar'])[0]
            the_user.usu_estado = 0
            the_persona = the_user.usu_per
            the_persona.per_estado = 0
            the_user.save()
            the_persona.save()
            return HttpResponseRedirect(reverse('enfermeriaapp:ver_personal_view'))
        elif 'cancelar' in request.POST:
            return HttpResponseRedirect(reverse('enfermeriaapp:ver_personal_view'))
            
    return render(request, 'enfermeriaapp/errorPage.html')

def registrar_persona_view(request):
    if request.method == 'GET':
        if is_logged(request.session):
            the_user = Usuario.objects.filter(usu_estado=1, id=request.session['user_id'])[0]
            if the_user.es_admin():
                return render(request, 'enfermeriaapp/registrar_persona.html')
            else:
                return render(request, 'enfermeriaapp/errorPage.html')
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

            if is_not_empty(nper_nombre) and is_not_empty(nper_celular) and es_natural(nper_carnet) and 'per_sexo' in request.POST and is_not_empty(nusu_password) and is_not_empty(usu_nombre):
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
                msg = "Rellene todos los datos correctamente para registrar la persona"
                return render(request, 'enfermeriaapp/registrar_persona.html', {'msg':msg, 'ok':False})
    return render(request, 'enfermeriaapp/errorPage.html')

# ========================================
#  PERFIL
# ========================================

def perfil_view(request):
    if request.method == 'GET':
        if is_logged(request.session):
            the_user = Usuario.objects.filter(usu_estado=1, id=request.session['user_id'])[0]
            return render(request, 'enfermeriaapp/perfil.html', {'user':the_user})
    else:
        if 'editar_perfil' in request.POST:
            the_use = Usuario.objects.filter(usu_estado=1, id=request.POST['editar_perfil'])[0]
            return render(request, 'enfermeriaapp/editar_perfil.html', {'user':the_use})
        elif 'editar' in request.POST:
            the_user = Usuario.objects.filter(usu_estado=1, id=request.POST['editar'])[0]
            the_person = the_user.usu_per
            new_password = request.POST['password']
            if is_not_empty(new_password) and new_password != the_user.usu_password:
                the_user.usu_password = new_password
                the_user.save()
            new_nombre = request.POST['nombre']
            if is_not_empty(new_nombre) and new_nombre != the_person.per_nombre:
                the_person.per_nombre = new_nombre
                the_person.save()
            new_apellidop = request.POST['apellido_p']
            if is_not_empty(new_apellidop) and new_apellidop != the_person.per_apellidoP:
                the_person.apellidoP = new_apellidop
                the_person.save()
            new_apellidom = request.POST['apellido_m']
            if is_not_empty(new_apellidom) and new_apellidom != the_person.per_apellidoM:
                the_person.apellidoM = new_apellidom
                the_person.save()
            new_celular = request.POST['celular']
            if is_not_empty(new_celular) and new_celular != the_person.per_celular:
                the_person.per_celular = new_celular
                the_person.save()
            new_email = request.POST['email']
            if is_not_empty(new_email) and new_email != the_person.per_email:
                the_person.per_email = new_email
                the_person.save()
            new_direccion = request.POST['direccion']
            if is_not_empty(new_direccion) and new_direccion!=the_person.per_direccion:
                the_person.per_direccion = new_direccion
                the_person.save()
            return HttpResponseRedirect(reverse('enfermeriaapp:perfil_view'))

    return render(request, 'enfermeriaapp/errorPage.html')


# ========================================
#  SERVICIOS
# ========================================
def gestionar_servicios_view(request):
    if request.method == 'GET':
        if is_logged(request.session):
            the_user = Usuario.objects.filter(usu_estado=1, id=request.session['user_id'])[0]
            if the_user.es_admin():
                los_servicios = Servicio.objects.filter(ser_estado =1)
                return render(request, 'enfermeriaapp/gestionar_servicios.html', {'servicios':los_servicios})
            else:
                return render(request, 'enfermeriaapp/errorPage.html')
    else:
        if 'nuevo' in request.POST:
            return render(request, 'enfermeriaapp/registrar_servicio.html')
    return render(request, 'enfermeriaapp/errorPage.html')

def registrar_servicio_view(request):
    if request.method == 'POST':
        if 'registrar' in request.POST:
            new_nombre = request.POST['ser_nombre']
            new_precio = request.POST['ser_precio']
            new_desc = request.POST['ser_desc']
            if is_not_empty(new_nombre) and is_not_empty(new_desc) and es_decimal(new_precio):
                new_precio = float(new_precio)
                new_servicio = Servicio(ser_nombre=new_nombre, ser_desc=new_desc, ser_precio=new_precio, ser_estado=1)
                new_servicio.save()
                msg="Servicio registrado"
                return render(request, 'enfermeriaapp/registrar_servicio.html',{'good_message':msg})
            else:
                msg="Datos no validos"
                return render(request, 'enfermeriaapp/registrar_servicio.html',{'message':msg})

