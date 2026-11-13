Tree_circumfence = float(input('Enter tree circumfence in cm: '))
Tree_diameter = Tree_circumfence / 3.14
Tree_can_be_cut_down = (Tree_diameter >= 50)
print(f'Tree can be cut down: {Tree_can_be_cut_down}')