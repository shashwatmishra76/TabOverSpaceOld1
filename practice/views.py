from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'practice/index.html', {})

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

def classes(request):
    return render(request, 'practice/c/classes.html', {
    "subdomain": 2,
    })

def debugging(request):
    return render(request, 'practice/c/debugging.html', {
    "subdomain": 5,
    })

def inheritance(request):
    return render(request, 'practice/c/inheritance.html', {
    "subdomain": 4,
    })

def introduction(request):
    return render(request, 'practice/c/introduction.html', {
    "subdomain": 0,
    })

def stl(request):
    return render(request, 'practice/c/stl.html', {
    "subdomain": 3,
    })

def strings_cpp(request):
    return render(request, 'practice/c/strings.html', {
    "subdomain": 1,
    })

def advanced(request):
    return render(request, 'practice/java/advanced.html', {
    "subdomain": 0,
    })

def bignumber(request):
    return render(request, 'practice/java/bignumber.html', {
    "subdomain": 1,
    })

def data_structures_java(request):
    return render(request, 'practice/java/data_structures.html', {
    "subdomain": 2,
    })

def exception_handling(request):
    return render(request, 'practice/java/exception_handling.html', {
    "subdomain": 3,
    })

def introduction_java(request):
    return render(request, 'practice/java/introduction.html', {
    "subdomain": 4,
    })

def strings_java(request):
    return render(request, 'practice/java/strings.html', {
    "subdomain": 5,
    })

def classes_python(request):
    return render(request, 'practice/python/classes.html', {
    "subdomain": 0,
    })

def collections(request):
    return render(request, 'practice/python/collections.html', {
    "subdomain": 1,
    })

def debugging_python(request):
    return render(request, 'practice/python/debugging.html', {
    "subdomain": 2,
    })

def introduction_python(request):
    return render(request, 'practice/python/introduction.html', {
    "subdomain": 3,
    })

def itertools(request):
    return render(request, 'practice/python/itertools.html', {
    "subdomain": 4,
    })

def math(request):
    return render(request, 'practice/python/math.html', {
    "subdomain": 5,
    })

def numpy(request):
    return render(request, 'practice/python/numpy.html', {
    "subdomain": 6,
    })

def sets(request):
    return render(request, 'practice/python/sets.html', {
    "subdomain": 7,
    })

def strings_python(request):
    return render(request, 'practice/python/strings.html', {
    "subdomain": 8,
    })

def xml(request):
    return render(request, 'practice/python/xml.html', {
    "subdomain": 9,
    })

def advanced_ds(request):
    return render(request, 'practice/data_structures/advanced.html', {
    "subdomain": 0,
    })

def arrays(request):
    return render(request, 'practice/data_structures/arrays.html', {
    "subdomain": 1,
    })

def heap(request):
    return render(request, 'practice/data_structures/heap.html', {
    "subdomain": 2,
    })

def queues(request):
    return render(request, 'practice/data_structures/queues.html', {
    "subdomain": 3,
    })

def stacks(request):
    return render(request, 'practice/data_structures/stacks.html', {
    "subdomain": 4,
    })

def trees(request):
    return render(request, 'practice/data_structures/trees.html', {
    "subdomain": 5,
    })

def trie(request):
    return render(request, 'practice/data_structures/trie.html', {
    "subdomain": 6,
    })
