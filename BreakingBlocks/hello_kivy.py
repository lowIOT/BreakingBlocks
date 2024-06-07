import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        # ラベルの作成
        label = Label(text="Hello, Kivy!",
                      font_size=24,
                      color=(0.7, 0.2, 0.3, 1))

        # レイアウトの作成
        box_layout = BoxLayout(orientation='vertical',
                                padding=10)
        box_layout.add_widget(label)

        # アプリケーションのルートウィジェットを返す
        return box_layout

if __name__ == "__main__":
    MyApp().run()