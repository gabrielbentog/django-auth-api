import multiprocessing

# Define o número de workers (o número recomendado é o número de CPUs disponíveis * 2 + 1)
workers = multiprocessing.cpu_count() * 2 + 1

# Define o tipo de worker (pode ser 'sync', 'gevent', 'eventlet', etc.)
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

# Define o número de threads por worker (opcional)
threads = 4

# Define o timeout em segundos
timeout = 30

# Define o endereço e a porta que o Gunicorn deve escutar
bind = '0.0.0.0:8000'

# Define o nível de log
loglevel = 'info'

# Define o arquivo de log
accesslog = './access.log'
errorlog = './error.log'
