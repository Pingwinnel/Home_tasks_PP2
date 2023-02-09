movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1task
def ibm(movie):
    x=input()
    p=False
    for i in movie:
        if i["name"]==x and i["imdb"]>=5.5:
            p=True
    print(p)
                 
          
#2task
def good_imdb(movie):
    j=1
    for i in movie:
        if i["imdb"]>5.5 :
            g="{}| {} | {} | {}"
            print(g.format(j,i["name"],i["imdb"],i["category"]),end='\n')   
            j+=1
            
#3task
def one_category(movie):
 x=input()
 for i in movie:
    if i["category"]==x :
     print(i["name"],end='\n')   

#4task
def avr_imdb(movie):
    sum_imdb=0
    for i in movie:
        sum_imdb=sum_imdb+float(i["imdb"])
    print(sum_imdb/len(movie))
    
#5task
def avr_imdb_catg(movie):
    sum_imdb=0
    j=0
    x=input()
    for i in movie:
        if x==i["category"]:    
         sum_imdb=sum_imdb+float(i["imdb"])
         j+=1
    print(sum_imdb/j)
    

