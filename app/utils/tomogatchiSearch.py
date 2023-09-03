from flask import request

tomogatchi = request.args.get('tomogatchi')
functionB = request.args.get('functionB')
functionC = request.args.get('functionC')
query = request.args.get('q')

print('Query:', query)
print('Tomogatchi:', tomogatchi)
print('FunctionB:', functionB)
print('FunctionC:', functionC)
