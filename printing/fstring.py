name = 'Cisco'
adverb = 'really'
ip = '192.168.10.2'
octets = ip.split('.')

#fstring
print(f'I {adverb} like {name}')
#C-Style
print('I %s like %s' %(adverb, name))
#format string
print('I {0} like {1}'.format(adverb, name))

i = 1
print('fString octets:')
for octet in octets:
    print(f'fString octet {i}: {octet}')
    i+=1
print('')
print(".format style octets:")
i = 1
for octet in octets:
    print('.format octet {0}: {1}'.format(i, octet))
    i+=1
print('')
print("C-Style octets:")
i = 1
for octet in octets:
    print("C-Style octets %i: %s" %(i, octet))
    i+=1



