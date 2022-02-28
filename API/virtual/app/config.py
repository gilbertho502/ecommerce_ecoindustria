class Config(object):
    #Conectando con la db de heroku
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:cargamos2022@localhost:5432/prueba'
    SQLALCHEMY_DATABASE_URI = 'postgresql://tbfojzitdztrky:9306e7e2ef6508feed5fc2ca21ad64ccb0aca399452ddaf97cb9352848cd83f2@ec2-54-83-21-198.compute-1.amazonaws.com:5432/dbep35g9le5809'
    SQLALCHEMY_TRACK_MODIFICATIONS = True