# ACTIVAR VENV
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows

# EJECUTAR MIGRACIONES
    python manage.py makemigrations
    python manage.py migrate

# INICIAR SERVIDOR DE DESARROLLO DJANGO
    python manage.py runserver

# SERVIDOR DE DESARROLLO DJANGO
    http://127.0.0.1:8000/admin


# ESTA APLIACIÓN DA SOLUCIÓN A LOS SIGUIENTES REQUERIMIENTOS:e
## 1. Usuarios  
### a. Crear usuarios. Los campos básicos deben ser:  
   - **Correo electrónico**  
   - **Nombre completo**  
   - **Apodo**  
   - **Foto o Avatar** (pueden ser imágenes predefinidas)  

### b. Modificar información del usuario, excepto el correo electrónico.  

### c. Dar de baja (Inactivar el usuario).  

## 2. Contactos  
### a. Añadir a mis contactos usuarios de la aplicación por medio de su correo electrónico.  

### b. Eliminar usuarios de mis contactos solo si no tienen eventos asociados.  

## 3. Eventos  
### a. Crear eventos. Los campos básicos deben ser:  
   - **Nombre**  
   - **Descripción**  
   - **Tipo:** Viaje, Hogar, Pareja, Comida, Otro  
   - **Foto o Avatar** (pueden ser imágenes predefinidas por tipo)  

### b. Modificar datos del evento  
   - Permitir editar solo si aún no tiene actividades.  

### c. Agregar contactos al evento.  
   - Solo el creador del evento puede agregarlos.  
   - El contacto debe aceptar (**Gestión de invitaciones y notificaciones**).  

### d. Quitar contactos del evento.  
   - Solo el creador del evento puede quitarlos.  
   - Solo se puede eliminar si no se ha registrado alguna actividad en el evento.  

### e. Los usuarios deben ver todos los eventos en los que son participantes, hayan o no creado el evento.  

### f. Todos los contactos del evento deben ver las actividades registradas en el evento.  

## 4. Actividades  
### a. Deben ser creadas desde un evento. Los campos básicos deben ser:  
   - **Descripción**  
   - **Valor**  
   - **Seleccionar ninguno o más participantes de la actividad** entre los contactos asociados al evento.  

### b. Permitir diligenciar el porcentaje de participación de cada contacto o el valor fijo de cada participante.  
   - **La sumatoria del valor no debe exceder el valor total de la actividad.**  
   - Esto debe sumar al saldo de cada contacto; es decir, el valor de la actividad se divide como se configure.  

### c. Por defecto la aplicación debe sugerir el porcentaje de participación por partes iguales.  

### d. Permitir modificar la actividad solo al creador.  

### e. Permitir eliminar la actividad solo al creador.  

## 5. Saldos  
### a. Permitir ver los saldos de cada contacto por evento.  

### b. Permitir ver mis saldos pendientes a mis contactos.  
   - _(Por `eventContacts`, buscamos por `eventId.owner` y traemos el balance.)_  

### c. Pagar saldo a mis contactos.  
   - Pueden registrar el pago cualquiera de los dos involucrados: **deudor o prestador**.  

### d. Permitir hacer pagos parciales.  
