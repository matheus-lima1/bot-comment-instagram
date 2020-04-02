from selenium import webdriver ## Operações  no navegador 
from selenium.webdriver.common.keys import Keys ## simulação do teclado
import time 
import random

class Instagram:
    def __init__(self, nomeUsuario, senha):
        self.nomeUsuario = nomeUsuario ## username
        self.senha = senha ## passwod
        self.driver = webdriver.Firefox(executable_path="local do geckodriver.exe")

    def login(self):
        time.sleep(5)
        driver = self.driver
        driver.get("https://www.instagram.com") ##chama o site requerido

        time.sleep(5)

        form_usuario = driver.find_element_by_xpath('//input[@name="username"]') ## PROCURAR CAMPO DO FORMULÁRIO DE USER
        form_usuario.click() ##CLICAR NO CAMPO SELECIONADO
        time.sleep(5)
        form_usuario.clear() ##Limpar campo
        form_usuario.send_keys(self.nomeUsuario) ## preencher campo
        time.sleep(5)

        form_senha = driver.find_element_by_xpath("//input[@name='password']") ## PROCURAR CAMPO DO FORMULÁRIO DE SENHA
        form_senha.click()
        time.sleep(5)
        form_senha.clear()
        form_senha.send_keys(self.senha)
        time.sleep(5)
        form_senha.send_keys(Keys.RETURN) ## SIMULA O ENTER
        time.sleep(5)
        self.comentar('calistenia')
        time.sleep(5)


    @staticmethod
    def digitar(frase, local):
        for letra in frase:
            local.send_keys(letra)
            time.sleep(random.randint(2,8)/30)

    def comentar(self,hashtag):

        ##procura a # que queremos pesquisar
        driver = self.driver
        time.sleep(5)
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")

        for i in range(1,3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(5)

        links = driver.find_elements_by_tag_name('a') ## procura todos os elementos a
        time.sleep(5)
        link_fotos = [elem.get_attribute('href') for elem in links] ## recupera elementos uteis    
        [href for href in link_fotos if hashtag in href] ## nova filtragem
        time.sleep(5)

        print(hashtag + ' fotos ' + str(len(link_fotos)))

        for link_foto in link_fotos:
            driver.get(link_foto)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') ## abaixar tela
            try:
                comentarios = ["It's great!","Very good!!"]
                driver.find_element_by_class_name('Ypffh').click()
                form_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(3,8))
                self.digitar(random.choice(comentarios),form_comentario)
                time.sleep(random.randint(30,40))
                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                time.sleep(5)
            except Exception as e:
                print(e)
                time.sleep(5)   




        



bot1 = Instagram('seu_user','sua_senha')
bot1.login()
