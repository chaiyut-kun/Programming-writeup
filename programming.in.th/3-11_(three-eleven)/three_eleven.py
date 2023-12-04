number = input()

mod_by_3 , mod_by_11 = 0 , 0 
for e in number :
    mod_by_3 = (mod_by_3 * 10 + int(e)) % 3;
    mod_by_11 = (mod_by_11 * 10 + int(e)) % 11;

print(f"{mod_by_3} {mod_by_11}")


