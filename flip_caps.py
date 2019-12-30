import unittest



def flip_caps(caps):

    forward = []
    backward = []
    i = 0
    while i < len(caps):
        current_cap = caps[i]
        if current_cap == 'H':
            i += 1
            continue
        j = i
        while j < len(caps) and (caps[j] == current_cap):
            j += 1
        

        if current_cap == 'F':
            forward.append((i,j -1))
        else:
            backward.append((i,j -1))

        i = j
    

    smaller = forward if len(forward) <= len(backward) else backward

    
    for start,end in smaller:

        if start != end:
            print(f"People in positions {start} to {end}, please flip your caps!")
        else:
            print(f"Person in position {start}, please flip your cap!")
#        print(("People" if start != end else "Person") + (" in position" + ("s" if start != end else '')) + (f" {start}") + (f" to {end}" if start != end else "") + ((", please flip your cap") + ("s" if start != end else "")))
    

def flip_caps_one_pass(caps):
    
    if not caps:
        return

    first_cap = caps[0]
    flip = 'F' if first_cap == 'B' else 'B'
    
    i = 0
    while i < len(caps):
        if caps[i] == flip:
            start = i
            j = i
            while j < len(caps) and caps[j] == caps[i]:
                j += 1

            end = j -1
            if end != start:
                print(f"People in positions {start} to {end}, please flip your caps!")
            else:
                print(f"Person in position {start}, please flip your cap!")
            i = j
        else:
            i += 1


def run_length_decoding(s):
    i = 0     

    decoding = ''
    while i < len(s):
        if s[i].isdigit():
            j = i
            num = ''
            while j < len(s) and s[j].isdigit():
                num += s[j]
                j += 1
            
            decoding += s[j] * int(num)
            j += 1
            i = j
        else:
            decoding += s[i]
            i += 1
    
    return decoding

def run_length_encoding(s):


    i = 0
    encoding = ''
    while i < len(s):
        current = s[i] 
        j = i
        count = 0
        while j < len(s) and s[j] == current:
            count += 1
            j += 1
        i = j 
        encoding += f"{count if count > 1 else ''}{current}"


    return encoding
            


if __name__ == "__main__":
    
    
    class Test(unittest.TestCase):

        def setUp(self):
            self.sol = run_length_encoding
        
        def test_case_1(self):
            s = 'BWWWWWBWWWW'
            self.assertEqual(self.sol(s),'B5WB4W')
        
        def test_case_2(self):
            s = 'B'
            self.assertEqual(self.sol(s),'B')
        
        def test_case_3(self):
            s = ''
            self.assertEqual(self.sol(s),'')
    
    
#    unittest.main(verbosity=2)
    s = '12B'
    print(run_length_decoding(s))
    #s = '1B5W1B4W'
    #print(run_length_decoding(s))

