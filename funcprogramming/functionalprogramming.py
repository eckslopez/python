#import socket
#from typing import Any

#class Resolver:
#    def __init__(self):
#        self._cache = {}

#    def __call__(self, host):
#        if host not in self._cache:
#            self._cache[host] = socket.gethostbyname(host)
#        return self._cache[host]

#    def clear(self):
#        self._cache.clear()

#    def has_host(self, host):
#        return host in self._cache 

#def sequence_class(immutable):
#    return tuple if immutable else list
#seq = sequence_class(immutable=True)
#t = seq("Timbuktu")
#print(t)
#print(type(t))

#scientists = ['Marie Curie','Albert Einstein','Rosalind Franklin',
#              'Neils Bohr','Dian Fossey','Isaac Newton',
#              'Grace Hopper','Charles Darwin','Lise Meitner']

#print(sorted(scientists, key=lambda name: name.split()[-1]))

#def hypervolume(*args):
#    print(args)
#    print(type(args))

#hypervolume(3,4)
#hypervolume(3,4,5)

#def hypervolume(length, *lengths):
#    v = length
#    for item in lengths:
#        v *= item
#    return v

#print(hypervolume(2,4))
#print(hypervolume(2,4,6))
#print(hypervolume(2,4,6,8))
#print(hypervolume())

#def tag(name, **kwargs):
#    print(name)
#    print(kwargs)
#    print(type(kwargs))

#tag('img', src="Monet.jpg", alt="Sunrise by Claude Monet", border=1)

#def tag(name, **attributes):
#    result = '<' + name
#    for key, value in attributes.items():
#        print(key)
#        result += ' {k}="{v}"'.format(k=key, v=str(value))
#    result += '>'
#    return result

#print(tag('img', src="Monet.jpg", alt="Sunrise by Claude Monet", border=1))

#a = {"First Base":"Steve Garvey","Second Base": "Harold Reynolds","Third Base":"Brooks Robinson"}
#for key, value in a.items():
#    print('{k}="{v}"'.format(k=key,v=str(value)))

#def sort_by_last_letter(strings):
#    def last_letter(s):
#        return s[-1]
#    return sorted(strings, key=last_letter)
#print(sort_by_last_letter(['hello','from','a','local','function']))

# According to Core Python3: Functions and Functional Programming, on PluralSight,
# this should result in a new sort_by_last_letter instance It doesn't.
#def sort_by_last_letter(strings):
#    def last_letter(s):
#        return s[-1]
#    print(last_letter)
#    return sorted(strings, key=last_letter)
#print(sort_by_last_letter(['ghi','def','abc']))
#print(sort_by_last_letter(['ghi','def','abc']))
#print(sort_by_last_letter(['ghi','def','abc']))

# LEGB scoping ule for name lookups:
# 1. Local 2. Enclosing 3. Global 4. Built-in

#g = 'global'
#def outer(p='param'):
#    l = 'local'
#    def inner():
#        print(g,p,l)
#    inner()

#outer()

# Returning Local Functions (First Class Functions)
#def enclosing():
#    def local_func():
#        print('local_func')
#    return local_func

#lf = enclosing()
#lf()

# Closures
#def enclosing():
#    x = 'closed_over'
#    def local_func():
#        print(x)
#    return local_func
#lf = enclosing()
#lf()
#print(lf.__closure__)

# LEGB demo
#message = 'global'

#def enclosing():
#    message = 'enclosing'

#    def local():
#        message = 'local'
    
#    print('enclosing message:', message)
#    local()
#    print('enclosing message:', message)

#print('global message:', message)
#enclosing()
#print('global message:', message)

# LEGB demo
# This time use the 'global' keywork to 
# Introduce the global message binding into local()
# message = 'global'

#def enclosing():
#    message = 'enclosing'

#    def local():
#        global message
#        message = 'local'
    
#    print('enclosing message:', message)
#    local()
#    print('enclosing message:', message)

#print('global message:', message)
#enclosing()
#print('global message:', message)

# LEGB demo
# This time use the 'nonlocal' keyword to 
# make the function local() modify the binding of
# message created in the function enclosing()
# nonlocal searches the enclosing scopes from innermost to outermost 
# using the first match found
#message = 'global'

#def enclosing():
#    message = 'enclosing'

#    def local():
#        nonlocal message
#        message = 'local'
    
#    print('enclosing message:', message)
#    local()
#    print('enclosing message:', message)

#print('global message:', message)
#enclosing()
#print('global message:', message)

# A practical example of the use of nonlocal
#import time

#def make_timer():
#    last_called = None # Never
#    def elapsed():
#        nonlocal last_called
#        now = time.time()
#        if last_called is None:
#            last_called = now
#            return None
#        result = now - last_called
#        last_called = now
#        return result
#    return elapsed

#t = make_timer()

