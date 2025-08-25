from conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    SELECCIONAR_ID = 'SELECT * FROM cliente WHERE id=%s'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        clientes = []  # 👈 siempre inicializamos
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
        except Exception as e:
            print(f'Ocurrió un error al seleccionar clientes: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
        return clientes  # 👈 siempre retornamos lista, aunque esté vacía

    @classmethod
    def seleccionar_por_id(cls, id):
        cliente = None
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR_ID, (id,))
            registro = cursor.fetchone()
            if registro:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
        except Exception as e:
            print(f'Ocurrió un error al seleccionar un cliente por id: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
        return cliente  # puede ser None si no existe, pero manejable en la app

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        cursor = None
        filas_afectadas = 0
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.INSERTAR, (cliente.nombre, cliente.apellido, cliente.membresia))
            conexion.commit()
            filas_afectadas = cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al insertar un cliente: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
        return filas_afectadas

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        cursor = None
        filas_afectadas = 0
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.ACTUALIZAR, (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id))
            conexion.commit()
            filas_afectadas = cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al actualizar un cliente: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
        return filas_afectadas

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        cursor = None
        filas_afectadas = 0
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.ELIMINAR, (cliente.id,))
            conexion.commit()
            filas_afectadas = cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar un cliente: {e}')
        finally:
            if cursor:
                cursor.close()
            if conexion:
                Conexion.liberar_conexion(conexion)
        return filas_afectadas


if __name__ == '__main__':
    clientes = ClienteDAO.seleccionar()
    print("Clientes en la base de datos:")
    for cliente in clientes:
        print(cliente)
