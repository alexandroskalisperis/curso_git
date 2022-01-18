"""============================ GIT - GITHUB ==================================

                           ==PRIMEROS COMANDOS==

_ git init :
            _ se introduce solo una vez al principio y asi se da comienzo al seguimiento del proyecto.
            
_ git add (nombre del archivo o archivos): 
            _ se especifica que archivos son los seleccionados para el seguimiento (por lo general en un 
            proyecto se realiza un seguimiento de todos los archivos a la vez)

_ git add .:
           _ este comando agrega todos los archivos del proyecto. (GIT ADD .)
            
_ git commit -m "un nombre que identifique esta foto(entre comillas)": 
            _ cuando se realiza por primera vez, git pide un USER NAME (debe ser escrito entre comillas) y
            un email (tambien entre comillas)
                    _ git config user.email "alejandro_kali@yahoo.com.ar"
                    _ git config user.name "kali"
            _ realiza la foto instantanea del proyecto la cual sera archivada con un nombre determinado 
            en caso que se quiera vorlver a ese momento del punto de programacion.
            _ si despues de un commit realizamos un status y nos indica en rojo una M, quiere decir que se 
            han realizado cambios en el archivo pero que no se han guardado, por lo tanto si se quiere 
            guardar nuevos cambios en el archivo se debe realizar un nuevo commit.

=========================================================================================================
_ git commit -am (nombre que se le quiera dar para identificar entre comillas):
           _ este comando realiza el ADD Y EL COMMIT a la vez.
=========================================================================================================

_ git status -s: 
            _ en la consola de git. este comando nos muestra todos los archivos que tenemos dentro de la carpeta 
            (en caso de que sea asi) y en que estado estan (osea si se estan siguiendo por git o no)
            
_ git log --oneline :
            _ este comando nos da un listado de todas las fotos instantaneas que hemos realizado con 
            cada commit.
            
_ git reset --hard (el codigo de la foto instantanea):
            _ esta herramienta sirve para desacer cambios.
            _ git reset --hard 1d47775
            


            
=======================================================================================================
                EN CASO QUE SE QUIERA CORREGIR ALGUN NOMBRE GUARDADO:

_ git commit --amend
        _ en la parte inferior de la pantalla ingresar ( :i ) y enter
        _ en la parte superior figura el nombre con error
        _ darle a la tecla suprimir y borrarlo todo luego ESC
        _ otra vez en la base de la pantalla ingresar ( :i ) y enter
        _ y en el mismo lugar (base de la pantalla) el nombre correcto (enter y ESC)
        
        _ para salir del editor y que guarde cambios ingresamos en la base de la pantalla
                ( :wq ) y enter
                
======================================================================================================="""