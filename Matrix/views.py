from django.shortcuts import render,HttpResponse
from . import matrix

# Create your views here.
def Matrix(request):
    if request.method == "POST":
        p=[]
        n=int(request.POST.get('matrix'))
        for i in range(n+1):
            p.append(int(request.POST.get(f'P{i}')))
        solution,m,s=matrix.main(n,p)
        p=[]
        return render(request,"Matrix/Matrix.html",{"solution":solution,"m":m,"s":s,'value':m[1][n]})
    return render(request,"Matrix/index.html")