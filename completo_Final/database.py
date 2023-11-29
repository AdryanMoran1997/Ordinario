from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
from config_singleton import ConfigSingleton
app = Flask(__name__)
# Utilizar la clase ConfigSingleton para la configuración de la base de datos
config_singleton = ConfigSingleton()
db_config = config_singleton.db_config

def cargar_datos_desde_bd(tabla):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(f"SELECT id{tabla}, {tabla} FROM {tabla}")
    resultados = cursor.fetchall()
    cursor.close()
    connection.close()
    return resultados

# queries.py

class Queries:
    @staticmethod
    def buscar_solicitud(curp):
        config_singleton = ConfigSingleton()
        db_config = config_singleton.db_config

        return """
            SELECT 
                solicitud.Turno, 
                alumno.Nombre AS NombreAlumno, 
                estatus.estatus, 
                tramite.Tramite, 
                municipio.municipio, 
                solicitud.Fecha 
            FROM solicitud
            INNER JOIN alumno ON solicitud.id_alumno = alumno.idAlumno
            INNER JOIN estatus ON solicitud.id_estatus = estatus.idmestatus
            INNER JOIN tramite ON solicitud.id_tramite = tramite.idTramite 
            INNER JOIN municipio ON solicitud.id_municipio = municipio.idmunicipio
            WHERE alumno.Curp = %s
        """
