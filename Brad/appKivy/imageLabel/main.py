from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        img = AsyncImage(source = 'jeff.png', 
                        size_hint = (1, .5),
                        pos_hint = { 'center_x': .5, 'center_y': .5 })
        return img
    
if __name__ == '__main__':
    app = MainApp()
    app.run()


# from kivy.uix.image import AsyncImage
# class MainApp(App):
#     def build(self):
#         label = Label(text = 'Leonardo Oliveira Santos',
#                       size_hint = (5, .5),
#                       pos_hint = { 'center_x': .5, 'center_y': .5 })
#         return label