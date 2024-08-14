from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Configura el controlador de Selenium (asegúrate de que chromedriver esté en tu PATH)
driver = webdriver.Chrome()

# URL de la aplicación bancaria
url = 'url/de/mi/banco'

# Iniciar sesión en la aplicación bancaria
def iniciar_sesion(driver, usuario, contrasena):
    driver.get(url)
    time.sleep(2)  # Esperar a que la página cargue

    usuario_input = driver.find_element(By.ID, 'usuario')
    contrasena_input = driver.find_element(By.ID, 'contrasena')
    login_button = driver.find_element(By.ID, 'login')

    usuario_input.send_keys(usuario)
    contrasena_input.send_keys(contrasena)
    login_button.click()

# Navegar a la página de transacciones y obtener los datos
def obtener_transacciones(driver):
    # Esperar a que la página de transacciones cargue (ajusta esto según tu aplicación)
    time.sleep(5)

    # Extraer los datos de las transacciones (ajusta los selectores según tu aplicación)
    transacciones = []
    filas = driver.find_elements(By.CSS_SELECTOR, '.transaccion')

    for fila in filas:
        fecha = fila.find_element(By.CSS_SELECTOR, '.fecha').text
        monto = fila.find_element(By.CSS_SELECTOR, '.monto').text
        tipo = fila.find_element(By.CSS_SELECTOR, '.tipo').text
        transacciones.append({
            'Fecha': fecha,
            'Monto': float(monto.replace('$', '').replace(',', '')),
            'Tipo': tipo
        })

    return pd.DataFrame(transacciones)

# Función principal
def main():
    usuario = 'tu_usuario'
    contrasena = 'tu_contrasena'

    iniciar_sesion(driver, usuario, contrasena)
    transacciones = obtener_transacciones(driver)
    driver.quit()

    # Procesar los datos y calcular el balance (usando las funciones del script anterior)
    datos_procesados = procesar_datos(transacciones)
    balance = calcular_balance(datos_procesados)
    graficar_balance(balance)

if __name__ == '__main__':
    main()

