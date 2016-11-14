from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title

print("test")
<<<<<<< HEAD
for i in range(10):
    print(i)
=======
print("test2")
>>>>>>> 4c5bbc0ac304ce633ac61c649881f53669f7ba2d
