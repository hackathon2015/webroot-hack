import matplotlib.pyplot as pyplot
 
x_list = [78, 75, 63, 56, 55, 50, 48, 47, 42, 36]
label_list = ['duke-energy', 'aol', 'dynegy', 'williams', 'calpine', 'mcnallytemple', 'marathon-com', 'calpx', 'gen', 'govadv']
 
pyplot.axis("equal")
pyplot.pie(
        x_list,
        labels=label_list,
        autopct="%1.1f%%"
        )
pyplot.title("Pastafarianism expenses")
pyplot.show()
