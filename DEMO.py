import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from tkinter import ttk
# from Classes import a, b, c, d, a1, b1, c1

def setup_driver():
    os.environ["PATH"] += r"C:/SeleniumDrivers"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return webdriver.Chrome(options=options)


def get_news():
    driver = setup_driver()
    driver.get("https://nova.bg/")
    driver.maximize_window()
    print("-------------------------------")

    try:
        time.sleep(1)
        cookie = driver.find_element(By.CLASS_NAME, "fc-button-label")
        cookie.click()
        print("Cookies have been accepted.---Nova")
    except NoSuchElementException:
        print("Cookies close button not found.---Nova")

    try:
        time.sleep(1)
        ad = driver.find_element(By.CLASS_NAME, "ad-TransitionClose")
        ad.click()
        print("First Ad has been closed.")
    except NoSuchElementException:
        print("First Ad close button not found.")

    news_element = driver.find_element(By.CLASS_NAME, "title gtm-TopNewsSecond-click")
    news_element.click()
    news = news_element.text
    print("Just clicked The Top News.")
    print("\n" + "The News are:", news, "\n")
    news_element.click()

    try:
        ad1 = driver.find_element(By.CLASS_NAME, "ad-TransitionClose")
        ad1.click()
        print("Second Ad has been closed.")
    except NoSuchElementException:
        print("Second Ad close button not found.")

    try:
        time.sleep(1)
        element1 = driver.find_element(By.CLASS_NAME, d)
        driver.execute_script("arguments[0].scrollIntoView();", element1)
        print("It is scrolled into the object.")
    except NoSuchElementException:
        print("It wasn't scrolled down there!")

    messagebox.showinfo("Top News", f"The Top News is: {news}")
    
    driver.quit()
    root.quit()


def get_bitcoin_price():
    driver = setup_driver()
    driver.get("https://www.google.com")

    try:
        cookie1 = driver.find_element(By.CLASS_NAME, a1)
        cookie1.click()
        print("Cookies have been accepted.---Google")
    except NoSuchElementException:
        print("Cookies close button not found.---Google")

    search_bar = driver.find_element(By.CLASS_NAME, b1)
    search_bar.click()
    search_bar.send_keys("Bitcoin Live Price")
    search_bar.send_keys(Keys.RETURN)
    print("Just searched for Bitcoin Live Price.")

    time.sleep(2)
    
    bitcoin_price_element = driver.find_element(By.CLASS_NAME, c1)
    bitcoin_price = bitcoin_price_element.text
    print("\nBitcoin Live Price is:", bitcoin_price,"BGN\n")
    
    messagebox.showinfo("Bitcoin Price", f"Bitcoin Live Price is: {bitcoin_price} BGN")

    driver.quit()
    root.quit()

root = tk.Tk()
root.title("Bitcoin & News Fetcher")
root.geometry("500x300")

try:
    background_image = Image.open("matrix.jpg")
    background_image = background_image.resize((500, 300), Image.Resampling.LANCZOS)
    background_image_tk = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_image_tk)
    background_label.place(relwidth=1, relheight=1)
except IOError:
    print("Background image file not found. Ensure 'matrix.jpg' exists.")

btn_style = {'bg': '#4CAF50', 'fg': 'black', 'font': ('Lobster', 13, 'bold'), 'width': 30, 'height': 2}
btn_bitcoin = tk.Button(root, text="Get Bitcoin Price", command=get_bitcoin_price, **btn_style)
btn_news = tk.Button(root, text="Get Top News", command=get_news, **btn_style)
btn_bitcoin.pack(pady=20)
btn_news.pack(pady=20)

root.mainloop()

print("The program has ended.")