import pandas as pd
import numpy as np
import soporte as sp
import mysql.connector




carga = sp.Cargar("tiburones_py", "AlumnaAdalab")
crear = carga.crear_bbdd(carga)
print(crear)