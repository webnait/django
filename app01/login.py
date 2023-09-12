import select

from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from django import forms
from io import BytesIO
from app01.utils.code import check_code


class loginform(forms.Form):
    username = forms.CharField(label='用户名',widget=forms.TextInput(attrs={'class':'form-control'}),)
    password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'class':'form-control'},render_value=True))
    # code = forms.CharField(label='验证码',widget=forms.TextInput(attrs={'class':'form-control'}))
def login(request):
    if request.method == 'GET':
        form = loginform()
        # models.Admin.objects.create(username=123456,password=123456)
        return render(request,'login.html',{'form':form})
    form = loginform(data=request.POST)
    if form.is_valid():

        # input_code = form.cleaned_data.pop('code')
        # code = request.session.get('image_code','')
        # if code.upper() !=
        obj = models.Admin.objects.filter(**form.cleaned_data).first()

        if not obj:
            form.add_error('password','用户名或密码错误')
            return render(request, 'login.html', {'form': form})
        request.session['info'] = {'id':obj.id,'username':obj.username}
        return redirect('/user/list/')
    return render(request,'login.html',{'form':form})

def logout(request):
    request.session.clear()
    return redirect('/login')

# def image_code(request):
#     img,code_string = check_code()
#     request.session['image_code'] = code_string
#     request.session.set_expiry(60)
#     stream = BytesIO()
#     img.save(stream,'png')
#     return HttpResponse(stream.getvalue())
