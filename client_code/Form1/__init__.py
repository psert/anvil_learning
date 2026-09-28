from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)

  @handle("submit_button", "click")
  def submit_button_click(self, **event_args):
    name = self.name_box.text
    email = self.email_box.text
    feedback = self.feedback_box.text
    like = self.dropdown_box.selected_value
    anvil.server.call('add_feedback', name, email, feedback, like)
    Notification("Feedback submitted!").show()
    self.clear_inputs()
    
  def clear_inputs(self):
    # Clear our three text boxes
    self.name_box.text = ""
    self.email_box.text = ""
    self.feedback_box.text = ""
    self.dropdown_box.selected_value=""