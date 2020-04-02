from selenium import webdriver ## Operações  no navegador 
from selenium.webdriver.common.keys import Keys ## simulação do teclado
import time 
import random

class Instagram:
    def __init__(self, nomeUsuario, senha):
        self.nomeUsuario = nomeUsuario ## username
        self.senha = senha ## passwod
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\Matheus\\Desktop\\insta\\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com") ##chama o site requerido

        time.sleep(5)

        ## a href="/accounts/Login/?source=auth_switcher" -> notação HTML

        ## botao_login = driver.find_element_by_xpath("a[@href='/accounts/Login/?source=auth_switcher']")
        ## botao_login.click()

        form_usuario = driver.find_element_by_xpath('//input[@name="username"]') ## PROCURAR CAMPO DO FORMULÁRIO DE USER
        form_usuario.click() ##CLICAR NO CAMPO SELECIONADO
        form_usuario.clear() ##Limpar campo
        form_usuario.send_keys(self.nomeUsuario) ## preencher campo

        form_senha = driver.find_element_by_xpath("//input[@name='password']") ## PROCURAR CAMPO DO FORMULÁRIO DE SENHA
        form_senha.click()
        form_senha.clear()
        form_senha.send_keys(self.senha)
        time.sleep(3)
        form_senha.send_keys(Keys.RETURN) ## SIMULA O ENTER
        time.sleep(5)
        self.comentar('calistenia')


    @staticmethod
    def digitar(frase, local):
        for letra in frase:
            local.send_keys(letra)
            time.sleep(random.randint(2,8)/30)

    def comentar(self,hashtag):

        ##procura a # que queremos pesquisar
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")

        for i in range(1,3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(5)

        links = driver.find_elements_by_tag_name('a') ## procura todos os elementos a
        link_fotos = [elem.get_attribute('href') for elem in links] ## recupera elementos uteis    
        [href for href in link_fotos if hashtag in href] ## nova filtragem

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




        



bot1 = Instagram('dixx_vivitheusz','crocodilosazuis')
bot1.login()
