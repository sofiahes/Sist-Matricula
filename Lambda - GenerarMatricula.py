import json
import random
from datetime import datetime
import boto3

def lambda_handler(event, context):
    # Simulacion de Lectura de Sensor
    tenant_id = "UTEC"
    curso_id = "cloud"
    now = datetime.now()
    fecha_hora = str(now.date()) + "." + str(now.time())
    matriculados = random.randint(0, 50) # Desde 0 a 50 alumnos (Nivel de cloud)
    unidad_medida = "alumnos"

    lectura_curso = {
        'tenant_id': tenant_id,
        'lectura_id': curso_id + "." + fecha_hora,
        'lectura_datos': {
            'matriculados': matriculados,
            'unidad_medida': unidad_medida
        }    
    }
    print(lectura_curso) # Para logs en Cloud Watch
    # Publicar en SNS
    sns_client = boto3.client('sns')
    response_sns = sns_client.publish(
        TopicArn = 'arn:aws:sns:us-east-1:702760422273:TemaCursos',
        Subject = 'Nueva Lectura curso',
        Message = json.dumps(lectura_curso),
        MessageAttributes = {
            'tenant_id': {'DataType': 'String', 'StringValue': tenant_id },
            'curso_id': {'DataType': 'String', 'StringValue': curso_id },
            'matriculados': {'DataType': 'Number', 'StringValue': str(matriculados) }
        }
    )    
    return {
        'statusCode': 200,
        'body': response_sns
    }
