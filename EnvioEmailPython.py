#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install secure-smtplib')
get_ipython().system('pip install python-dotenv')


# In[4]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações do servidor SMTP e credenciais do remetente
smtp_server = 'seu_smtp_server'
smtp_port = 465  # Use 465 para SSL ou 587 para TLS
sender_email = 'equipeprotecta@gmail.com'
password = 'sua_senha'

def enviar_email(destinatario, assunto, corpo):
    try:
        # Criar uma mensagem
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = destinatario
        msg['Subject'] = assunto

        # Corpo do email
        msg.attach(MIMEText(corpo, 'plain'))

        # Conectar ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Ativar a criptografia TLS
        server.login(sender_email, password)

        # Enviar o email
        server.sendmail(sender_email, destinatario, msg.as_string())

        # Encerrar a conexão com o servidor SMTP
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print("Ocorreu um erro ao enviar o email:", str(e))

# Exemplo de uso
destinatario = 'rosendomilenia4@gmail.com'
assunto = 'Olá, usuária'
corpo = 'Olá, usuária, alguem esta sofrendo assedio dentro desse coletivo! .'

enviar_email(destinatario, assunto, corpo)

