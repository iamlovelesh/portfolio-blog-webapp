from django.shortcuts import redirect,render
# from django.http import HttpResponse
from portfolioApp.forms import UserData
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
# def index(request):
#     return render(request,"portfolioApp/index.html")

def UserMessage(request):


    form=UserData()

    if request.method=="POST":
        form=UserData(request.POST)

        if form.is_valid():
            form.save(commit=True)
            messages.success(request,"Message Successfully Sent!")
            # return http.HttpResponseRedirect('portfolioApp/index.html')
            # return index(request)
            # form=UserData()
            return redirect(request.path_info)
            # return HttpResponseRedirect("")
            # return HttpResponseRedirect(self.request.path_info)
        else:
            form=UserData()
            print("Error!")


    return render(request,'portfolioApp/index.html',{'form':form})
