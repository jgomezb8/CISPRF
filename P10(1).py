def main():
    thetext = '''
       Python was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.    
        '''
    print(thetext)
    textlen=len(thetext)
    print('the lenght of the original text is-> ',(textlen))

    rmv1=thetext.strip()
    print('lenght of the text w/o spaces-> ',(len(rmv1)))

    cthe=rmv1.count('the')
    print("count of the word 'the' is-> ",(cthe))

    if rmv1.find('little'):
        print('found little')

    else:
        print('not found')

    if rmv1.find('titan'):
        print('titan found')

    else:
        print('titan not found')

    
    posapl= rmv1.find('appl')
    print('position of appl is-> ',(posapl))

    thetext2= rmv1.replace('Python','PYTHON')
    print(thetext2)
        

    


    
    

# ---------------------------------
#  put assignment statements here
# ---------------------------------

    return
main()
