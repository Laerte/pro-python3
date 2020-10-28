print('propython.com'.split('.'))
domain, tld = 'propython.com'.split('.')
print(f"{domain} {tld}")

try:
    domain, path = 'propython.com/example/url'.split('/')
except ValueError as e:
    print(e)
    domain, *path = 'propython.com/example/url'.split('/')
    print(f"{domain} {path}")
