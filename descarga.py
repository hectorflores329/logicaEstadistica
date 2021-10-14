import pandas as pd
import shutil
import time
import glob
import os
import csv
import requests
import numpy as np
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def principal():
    getDriver(enlace)

enlace = "https://regiones.ine.cl/documentos/default-source/region-xv/estadisticas/generacion-y-distribucion-de-energia-electrica/cuadros-estadisticos/series-mensuales/series-mensuales-desde-2015-a-la-fecha.xlsx?sfvrsn=c19505b2_8"

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


if __name__ == '__main__':
    principal()