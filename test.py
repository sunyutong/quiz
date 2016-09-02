import base64
print(base64.b64decode('JCRxQnY9bXt2XnsyfVxvdmVyIHJ9JCQl'))

#b'$$qBv=m{v^{2}\\over r}$$%'
print(base64.b64decode('JCR7IDJ9XERlbHRhIHQkJCU='))
#b'$$\{ 2\}\\\\Delta t$$%'

a='mamamama[imgslsdfjksdlk/img]'
print(a)
b=a.replace('ma','haha')
c=b.replace('/img]','/img>')
print(c)