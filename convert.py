data = 'FEFEFEFE681022102687001111040417A0019901160000'

data = [i+j for i,j in zip(data[::2],data[1::2])]

holder = []

for i in data:

	i = int(i, 16)
	holder.append(i)

print holder