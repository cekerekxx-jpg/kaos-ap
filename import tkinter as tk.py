import flet as ft
import random

def main(page: ft.Page):
    page.title = "Kaos Uygulaması"
    page.bgcolor = "black"

    def kaos_baslat(e):
        # 10 adet hata mesajı oluştur
        for i in range(10):
            # Kapatma fonksiyonu
            def kapat_fonksiyonu(e):
                e.control.parent.controls[0].value = "Pencere Kapatıldı"
                e.control.parent.controls[0].color = "green"
                e.control.visible = False # Kapat butonunu gizle
                page.update()

            mesaj = ft.Text(f"HATA {random.randint(1000, 9999)}!", color="red", size=20)
            kapat_btn = ft.ElevatedButton("Kapat", on_click=kapat_fonksiyonu)
            
            # Mesajı ve butonu yan yana koy
            satir = ft.Row(controls=[mesaj, kapat_btn])
            page.add(satir)
        
        page.update()

    page.add(ft.ElevatedButton("KAOSU BAŞLAT", on_click=kaos_baslat))

ft.app(target=main)