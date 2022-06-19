import my_function_module
import my_class_module

print( my_function_module.gcd.__doc__ )


print(  my_function_module.gcd(100, 200)  )



x = my_class_module.Stack()

x.push( 10 )
x.push( 20 )

print(x.pop() )
print(x.pop() )
