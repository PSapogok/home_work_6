set_name={'igor' , 'vany', 'pasha'}
set_read_books={'vlastik', 'hobbit', 'zona51'}
set_must_read={'vlastik', 'hobbit', 'garri_potter'}
all_book= {'vlastik', 'hobbit', 'garri_potter','zona51'}
bibl= {
    'vlastik':'igor',
    'hobbit':'vany',
    'zona51':'pasha'
}

def poisk_book():
    for i in bibl.keys():
        for j in set_must_read:
            if i == j:
                print(bibl.get(i))
                
          
      
poisk_book()
