import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.image import Image
import cv2
from cvzone.ClassificationModule import Classifier

# Initialize the classifier
classifier = Classifier("model/keras_model.h5", "model/labels.txt")

# Define class labels
class_labels = {
    0: "Cataract",
    1: "Diabetic Retinopathy",
    2: "Glaucoma",
    3: "Normal Eye"
}

class MainApp(App):
    def build(self):
        self.title = 'Eye Disease Classification'
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.file_chooser_popup = None  # Define file_chooser_popup attribute

        self.img_path_label = Label(text="Selected Image: None")
        self.layout.add_widget(self.img_path_label)

        select_button = Button(text="Select Image")
        select_button.bind(on_press=self.show_file_selection_dialog)
        self.layout.add_widget(select_button)

        self.image_display = Image()
        self.layout.add_widget(self.image_display)

        self.result_label = Label(text="Result: ")
        self.layout.add_widget(self.result_label)

        return self.layout

    def show_file_selection_dialog(self, instance):
        if self.file_chooser_popup is None:
            file_chooser = FileChooserListView()
            file_chooser.bind(selection=self.load_selected_image)
            self.file_chooser_popup = Popup(title="Select an image", content=file_chooser, size_hint=(0.9, 0.9))
        self.file_chooser_popup.open()

    def load_selected_image(self, chooser, selection):
        if selection:
            filepath = selection[0]
            self.img_path_label.text = f"Selected Image: {filepath}"
            self.display_image(filepath)
            self.perform_prediction(filepath)
            self.show_image_selected_popup()
            popup = chooser.parent
            if isinstance(popup, Popup):
                popup.dismiss()
        else:
            self.img_path_label.text = "Selected Image: None"
            self.result_label.text = "Result: "

    def display_image(self, filepath):
        self.image_display.source = filepath

    def perform_prediction(self, filepath):
        try:
            img = cv2.imread(filepath)
            predicted_values, _ = classifier.getPrediction(img)
            prediction_results = [(class_labels[i], predicted_values[i]) for i in range(len(predicted_values))]
            result_text = "\n".join([f"{label}: {value:.2f}" for label, value in prediction_results])
            self.result_label.text = f"Result:\n{result_text}"
        except Exception as e:
            self.result_label.text = f"An error occurred: {e}"

    def show_image_selected_popup(self):
        popup = Popup(title='Image Selected', content=Label(text='Your image is selected!'), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    MainApp().run()
