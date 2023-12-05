# Sistema de Matricula 
# Generar matricula:
  -> Contiene SNS con política de filtro y Correo<br>
  ->Tiene SQS a Insertar Matricula<br>
  -> Suscripción a correo cuando matriculados sea mayor a 45 <br>
# Insertar matricula: <br>
  -> Ingresa data en tabla dynamoDB "TMatricula"<br>
  -> Contiene SNS de filtro<br>
# Textract Lambda: <br>
  -> Contiene un SNS con filtro a clase de ADA <br>
  -> Suscripción a correo<br>

![Diagrama.](/Diagrama.png)
