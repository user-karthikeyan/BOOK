from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)

  def go_click(self, **event_args):
    books = anvil.server.call('recommend', self.BookName.text)

    if books:
      self.render_result(books)
      
  def render_result(self, books):
    self.image_1.source = books[0]['url']
    self.image_2.source = books[1]['url']
    self.image_3.source = books[2]['url']
    self.image_4.source = books[3]['url']
    self.image_5.source = books[4]['url']
    self.image_6.source = books[5]['url']
    self.title_1.content = books[0]['title']
    self.title_2.content = books[1]['title']
    self.title_3.content = books[2]['title']
    self.title_4.content = books[3]['title']
    self.title_5.content = books[4]['title']
    self.title_6.content = books[5]['title']
    self.Book_1.visible = True
    self.Book_2.visible = True
    self.Book_3.visible = True
    self.Book_4.visible = True
    self.Book_5.visible = True
    self.Book_6.visible = True
