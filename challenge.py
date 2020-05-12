list1 = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
list2 = []
list1.sort(key=lambda e: e[len(e) // 2])
for name in list1:
    print(name)
    
