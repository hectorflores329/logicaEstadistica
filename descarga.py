import pandas as pd
import shutil
import time
import glob
import os
import csv
import requests
import wget
import numpy as np
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def principal():
    descarga()

enlace = "https://regiones.ine.cl/arica-y-parinacota/estadisticas-regionales/economia/energia-y-medioambiente/generacion-y-distribucion-de-energia-electrica"

def getDriver(enlace):
    
    options = Options()
    options.log.level = "trace"
    options.add_argument("--headless")
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout("60")
    driver.get(enlace)
    
    return driver


def descarga():

    driver = getDriver(enlace)

    cuadro = driver.find_element_by_xpath("/html/body/form/div[3]/div[5]/div/div/div/div[1]/div/div/div/div[1]")
    cuadro.click()
    time.sleep(3)

    serie = driver.find_element_by_xpath("/html/body/form/div[3]/div[5]/div/div/div/div[2]/div/div/div/div[4]/div/div/div[2]")
    serie.click()
    time.sleep(3)

    archivo = driver.find_element_by_xpath("/html/body/form/div[3]/div[5]/div/div/div/div[3]/div/div/div/div/div[2]/a/span[2]")
    archivo.click()
    time.sleep(3)

    print("ARCHIVO DESCARGADO CORRECTAMENTE")

if __name__ == '__main__':
    principal()