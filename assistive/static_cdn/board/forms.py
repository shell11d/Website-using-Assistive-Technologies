from django import forms

from .models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = [
            "title",
            "content",
            "image",
            "tags",
            "draft",
            "publish",
        ]



# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = [
#             "title",
#             "content",
#             "image",
#             "draft",
#             "publish",
#         ]


# our new form
