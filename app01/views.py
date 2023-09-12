import select

from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from django import forms
# Create your views here.
def depart_list(request):
    info = request.session.get('info')
    if not info:
        return redirect('/login')
    queryset = models.Department.objects.all()

    return render(request,'depart_list.html',{'queryset':queryset})

def depart_add(request):
    info = request.session.get('info')
    if not info:
        return redirect('/login')
    if request.method =='GET':
        return render(request,'depart_add.html')
    add_title = request.POST.get('title')
    models.Department.objects.create(title=add_title)

    return redirect('/depart/list')

def depart_delete(request):
    info = request.session.get('info')
    if not info:
        return redirect('/login')
    delete_nid = request.GET.get('nid')
    models.Department.objects.filter(id=delete_nid).delete()
    return redirect('/depart/list')
def depart_edit(request,nid):
    info = request.session.get('info')
    if not info:
        return redirect('/login')
    if request.method == 'GET':
        QuerySet = models.Department.objects.filter(id=nid)
        return render(request,'depart_edit.html',{'QuerySet':QuerySet})
    up_title = request.POST.get('up_title')
    # models.Department.objects.filter(id=nid).update(title=up_title,其他=123 )
    models.Department.objects.filter(id=nid).update(title=up_title)
    return redirect('/depart/list')
def user_list(request):

    info = request.session.get('info')
    if not info:
        return redirect('/login')

    queryset = models.UserInfo.objects.all()
    # for obj in queryset:
        # depart_id_title = models.Department.objects.filter(id=obj.depart_id).first().title
        # depart_id_title = obj.depart.title

    return render(request, 'user_list.html',{'queryset':queryset})

def user_add(request):
    info = request.session.get('info')
    if not info:
        return redirect('/login')
    if request.method =='GET':
        queryset = models.Department.objects.all()
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'queryset':queryset,
            'depart_list':models.Department.objects.all()


        }
        return render(request,'user_add.html',context)

    add_name = request.POST.get('name')
    add_pwd = request.POST.get('pwd')
    add_age = request.POST.get('age')
    add_gender = request.POST.get('gender')
    depart_id = request.POST.get('depart_id')
    models.UserInfo.objects.create(name=add_name,pwd=add_pwd,age=add_age,gender=add_gender,depart_id=depart_id)
    return redirect('/user/list')




class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name','pwd','age','account','gender','depart']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'pwd':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'account':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'depart':forms.Select(attrs={'class':'form-control'}),
        }
        # ==============================================================
        # def __int__(self,*args,**kwargs):
        #     super().__init__(*args,**kwargs)
        #     # 循环找到所有的插件，添加 'class':'form-control'
        #     for name,field in self.fields.items():
        #         field.widget.attrs = {'class':'form-control'}
def user_modeladd(request):
    info = request.session.get('info')
    if not info:
        return redirect('/login')
    form = UserModelForm()
    if request.method =='GET':
        queryset = models.Department.objects.all()
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'queryset':queryset,
            'depart_list':models.Department.objects.all()
        }
        return render(request,'user_modeladd.html',{'form':form})

    #用户提交post数据 逐一进行校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存数据
        # print(form.cleaned_data)
        form.save()
        return redirect('/user/list')
    #检验不合法，页面上显示错误信息
    return render(request,'user_modeladd.html',{'form':form})

def user_edit(request,nid):
    info = request.session.get('info')
    if not info:
        return redirect('/login')
    row_obj = models.UserInfo.objects.filter(id=nid).first()
    if request.method =='GET':
        form = UserModelForm(instance=row_obj)
        return render(request,'user_exit.html',{'form':form})

    form = UserModelForm(data=request.POST,instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/user/list')
    return render(request,'user_exit.html',{'form':form})

def user_delete(request,nid):
    info = request.session.get('info')
    if not info:
        return redirect('/login')
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list')
def pretty_list(request):
    info = request.session.get('info')
    if not info:
        return redirect('/login')
    queryset = models.PrettyNum.objects.all().order_by('-level')

    return render(request,'pretty_list.html',{'queryset':queryset})