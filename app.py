from flaskr import create_app
from flaskr.modelos.modelos import Album, Usuario, Medio, Cancion
#from flask_restful import Api
from .modelos import db
"""from .vistas import VistaCanciones, VistaCancion, VistaSignIn, VistaLogIn, VistaAlbum, VistaAlbumsUsuario, VstaCancionesAlbum
from flask_jwt_extended import JWTManager"""


app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()


with app.app_context():  # Este contexto generalmente se utiliza en frameworks web para ejecutar código relacionado con la aplicación.

# Creación de instancias de las clases
 u = Usuario(nombre='juan', contrasena='12345')
 a = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
 c = Cancion(titulo='Earth Song', minutos=6, segundos=45, interprete='Michael Jackson')

 # Establecimiento de relaciones entre las instancias
 u.albumes.append(a)
 a.canciones.append(c)
 
 # Agregar las instancias a la sesión de la base de datos
 db.session.add(u)
 db.session.add(c)
 
 # Confirmar los cambios en la base de datos
 db.session.commit()
 
 # Consultas a la base de datos y visualización de resultados
 print(Usuario.query.all())
 print(Album.query.all())
 print(Album.query.all()[0].canciones)
 print(Cancion.query.all())
 
 # Eliminación de una instancia y confirmación de los cambios
 db.session.delete(a)  # Suponiendo que 'o' es una instancia a eliminar
 
 # Nuevamente, se consultan los datos para verificar los cambios
 print(Album.query.all())
 print(Cancion.query.all())


"""api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaAlbumsUsuario, '/usuario/<int:id_usuario>/albumes')
api.add_resource(VistaAlbum, '/album/<int:id_album>')
api.add_resource(VistaCancionesAlbum, '/album/<int:id_album>/canciones')

jwt = JWTManager(app)"""


