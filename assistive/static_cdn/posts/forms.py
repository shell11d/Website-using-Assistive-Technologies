from django import forms

from .models import Post


# class BoardForm(forms.ModelForm):
#     class Meta:
#         model = Board
#         fields = [
#             "title",
#             "content",
#             "image",
#             "draft",
#             "publish",
#         ]



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "tags",
            "draft",
            "publish",
        ]


# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )