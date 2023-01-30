from mysql.connector.errors import Error

print(str(Error(errno=10999)))

#Rewrite module to suport INSERT ERROS, UPDATE ERROS and others no just connection or desconnection erros