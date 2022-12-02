things_to_do = [
   '🚀 Build a meaningful product for everyone.',
   '⛰ Hike the Pacific Crest Trail.',
   '🏡 Build an A-frame house and raise some goats.',
   '🌏 Live somewhere in Asia for a year.',
   '🎸 Release an album.',
   '📝 Write a book.',
   '🏆 Reach 100k subscribers on YouTube.',
   '🚐 Road trip with the fam.',
   '🍳 Open a cozy diner upstate.',
   '👴🏻 Grow old with no regrets.'
]


for i in things_to_do:
    print(i)

things_to_do.insert(9, 'Codear en CODEXDEX') # El insert, si pones un número menor, te desplaza los siguientes
things_to_do.append('Appendeado') 

print('******************************************************')

for i in things_to_do:
    print(i)


print ('max: ', max(things_to_do))
print ('min: ', min(things_to_do))