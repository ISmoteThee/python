"""
Opens a Power Point file with 
format: slide with question / slide with answer 
and pulls a random selection of 
questions with matching answers

Does not account for title slides
run as "python shuffleSlides.py <file> <samplesize>
"""

from pptx import Presentation
from sys import argv
import random
import os

script, preso, samplesize = argv

# experimental from https://github.com/scanny/python-pptx/issues/67
def delete_slide(prs, slide):
    #Make dictionary with necessary information
    id_dict = { slide.id: [i, slide.rId] for i,slide in enumerate(prs.slides._sldIdLst) }
    slide_id = slide.slide_id
    prs.part.drop_rel(id_dict[slide_id][1])
    del prs.slides._sldIdLst[id_dict[slide_id][0]]

#copy file to ./copy.pptx
inprs = Presentation(preso)
inprs.save('copy.pptx')
prs = Presentation('copy.pptx')

#find the slide count
max = len(prs.slides)

sets = []
keepers = []
i = 0
# Generate question answer pairs (qa)
while i < max:
    sets.append([i,i+1])
    i+=2

#pull random set of qa pairs based on samplesize
qas = random.sample(sets, int(samplesize))

# Generate a list of slides to keep
for qa in qas:
    keepers.append(qa[0])
    keepers.append(qa[1])

keepers.sort()
#print(qas)
#print(keepers)
i = max - 1
while i >= 0:
    if i not in keepers:
        delete_slide(prs, prs.slides[i])
        i-=1
    else:
        #print(f'{i} is a keeper!')
        i-=1

#Save the new random set to 'shuffle.pptx'
prs.save('shuffle.pptx')
#Delete the copy of the input file
os.remove('copy.pptx')




