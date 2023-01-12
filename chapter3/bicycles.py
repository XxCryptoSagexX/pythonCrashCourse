bicycles = ['trek', 'cannondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[2])
print(bicycles[3])

# INDEX -1  acts as the last position in list. This is due to there being situations where you do not know how many are in list but you need the last one.

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

