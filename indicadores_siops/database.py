# Bibliotecas 
from peewee import *
from playhouse.db_url import connect 
import os 

# Estabelecendo conexão 
database = connect("mysql+pymysql://alexandre:34340012@localhost:3306/Alerts_trends")

# Criando a classe de conexão mysql 
class MySQLBitField(Field):
    field_type = "bit" 
    
    def __init__(self,*_,**__):
        pass

# Criando a classe do modelo basico 
class BaseModel(Model):
    class Meta:
        database = database 

# Tabela de Capacidade do Municipio 
class Indicador_de_Capacidade_do_Municipio(BaseModel):
    municipio = TextField()
    estado = TextField()
    codigo = IntergerField()
    ano = IntergerField()
    Capacidade = FloatField()

    class Meta:
        table_name = "Indicador_de_Capacidade_do_Municipio" 

# Indicadores de Dependência 
class Indicadores_de_Dependência(BaseModel):
    municipio = TextField()
    estado = TextField()
    codigo = IntergerField()
    ano = IntergerField()
    Dependência_União = FloatField()
    Dependência_Estado = FloatField()
    class Meta:
        table_name = "Indicadores_de_Dependência"

# Indicadores de Dependência do Sus 
class Indicadores_de_Dependência_SUS(BaseModel):
    municipio = TextField()
    estado = TextField()
    codigo = IntergerField()
    ano = IntergerField()
    Dependência_União = FloatField()
    Dependência_Estado = FloatField()
    class Meta:
        table_name = "Indicadores_de_Dependência_Sus"
