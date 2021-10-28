from selenium import webdriver
import os
import psycopg2
from time import sleep

class zapbot:
    # O local de execução do nosso script
    dir_path = os.getcwd()
    # O caminho do chromedriver
    chromedriver = os.path.join(dir_path, "chromedriver.exe")
    # Caminho onde será criada pasta profile
    profile = os.path.join(dir_path, "profile", "wpp")

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # Configurando a pasta profile, para mantermos os dados da seção
        self.options.add_argument(
            r"user-data-dir={}".format(self.profile))
        # Inicializa o webdriver
        self.driver = webdriver.Chrome(
            self.chromedriver, chrome_options=self.options)
        # Abre o whatsappweb
        self.driver.get("https://web.whatsapp.com/")
        # Aguarda alguns segundos para validação manual do QrCode
        self.driver.implicitly_wait(15)

    def ultima_msg(self):
        """ Captura a ultima mensagem da conversa """
        try:
            post = self.driver.find_elements_by_class_name("_3_7SH")
            ultimo = len(post) - 1
            # O texto da ultima mensagem
            texto = post[ultimo].find_element_by_css_selector(
                "span.selectable-text").text
            return texto
        except Exception as e:
            print("Erro ao ler msg, tentando novamente!")

    def envia_msg(self, msg):
        """ Envia uma mensagem para a conversa aberta """
        try:
            sleep(2)
            # Seleciona acaixa de mensagem
            self.caixa_de_mensagem = self.driver.find_element_by_class_name("_3uMse")
            # Digita a mensagem
            self.caixa_de_mensagem.send_keys(msg)
            sleep(1)
            # Seleciona botão enviar
            self.botao_enviar = self.driver.find_element_by_class_name("_1U1xa")
            # Envia msg
            self.botao_enviar.click()
            sleep(2)
        except Exception as e:
            print("Erro ao enviar msg", e)

    def envia_media(self, fileToSend):
        """ Envia media """
        try:
            # Clica no botão adicionar
            self.driver.find_element_by_css_selector("span[data-icon='clip']").click()
            # Seleciona input
            attach = self.driver.find_element_by_css_selector("input[type='file']")
            # Adiciona arquivo
            attach.send_keys(fileToSend)
            sleep(3)
            # Seleciona botão enviar
            send = self.driver.find_element_by_xpath("//div[contains(@class, '_3uMse')]")
            # Clica no botão enviar
            send.click()
        except Exception as e:
            print("Erro ao enviar media", e)

    def abre_conversa(self, contato):
        """ Abre a conversa com um contato especifico """
        try:
            # Seleciona a caixa de pesquisa de conversa
            self.caixa_de_pesquisa = self.driver.find_element_by_class_name("_2FVVk")
            # Digita o nome ou numero do contato
            self.caixa_de_pesquisa.send_keys(contato)
            sleep(4)
            # Seleciona o contato
            self.contato = self.driver.find_element_by_xpath("//span[@title = '{}']".format(contato))
            # Entra na conversa
            self.contato.click()
        except Exception as e:
            print("Erro ao abrir conversa", e)

def main():
    bot =zapbot()
    con = psycopg2.connect(
        host="192.168.223.228",
        port="5432",
        database="SSI",
        user="SSI",
        password="*****")
    con.isolation_level = None
    cur = con.cursor()
    sleep(15)
    while True:
        cur.execute("SELECT * from app_notificacoes where status = 'Não Lida' ")
        dados = cur.fetchall()
        try:
            print(dados)
            query = dados[0]
            print(query)
            idq = query[0]
            if query[6] == 'TI':
                bot.abre_conversa('Lucas TI')
                sleep(15)
            if query[6] == 'MAN_P':
                bot.abre_conversa('Bosco')
                sleep(15)
            if query[6] == 'MAN_A':
                bot.abre_conversa('Bosco')
                sleep(15)
            if query[6] == 'MAN_T':
                bot.abre_conversa('Bosco')
                sleep(15)
            bot.envia_msg(query[3])
            cur.execute("UPDATE app_notificacoes SET status='Enviado' WHERE id={};".format(idq))
            cur.execute("commit;")

        except Exception as e:
            print("Erro ao enviar media", e)


        sleep(30)

    con.close()

main()
