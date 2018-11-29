def create_counter():
   mem = {}
   def counter():
       count = mem.get("count", 0)
       count += 1
       mem["count"] = count

       return count

   return counter

id_generator = create_counter();

ids = list()
ids.append(id_generator())
ids.append(id_generator())
ids.append(id_generator())

print(ids) # [1, 2, 3]
