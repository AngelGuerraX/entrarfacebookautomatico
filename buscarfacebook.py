from selenium import webdriver
import time

# Inicializar el navegador
driver = webdriver.Chrome()  # Asegúrate de tener el driver de Chrome instalado y en el PATH

# Abrir la página de inicio de sesión
driver.get("https://www.facebook.com/")

# Encontrar los campos de correo electrónico y contraseña e ingresar datos
email_field = driver.find_element_by_id("email")
email_field.send_keys("angelguerra@hotmail.com")

password_field = driver.find_element_by_id("pass")
password_field.send_keys("micontrasena")

# Hacer clic en el botón de inicio de sesión
login_button = driver.find_element_by_id("u_0_9_n4")
login_button.click()

# Esperar un momento para ver el resultado
time.sleep(5)

# Tomar una captura de pantalla del resultado de la prueba
driver.save_screenshot("resultado_facebook.png")

# Crear un archivo de texto para el reporte
with open("reporte_facebook.txt", "w") as report_file:
    # Verificar si se pudo iniciar sesión
    if "facebook.com" in driver.current_url:
        report_file.write("El inicio de sesión ha fallado.")
    else:
        report_file.write("El inicio de sesión ha sido exitoso.")

# Cerrar el navegador al finalizar la prueba
driver.quit()
