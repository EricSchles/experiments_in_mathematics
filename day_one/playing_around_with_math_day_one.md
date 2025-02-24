Playing_around_with_math_day_one

This morning I didn't watch tv, not really.  This morning I sat with myself.  And lived in my head.  I lived with myself.  And you know what?  It wasn't that bad. The noise wasn't as loud inside my head.  And I actually enjoyed it for the first time in a long time.  I thought about mathematics and art and I realized something really deep:

3,4,5 triangles are related to squares.  We can figure out all the triangles with 90 degrees just by observing these simple patterns.  

So 

3^2 + 4^2 = 5^2

What are some others?

Let's make a program to find them for us!

```python
import math
import json

triplets = []
for i in range(1, 1000):
    for j in range(1, 1000):
        result = i**2 + j**2
        result_square_root = math.sqrt(result)
        if int(result_square_root) == result_square_root:
            triplets.append(
                (i,j,result_square_root)
            )
    
triplets = list(set(triplets))
json.dump(triplets, open("triplets.json", "w"))
```

Using this program we can see that there are 2068 triplets in the first 1000 numbers!  That's way more than I would have expected.  That means a triangle lengths of any of these triples will have a right angle.  This is mathematics, in a nutshell.  It's taking an idea from the world, mapping it to the numbers, exploring with the numbers and then mapping it back to the world.  That's how you apply mathematics.

So you might be asking - how do triangles apply to the real world?  Well!  Distances for one, construction for another, especially right angle triangles.  Literally anything.  Mapping visual structure to numerical structure is what allows us to apply mathematics.  This shows us our overall structure of thinking about mathematics - 

The original domain - the visual space
The numerical domain - the "mathematical" space
The maps between the two domains.

This is all mathematics is.  Again and again and again.  It's not bigger than this.  And it's not smaller.  It's just this.
