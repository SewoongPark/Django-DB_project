from django import forms
from .models import (
    User,
    Champion_rate,
    Champions,
    Champion_story,
    champion_tip,
    Champion_counter,
    champion_skill_name,
    champion_skill_img_text,
    Review,
    Comment,
)

# class UserForm(forms.ModelForm):
#   def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     self._widget_update()

#   class Meta:
#     model = User
#     fields = ["title", "content"]
#     widgets = {
#         'title': forms.TextInput(
#             attrs={
#                 'placeholder': "제목을 입력해주세요."
#             }
#         )
#     }

# def _widget_update(self):
#   for visible in self.visible_fields():
#       visible.field.widget.attrs['class'] = 'form-control'


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._widget_update()

    class Meta:
        model = Review
        fields = ["review"]
        widgets = {"title": forms.TextInput(attrs={"placeholder": "제목을 입력해주세요."})}

    def _widget_update(self):
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._widget_update()

    class Meta:
        model = Comment
        fields = ["content"]

    def _widget_update(self):
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
