import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline

#lyrics of the songs
lyrics = "Ah, Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann Oh Barbara Ann Take My Hand Barbara Ann You Got Me Rockin' And A-Rollin' Rockin' And A-Reelin' Barbara Ann Ba Ba Ba Barbara Ann  Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann"
#get all words of song
list_of_words=lyrics.split(' ')
print('No of words: '+str(len(list_of_words)))
#normal_set = set(["a", "b","c"])
#unique_words=set()
unique_words=set(list_of_words)
print ('No of unique words: '+ str(len(unique_words)))

#making a dictionary for count
dicto={}
for i in unique_words:
    dicto.update({i:list_of_words.count(i)})

print (dicto)

x=list(unique_words)
y=list(dicto.values())
print (x,len(x))
print (y,len(y))

plotly.offline.plot({
"data": [
    plotly.graph_objs.Bar(x=list(unique_words),y=list(dicto.values()))
]
})




print ('Finito!')