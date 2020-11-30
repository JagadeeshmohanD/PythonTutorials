def print_names(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs["address"])

print_names(name="jags",address="Bengaluru",Ph=123,area="Nagar")

def hello_world(fname,*args,**kwargs):
    print(fname)
    print(args)
    print(kwargs)

hello_world(10,20,30,name="python",country="India")