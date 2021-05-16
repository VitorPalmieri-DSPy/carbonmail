# Aquivo principal (inicial) executado;
# Quando iniciamos o projeto (carbonmail) ele é o primiero a ser executado pelo Python;
# Nós usamos também para ser o Ponto de Entrada da Aplicação.

from carbonmail.email_sender.manager import initializer as init_sender

init_sender()