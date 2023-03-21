from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Navegar até o Wpp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

#tempo de espera para scanear o QR CODE

time.sleep(30)
#definir contatos e grupos e mensagem para enviar


contatos = ['Dev teste']
mensagem = 'Olá, está é uma mensagem automática, eu sou apenas uma IA digitando está mensagem!'
#buscar contatos/grupos


def buscar_contato(contato):
    campo_pesquisa = driver.find_element(By.XPATH, '//div[contains(@class, "selectable-text copyable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element(By.XPATH, '//div[contains(@class, "selectable-text copyable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
    

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
#campo de pesquisa 'selectable-text copyable-text'
# campo de chat 'selectable-text copyable-text'
