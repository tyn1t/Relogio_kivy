from kivy.app import App
from  kivy.clock import Clock
from datetime import datetime


class MainApp(App):
    def on_start(self):
        Clock.schedule_interval(self.update_label, 1)

    def update_label(self, *args):
        # Update my label
        self.time = datetime.now()
        self.T = self.time.strftime("%H:%M:%S")
        self.root.ids.counter.text = self.T
if __name__ == "__main__":
    MainApp().run()