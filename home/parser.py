a = """
"""

b = """
<link rel="stylesheet" href="{% static 'new/assets/css/normalize.css' %}">
"""
count = 0


a = a.replace('href="', """href="{% static '""")
a = a.replace(""".css">""", """.css' %}">""")
a = a.replace('src="', """src="{% static '""")
a = a.replace(""".js">""", """.js' %}">""")
a = a.replace(""".jpg">""", """.jpg' %}">""")
a = a.replace(""".png">""", """.png' %}">""")

a = a.replace(""".jpg""", """ .jpg' %}""")
a = a.replace(""".png""", """ .png' %}""")

a = a.replace(""".html""", """ ' %}""")
#a = a.replace('<a href="{% static', '<a href="{% url')

print(a)
