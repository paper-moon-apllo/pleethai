from django import forms


class RequestForm(forms.Form):
    name = forms.CharField(label='名前', required=False, widget=forms.TextInput(
        attrs={
            'placeholder': 'お名前（省略可）',
        }))
    mail1 = forms.EmailField(label='メールアドレス', required=False, widget=forms.EmailInput(
        attrs={
            'placeholder': 'メールアドレス（省略可）',
        }))
    mail2 = forms.EmailField(label='メールアドレス（確認用）', required=False, widget=forms.EmailInput(
        attrs={
            'placeholder': 'メールアドレス確認用（省略可）',
            'oncopy': 'return false',
            'onpaste': 'return false',
            'oncontextmenu': 'return false',
        }))
    content = forms.CharField(label='リクエスト内容', widget=forms.Textarea(
        attrs={
            'placeholder': '（例）ภาษาไทย（タイ語）が登録されていません。　「永遠に」ってタイ語でどう言いますか？　単語のお気に入り機能が欲しいです。',
        }))

    def clean(self):
        super().clean()
        cleaned_data = self.cleaned_data
        cd_mail1 = cleaned_data.get('mail1')
        cd_mail2 = cleaned_data.get('mail2')

        # mail address match check
        if cd_mail1 != cd_mail2:
            msg = "メールアドレスが確認用と一致しません。"
            self.add_error('mail1', msg)
