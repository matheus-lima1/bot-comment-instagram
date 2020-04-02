from selenium import webdriver ## Operações  no navegador 
from selenium.webdriver.common.keys import Keys ## simulação do teclado
import time 
import random

class Instagram:
    def __init__(self, nomeUsuario, senha,publicacao,num):
        self.num = num
        self.nomeUsuario = nomeUsuario 
        self.senha = senha 
        # escreva o caminho do arquivo geckodriver.exe usando duas barras "\\"
        self.driver = webdriver.Firefox(executable_path="caminho\\geckodriver.exe") 
        self.publicacao = publicacao

    def login(self):
        time.sleep(5)
        driver = self.driver
        driver.get("https://www.instagram.com") 

        time.sleep(5)

        form_usuario = driver.find_element_by_xpath('//input[@name="username"]') 
        form_usuario.click() 
        time.sleep(5)
        form_usuario.clear() 
        form_usuario.send_keys(self.nomeUsuario)
        time.sleep(5)

        form_senha = driver.find_element_by_xpath("//input[@name='password']") 
        form_senha.click()
        time.sleep(5)
        form_senha.clear()
        form_senha.send_keys(self.senha)
        time.sleep(5)
        form_senha.send_keys(Keys.RETURN) 
        time.sleep(5)
        self.comentar()
        time.sleep(5)


    @staticmethod
    def digitar(frase, local):
        for letra in frase:
            local.send_keys(letra)
            time.sleep(random.randint(2,8)/30)

    def comentar(self):

 
        driver = self.driver
        time.sleep(5)
        driver.get(self.publicacao)



        for i in range(1,2):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(5)


        try:
            #insira os comentários desejados nesta lista
            comentarios = ["It's great! 1 ","I love 2 ","lindo ! 3 ", "start 4 ","the best 5 ", "yeees 6"] 
            c=0

            for i in range(int(len(comentarios))):
                time.sleep(5)
                c = c+1
                if(c!=int(self.num)):
 
                    driver.find_element_by_xpath("//textarea[@aria-label='Adicione um comentário...']").click()
                    form_comentario = driver.find_element_by_xpath("//textarea[@aria-label='Adicione um comentário...']")
                    time.sleep(random.randint(3,8))
                    self.digitar(comentarios[i],form_comentario)
                    time.sleep(random.randint(5,8))
                    
                else:
                    
                    driver.find_element_by_xpath("//textarea[@aria-label='Adicione um comentário...']").click()
                    form_comentario = driver.find_element_by_xpath("//textarea[@aria-label='Adicione um comentário...']")
                    time.sleep(random.randint(3,8))
                    self.digitar(comentarios[i],form_comentario)
                    time.sleep(random.randint(5,8))

                    driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                    time.sleep(5)
                    c=0
        except Exception as e:
            print(e)
            time.sleep(5) 
            


url = input("informe a URL: ")
n = int(input("informe o número de comentários: "))

# complete com seus dados
bot1 = Instagram('seu_user','sua_senha',url,n)
bot1.login()
