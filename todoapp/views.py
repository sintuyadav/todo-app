from asyncio import tasks
from webbrowser import get
from django.shortcuts import render,redirect,get_object_or_404
from .forms import todo
from .models import Mytodo
# Create your views here.
def alltodos(request):
    if request.method == 'POST':
        form_data = todo(request.POST)
        if form_data.is_valid():
            post_data = form_data.save()
            return redirect('t_list')
    else:
         form_data = todo()
    
    return render(request,'index.html',{'form_data':form_data})

def t_list(request):
    d=Mytodo.objects.all().order_by('-id')
    return render(request,"list.html",{"d":d})



def post_delete(request,pk):
    post = get_object_or_404(Mytodo,pk=pk)
    post.delete()
    return redirect('t_list')


# def update(request, pk):                                         
#     data = get_object_or_404(Mytodo, pk=pk)
    
    
#     form = todo(instance=data)                                                               

#     if request.method == "POST":
#         form = todo(request.POST)
#         if form.is_valid():
    #         form.save()
    
    #         return redirect ('t_list')
    # # context = {
    # #     "form":form
    # # }
    # return render(request, 'index.html', {'form':form})


# def update(request,pk):
#      todo = get_object_or_404(Mytodo,pk=pk)
#      form = todo(instance=todo)
#      if request.method == 'POST':
#          form = todo(request.POST,instance=todo)
#          if form.is_valid():
#             form.save()
#             return redirect ('t_list')

            
#      return render(request,'index.html',{'todo':todo,'form':form })



def update(request,pk):
    post = get_object_or_404(Mytodo,pk=pk)
    post.status='complete'
    post.save()
    return redirect('t_list')