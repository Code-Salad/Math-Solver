from django.http.response import JsonResponse
from . forms import *
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.generic.edit import UpdateView,CreateView,DeleteView,FormView


import os
import sys
sys.argv=['']
del sys

import sys
import LatexOCR
# from LatexOCR import settings


sys.path.insert(1,'./LatexOCR/')
sys.path.append('/LatexOCR/')
# sys.path.append('./LatexOCR/')
# sys.path.insert(1,'./settings/')
from pix2tex import *


from sympy.parsing.latex import parse_latex
from sympy import * 

class upload(FormView):
    form_class = SumForm
    template_name = 'upload.html'
    success_url = '/'


# def home(request):
#     return render(request, 'upload.html')


def process_image(request):
    if request.method == 'POST':

        upload = request.FILES['sum_img']

        fs=FileSystemStorage()
        file=fs.save(upload.name,upload)
        fileurl = fs.url(file)
        
        fileurl=fileurl[1:]

        print('\n\n\n\n\n'+fileurl)
        
        
        x=latexocr(fileurl)

        print('\n\n\n\n\n'+x)
        
        expr = parse_latex(x)


        # x=x.strip
        x=simplify(expr)
        os.remove(fileurl)
        y=x.evalf( )
        
    
        print(y)

        # args['mytext'] = text
        return render(request, 'result.html',{'sum_result':y})


