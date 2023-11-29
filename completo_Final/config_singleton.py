class ConfigSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigSingleton, cls).__new__(cls)
            # Configuración de la base de datos
            cls._instance.db_config = {
                'host': 'localhost',
                'user': 'root',
                'password': '123456',
                'database': 'alumnotramite3',  # Nombre de tu base de datos
            }
        return cls._instance

