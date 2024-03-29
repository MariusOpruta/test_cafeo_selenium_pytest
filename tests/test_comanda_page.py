from time import sleep

from pages.home_page import HomePage
from pages.comanda_pages import ComandaNoua


def test_comanda_noua(browser):
    home_page = HomePage(browser)
    comanda = ComandaNoua(browser)
    home_page.load_page()
    comanda.click_select_brand()
    comanda.click_select_product()
    comanda.cantitate()
    comanda.click_cantitate(3)
    comanda.select_numar_bucati()
    comanda.click_adauga_cos()
    sleep(4)
    assert "Produsul a fost adăugat în coș" in comanda.get_mesaj_adaugat()
    comanda.click_buton_detalii_cos()
