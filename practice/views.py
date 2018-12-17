from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'practice/index.html', {})

def algorithms(request):
    return render(request, 'practice/algorithms.html', {})

def constructive_algorithms(request):
    return render(request, 'practice/algorithms/constructive_algorithms.html', {
    "subdomain": 9,
    })

def dynamic_programming(request):
    return render(request, 'practice/algorithms/dynamic_programming.html', {
    "subdomain": 7,
    })

def graph_theory(request):
    return render(request, 'practice/algorithms/graph_theory.html', {
    "subdomain": 5,
    })

def greedy(request):
    return render(request, 'practice/algorithms/greedy.html', {
    "subdomain": 6,
    })

def implementation(request):
    return render(request, 'practice/algorithms/implementation.html', {
    "subdomain": 1,
    })

def np_complete(request):
    return render(request, 'practice/algorithms/np_complete.html', {
    "subdomain": 10,
    })

def recursion(request):
    return render(request, 'practice/algorithms/recursion.html', {
    "subdomain": 8,
    })

def search(request):
    return render(request, 'practice/algorithms/search.html', {
    "subdomain": 4,
    })

def sorting(request):
    return render(request, 'practice/algorithms/sorting.html', {
    "subdomain": 3,
    })

def strings(request):
    return render(request, 'practice/algorithms/strings.html', {
    "subdomain": 2,
    })

def warmup(request):
    return render(request, 'practice/algorithms/warmup.html', {
    "subdomain": 0,
    })

def data_structures(request):
    return render(request, 'practice/data_structures.html', {})

def python(request):
    return render(request, 'practice/python.html', {})

def java(request):
    return render(request, 'practice/java.html', {})

def c(request):
    return render(request, 'practice/c.html', {})
