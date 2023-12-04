number = input()

mod_by_3 , mod_by_11 = 0 , 0 
for e in number :
    mod_by_3 = (mod_by_3 * 10 + int(e)) % 3
    mod_by_11 = (mod_by_11 * 10 + int(e)) % 11

print(f"{mod_by_3} {mod_by_11}")


""" 

   input = 11 
   first round 
   mod_by_3 = ( 0 * 10 + 1)  % 3   :=> 1
   mod_by_11 = ( 0 * 10 + 1) % 11 :=> 1

   sec round 
   mod_by_3 = ( 1 * 10 + 1 ) % 3  :=> 2
   mod_by_11 = ( 1 * 10 + 1 ) % 11 :=> 0


"""