from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class WhatsAppApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        self.bilgi_etiketi = Label(text="Bilgi:")
        kapat_butonu = Button(text="Kapat", on_press=self.kapat_fonksiyonu)
        ac_butonu = Button(text="Aç", on_press=self.ac_fonksiyonu)

        layout.add_widget(kapat_butonu)
        layout.add_widget(ac_butonu)
        layout.add_widget(self.bilgi_etiketi)

        return layout

    def kapat_fonksiyonu(self, instance):
        self.bilgi_etiketi.text = "Bilgi: WhatsApp bildirimleri kapalı."

    def ac_fonksiyonu(self, instance):
        self.bilgi_etiketi.text = "Bilgi: WhatsApp bildirimleri açık."

if __name__ == '__main__':
    WhatsAppApp().run()