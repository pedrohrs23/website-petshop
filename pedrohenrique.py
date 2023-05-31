from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
moedas = ["Dinar do Kuwait", "Dinar do Bahrein", "Rial de Omã", "Dinar da Jordânia", "Libra Esterlina", "Franco Suíço", "Euro", "Balboa panamenho", "Dólar bahamense", "Dólar americano", "Iene japonês (JPY)", "Yuan chinês (CNY)", "Dólar australiano (AUD)", "Dólar canadense (CAD)", "Dólar neozelandês (NZD)", "Dólar de Singapura (SGD)", "Coroa sueca (SEK)", "Coroa norueguesa (NOK)", "Coroa dinamarquesa (DKK)", "Rublo russo (RUB)", "Peso mexicano (MXN)", "Rand sul-africano (ZAR)", "Lira turca (TRY)", "Rupia indiana (INR)", "Real brasileiro (BRL)"]


for moeda in moedas:
    driver.get(f"https://www.google.com/search?q={moeda}&hoje")
    valor = driver.find_element(By.CLASS_NAME, "SwHCTb")
    print(f"1 {moeda} equivale a {valor.text} reais brasileiros")

driver.quit()