from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool


class Conexion:
	DATABASE = 'zona_fyt_db'
	USERNAME = 'root'
	PASSWORD = 'root'
	DB_PORT = 3306
	HOST = 'localhost'
	POOL_SIZE = 5
	POOL_NAME = 'zona_fit_pool'  # Conservado por compatibilidad
	
	_engine = None
	
	@classmethod
	def obtener_pool(cls):
		if cls._engine is None:
			cls._engine = create_engine(
				f"mysql+pymysql://{cls.USERNAME}:{cls.PASSWORD}@{cls.HOST}:{cls.DB_PORT}/{cls.DATABASE}",
				poolclass=QueuePool,
				pool_size=cls.POOL_SIZE,
				max_overflow=10
			)
		return cls._engine
	
	@classmethod
	def obtener_conexion(cls):
		return cls.obtener_pool().raw_connection()
	
	@classmethod
	def liberar_conexion(cls, conexion):
		# Cierra la conexión devuelta por raw_connection()
		conexion.close()


if __name__ == '__main__':
	# Creamos un objeto pool
	pool = Conexion.obtener_pool()
	print(pool)
	
	conexion1 = pool.connect()
	print(conexion1)
	Conexion.liberar_conexion(conexion1)
	print('Se ha liberado el objeto conexion')
