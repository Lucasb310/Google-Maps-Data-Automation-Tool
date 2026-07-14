from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def buscar_contatos_santarem(profissao):
    chrome_options = Options()
    # options.add_argument("--headless") # Descomente para rodar sem abrir a janela
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    driver.get("https://www.google.com/maps")
    time.sleep(20)
    
    # Pesquisa o termo (Ex: 'Médicos em Santarém')
    search_box = driver.find_element(By.ID, "searchboxinput")
    search_box.send_keys(f"{profissao} em Santarém, PA")
    search_box.send_keys(Keys.ENTER)
    time.sleep(20)
    
    leads = []
    
    # Coleta os nomes e telefones (lógica simplificada de extração)
    results = driver.find_elements(By.CLASS_NAME, "hfpxzc") # Classe dos links de lugares
    
    for i in range(min(len(results), 20)): # Pega os 20 primeiros de cada busca
        try:
            results[i].click()
            time.sleep(20)
            
            nome = driver.find_element(By.TAG_NAME, "h1").text
            
            # Tenta pegar o telefone pelo ícone de telefone no Maps
            try:
                telefone = driver.find_element(By.XPATH, "//button[contains(@data-item-id, 'phone:tel')]").get_attribute("aria-label")
                telefone = telefone.replace("Telefone: ", "")
            except:
                telefone = "Não encontrado"
                
            leads.append({"Nome": nome, "Profissão": profissao, "Telefone": telefone})
            print(f"Extraído: {nome} - {telefone}")
            
        except Exception as e:
            continue
            
    driver.quit()
    return leads

# Executar para várias profissões
todas_profissoes = ["Médico", "Advogado", "Arquiteto", "Contador", "Engenheiro"]
lista_final = []

for p in todas_profissoes:
    print(f"Buscando {p}...")
    lista_final.extend(buscar_contatos_santarem(p))

# Salvar em Excel
df = pd.DataFrame(lista_final)
df.to_excel("contatos_reais_santarem.xlsx", index=False)
print("Sucesso! Arquivo 'contatos_reais_santarem.xlsx' gerado com números REAIS do Google.")