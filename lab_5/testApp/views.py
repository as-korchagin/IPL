from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from lab_4.librip.gens import gen_random


# Create your views here.
def function_view(request):
    return HttpResponse('Hello world')


class Homepage(View):
    def get(self, request):
        return render(request, 'base.html')


class NestedFields(View):
    def get(self, request):
        var_1 = 1
        var_2 = 2
        var_3 = '3'
        var_4 = 'Hello, Django'
        return render(request, 'nested_fields.html', {'vars': {
            'var_1': var_1,
            'var_2': var_2,
            'var_3': var_3,
            'var_4': var_4
        }})


class Conditions(View):
    def get(self, request):
        return render(request, 'conditions.html', {'args': {'first': 10, 'second': 11}})


class Cycles(View):
    def get(self, request):
        return render(request, 'cycles.html',
                      {'elements': list({'id': str(i),
                                         'info': 'Information about element with id = {}'.format(i)} for i in
                                        gen_random(0, 15, 5))})


class Variables(View):
    def get(self, request):
        var_1 = 'Hello, Django'
        return render(request, 'variables.html', {'var_1': var_1})


class CycleElement(View):
    def get(self, request, id):
        data = {
            'element': {
                'id': id,
                'info': "Information about element with id = {}".format(id)
            }
        }
        return render(request, 'cycle_element.html', data)
