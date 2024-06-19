Men = ['Utku', 'Hasan', 'Talha', 'Görkem']
Women = ['Nihal', 'Elif', 'Nur', 'Hilal']


Men_Pref = {  
    'Utku':   ['Nihal', 'Elif', 'Nur', 'Hilal'],
    'Hasan': ['Elif', 'Hilal', 'Nihal', 'Nur'],
    'Talha':  ['Nur', 'Elif', 'Nihal', 'Hilal'],
    'Görkem':  ['Nur', 'Elif', 'Hilal', 'Nihal']
}

Women_Pref = {  
    'Nihal':  ['Utku', 'Talha', 'Görkem', 'Hasan'],
    'Elif':  ['Utku', 'Hasan', 'Görkem', 'Talha'],
    'Nur':  ['Talha', 'Görkem', 'Utku', 'Hasan'],
    'Hilal':  ['Hasan', 'Görkem', 'Talha', 'Utku']
}
def main():
    Men_Free = list(Men)
    Women_Free = list(Women)

    
    Matches = {
        'Utku':  '',
        'Hasan': '',
        'Talha': '',
        'Görkem': ''
        }
    key_list = list(Matches.keys())

    

    while len(Men_Free) > 0:
        for man in key_list:
            for woman in Men_Pref[man]:
                if woman not in list(Matches.values()):
                    Matches[man] = woman
                    Men_Free.remove(man)
                    
                    break
                elif woman in list(Matches.values()):
                    current_suitor = list(Matches.keys())[list(Matches.values()).index(woman)]
                    w_list = Women_Pref.get(woman)
                    if w_list.index(man) < w_list.index(current_suitor):
                        Matches[man] = woman
                        Men_Free.remove(man)
                        Matches[current_suitor] = ''
                        Men_Free.append(current_suitor)
                        print('{} was earlier engaged to {} but now is engaged to {}! '.format(woman, current_suitor, man))

    print('\n ')
    print('                             Stable Matching Finished !              ')
    for man in Matches.keys():
        print('{} is engaged to {} !'.format(man, Matches[man]))


if __name__ == "__main__":
    main()

