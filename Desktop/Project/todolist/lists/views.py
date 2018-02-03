from django.shortcuts import render,get_object_or_404
from .models import todolist
from .form import todoform

def home(request):
	qs=todolist.objects.all()
	number=qs.count()
	context={"query":qs,"no":number}
	return render(request,"index.html",context)

def add(request):
	form = todoform(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=True)
		instance.save()

	
	context={"form":form}
	return render(request,"add.html",context)
# Create your views here.

