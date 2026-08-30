from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import csv
import os


class DataEntryApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        layout.add_widget(Label(
            text="DATA ENTRY APP",
            font_size=28
        ))

        self.name = TextInput(
            hint_text="Enter Name",
            multiline=False
        )
        layout.add_widget(self.name)

        self.phone = TextInput(
            hint_text="Enter Phone Number",
            multiline=False,
            input_filter="int"
        )
        layout.add_widget(self.phone)

        self.data = TextInput(
            hint_text="Enter Data",
            multiline=True
        )
        layout.add_widget(self.data)

        save_button = Button(
            text="SAVE",
            size_hint_y=None,
            height=55
        )
        save_button.bind(on_press=self.save_data)
        layout.add_widget(save_button)

        clear_button = Button(
            text="CLEAR",
            size_hint_y=None,
            height=55
        )
        clear_button.bind(on_press=self.clear_data)
        layout.add_widget(clear_button)

        return layout

    def save_data(self, instance):
        name = self.name.text.strip()
        phone = self.phone.text.strip()
        data = self.data.text.strip()

        if not name or not phone or not data:
            self.show_popup(
                "Error",
                "Please fill all fields."
            )
            return

        file_path = os.path.join(
            self.user_data_dir,
            "data.csv"
        )

        file_exists = os.path.exists(file_path)

        with open(
            file_path,
            "a",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    ["Name", "Phone", "Data"]
                )

            writer.writerow(
                [name, phone, data]
            )

        self.show_popup(
            "Success",
            "Data saved successfully!"
        )

        self.clear_data(None)

    def clear_data(self, instance):
        self.name.text = ""
        self.phone.text = ""
        self.data.text = ""

    def show_popup(self, title, message):
        Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.8, 0.3)
        ).open()


if __name__ == "__main__":
    DataEntryApp().run()