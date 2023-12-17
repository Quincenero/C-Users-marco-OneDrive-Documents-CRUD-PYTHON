import conexion as con

def save(persona):
    persona=dict(persona)
    try:
        db = con.conectar()
        cursor = db.cursor()
        columnas = tuple(persona.keys())
        valores = tuple(persona.values())
        sql = """
        INSERT INTO PERSONAS{campos} VALUES(?,?,?,?,?,?)
        """.format(campos=columnas)
        #return sql
        cursor.execute(sql,(valores))
        creada=cursor.rowcount>0
        db.commit()
        
        if creada:
            return {"respuesta ":creada, "mensaje":"Persona registrada"}
        else:
            return {"respuesta ":creada, "mensaje":"No se logro registrar a la persona]"}

    except Exception as ex:
        if "UNIQUE" in str(ex) and "correo" in str(ex):
            mensaje= "Ya existe una persona con ese correo"
        elif "UNIQUE" in str(ex) and "dni" in str(ex):
            mensaje= "Ya existe una persona con ese dni"
        else:
            mensaje=str(ex)    
        return{"respuesta":False, "mensaje ":mensaje }
    
    finally:
       cursor.close()
       db.close() 