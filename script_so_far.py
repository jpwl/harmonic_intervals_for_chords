def get_distance(n1, n2):
    return abs(n1-n2)
    
def determine_interval(distance):
    return distance_dic.get(distance, 'unknown')

def find_interval(n1, n2):
    d = get_distance(n1, n2)
    return determine_interval(d)

def cycle_through(fam, version): # get interval
    b = 2
    if version == 'notes':
        b = 1
    # cycle through 
    familyWH_total = []
    for family in fam:
        familyWH = []
        for i in range(len(family)-2):
            z = i % len(family)
            k = (i + b) % len(family)
            x = find_interval(family[z], family[k])
            familyWH.append(x)
        familyWH_total.append(familyWH)

    return familyWH_total

def collect_tetras(steps, version): # get modes
    tetras_total = []
    for scale in steps:
        for i in range(len(scale)):
            a = i
            b = (i+1) % len(scale)
            c = (i+2) % len(scale)
            if version == 'chords':
                d = (i+3) % len(scale)
                tetra = [scale[a], scale[b], scale[c], scale[d]]
            if version == 'notes':
                tetra = [scale[a], scale[b], scale[c]]
            tetras_total.append(tetra)
    return tetras_total

def deduplicate_tetras(tetras):
    # make set to remove dupes
        tet_set = set()
        for t in tetras:
            test = ''.join(t)
            if test not in tet_set:
                tet_set.add(test)
        col_tet = []
        for t in tet_set:
            l = ', '.join(t[i:i+2] for i in range(0, len(t), 2))
            col_tet.append([l])
        return col_tet

    
def tetra_me_bro(families, version, style):
    collated_steps = cycle_through(families, version)
    collected_tetras = collect_tetras(collated_steps, version) 
    if style == 'dictionary':
        return collected_tetras
    if style == 'unique':
        return deduplicate_tetras(collected_tetras)    
        
def collate_notes_to_chords(notes, chords):
    return_set = {}
    for i in range(len(notes)):
        if len(chords[i]) == 4:
            n = ''.join(notes[i])
            if not return_set.get(n):
                return_set[n] = [chords[i]]
            if return_set.get(n):
                return_set[n].append(chords[i])
    return return_set

def deduplicate_note_chord_dictionary(dictionary):
    copied = {}
    for key in dictionary:
        tetons = dictionary.get(key)
        reduced_tetons = deduplicate_tetras(tetons)
        copied[key] = reduced_tetons
    return copied

def deduplicate_chord_note_dictionary(dictionary):
    # inverse of deduplicate_note_chord_dictionary
    pass

interval_tetras = tetra_me_bro(families, 'notes', 'dictionary') #'unique'
chord_tetras = tetra_me_bro(families, 'chords', 'dictionary')
collated_notes_chords = collate_notes_to_chords(interval_tetras, chord_tetras)
bop = deduplicate_note_chord_dictionary(collated_notes_chords)

bop
