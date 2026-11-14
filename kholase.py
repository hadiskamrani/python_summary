'''
In the name of god

autor : Hadis Kamrani

kholase

human ---> interface(zaban barname) ---> machine(binary)

baraye dashtane python
1-python kernel ---> ye motore python hast k miad tarjome mikone b binary
2-editor,IDE ---> mohiti k code minevisim ---> ersal code b python kernel ---> tarjome b binary ---> machine(laptop,ram,cpu) ---> javab migire
 ---> IDE/editor namayesh midahad

editor ha masalan vs code,sublime,cursor ---> faghat baray python nis baray hame zabani hast ---> tamame code ro run mikoni
IDE mesle spyder ---> na tanha ye editor dare balke chanta vijegi ham dare ---> hamzaman k code mizani erroreto neshoon mide ---> memory ziad dargir
baste b kari k darim az editor ya IDE estefade mikonim

anaconda ---> taghsim laptab b mohit hay mokhtalef ---> hal moshkel update ---> to har mohit(environment) y version az spyder,python...bashe

python, spyder , ... ---> se ta adad daran---> 3.9.6 ---> adad aval kheili moheme va taghiresh mese tabdil shodan b 
yek barname jadide, adad dovom taghir dar yek vijegiye, adad sevom hal yek bug ast (major,minor,patch)

zababn ensan bar paye 10 ---> 0,1,2,3,4,5,6,7,8,9 ---> 10,11,12,13,...
zaban binary bar paye 2 ---> 0,1 ---> 10,11,100,110,...

python b zaban ensan nazdik tare ---> yadgiri asan, sorate paein

kole spyder 4 bakhshe 
1- Tool balaye safhe ---> new file, save file, import file, run, run section, setting
2- editor ---> codeto minevsii
3- samte rast yek ghesmati , variables,plot , files , ...
4- Console --->  run miseh ,javabe run ro mide

library/package ---> dakhelesh hezaran class, function hast ---> shamel code hay 100 ta ... khat hast ---> ma bayad oon tabe ra seda bezanim

yadgiri library + use(estefade az an)

numpy --->  mohasebate riazi
scipy , sympy ---> differential,jabr
pandas ---> kar ba data ( csv,excell) ---> data scientist ---> data cleaning
matplotlib ---> rasm , mosaver sazi
sklearn(scikit-learn) ---> mohem tarin ketabkhane machine learning
tensorflow ---> google (deepmind) ---> deeplearning
pytorch ---> meta (facebook, insta) ---> deeplearning

library ha
1- version daran
2- b ham vabastegi daran (dependency)

run kardan b 2 sorate 
ya kole code ---> az bala b paeen chap b rast
ya ghesmati az code ---> bayad select konim oon ghesmato

# ---> yek khat   ya  '''  '''---> chand khat ---> ignore(sarfenazar)

nokte1
overwright ---> akharin meghdar gharar migire
a = 10 
a = 20
a barabar 20

nokte2
a = 10
b = 40
a = b ---> a khali mikone b (40) mirize toosh
b = a ---> b khali mikone a (10) mirize toosh

nokte3
aval zarf misazim bad operation anjam midim ---> c =  a + b

nokte4 
case sensetive ---> Print, PRINT ,print ba ham fargh daran

-----------------------------------------------------------------------------------------------------------------------------------

python se bakhshe :

1-python built in function (defined) ---> yek amalkardi daran ---> narenji ---> parantez daran ---> print(),type(),len()
vorodi k midi khoroji midan
ba kama mitooni vorodi haye mokhtalef b tabat bedi
bazi tavabe bayad ba ham etefagh bioftan

baray didan built in ha ---> dir(__builtins__)  
ya
import builtins
print(dir(builtins))

A

abs() ---> ghadre motlagh adad ra pas midahad(absolute) ---> abs(number) ---> abs(10)
aiter()
all()  ---> age hame maghadir True , True barmigardoone 
anext()
any() ---> age hadeaghal yeki az maghadir True bashe ,True barmigardoone
ascii()
'''
def check_email(email):
    shart1 = '@' in email
    shart2 = '.com' in email
    shart3 = ' ' not in email
    
    #har se ta shart bayad true bashe
    all_shart = [shart1,shart2,shart3]
    
    if all(all_shart):
        return True
    else:
        return False


'''
B

bin()
bool() ---> bool(0) ---> False   bazi vaghta data haii k baramoon miyad 0, 1 ast mikhaym tabdilesh konim b True va False k estefade konim
            bool(1) ---> True    masalan mojoodi website lavazem arayesh ---> mojood, 1 neshoon mide , mojood nis, 0 neshoon mide---> mikhaym ba True va False neshoon bedim
breakpoint()
bytearray()
bytes()

C

callable() ---> barresi mikonad aya yek object ghabele farakhani ya na
chr() ---> chr(65) ---> "A"
classmethod()
compile()
complex()

D

delattr()
dict()
dir() ---> baraye didan attribute ha va method ha yek object ---> baraye yadgiri python mofide
divmod()

E

enumerate() ---> baraye zamani k ham index ham value mikhahim

'''
names =["ali","reza"]
for i,name in enumerate(names):
    print(i,name)
'''
0 ali
1 reza

eval() ---> ye reshte ra b onvan expression python evaluate mikonad ---> nabayad vorodi nashenas karbar (input) b eval bedi

'''

x = eval("2 + 3")
print(x)  #5

'''
exec()

F

filter() ---> baray filter kardan dade ha

'''

numbers=[1,2,3,4,5,6,7,8]
result=filter(lambda x : x % 2 == 0 , numbers)
print(list(result))   #[2, 4, 6, 8]

'''

float()
format() 

'''
name ="ali" 
print(f"hello {name}")
#hello ali 

adad = format(100000,",")
print(adad)
#100,000

'''
 
frozenset()

G

getattr()
globals()

H

hasattr()
hash() ---> agar object ghabel hash bashad ---> baraye dict va set ahamiyat darad
help() ---> vaghti tabei motevajeh nemishim mizarim to help behemoon mige
hex()

I

id() ---> shenase yek object midahad

'''

x = 10
print(id(x))
#140729242580168

'''

input() ---> harchi benevisi be karbar neshoon mide va montazer mimone karbar chizi benevise , javab karbar khoroji
 mide mirize to zarf(khorooji b soorate string)
int()
isinstance() ---> barresi mikone ye shei az noe khasi hast ya na 

'''

x=10
print(isinstance(x,int))
#True

'''

issubclass()
iter() 

'''

numbers =[1,2,3,4]
iterator = iter(numbers)
print(next(iterator))   #1
print(next(iterator))   #2
print(next(iterator))   #3
print(next(iterator))   #4

'''
L

len() ---> object migire ---> dar javab tool b ma pas midahad ---> tedad ---> string , byte , tuple , list,
 range ya dictionary , set
 
list()
locals()

M

map() ---> emal yek function rooye tamam anasoor

'''

numbers=[1,2,3,4,5]
result=map(lambda x : x * 2 ,numbers)
print(list(result))
#[2, 4, 6, 8, 10]

'''

max() ---> bozorgtarin
memoryview()
min() ---> kochiktarin

N

next()

O

object() ---> payeye selsele marateb besiyari az class ha object ast
oct()
open() ---> baraye kar ba file ha

'''

with open("test.txt","r") as file:
    content=file.read()
    
'''

ord() ---> adad unicode

'''

ord("A") # 65

'''

P

pow() ---> tavan
print() ---> namayesh mide
property()

'''

print("ali","reza",sep="-")  #ali-reza
print("hello",end=" ")
print("world")
#helloworld
print("sara\n")
print("20")

'''
sara

20


R

range() --->  baraye toolid donbalei az adad estefade mishavad  ---> range(start,stop,step)
repr()
reversed() ---> makoos
round() ---> gerd kardan

S

set()
setattr()
slice()
sorted() ---> baray moratab sazi

'''

names=["ali","reza","sara"]
result= sorted(names,key=len)
print(result)

'''

staticmethod()
str()
sum()  ---> jam anasoor ---> bayad iterable bashad k sum estefade konim
super() 

T

tuple()
type() ---> type(noe) neshoon mide

V

vars()

Z

zip() ---> chand iterable ra ba ham jooft mikonad

'''

names =["ali", "reza"]
ages=[20,25]
for name,age in zip(names,ages):
    print(name,age)

'''
ali 20
reza 25


_
__import__()


int() , float() , complex() , string() , bool() ,list() ,tuple()---> khodeshoon tabe hesab mishan(tabe dakheli) ---> baraye casting
casting ---> tabdil type b type dige
5.8 ---> float ---> 5 ---> int

2-keywords (defined) ---> logic ya mantegh barname ra avaz koni ---> banafsh ---> if , elif , else , for , while , and ,
 or , not ,def , pass , continue , break , raise ,False, True , None , return , as , assert , async , await , case , class 
 , del , except , finally , from , global , is, in , lambda , match , nonlocal , try ,with , yield , match ---> har 
 keyword yek sakhtari dare

baray didan keyword ha:
import keyword
print(keyword.kwlist)

3-unknown ---> variable (undefined) ---> harchizi gheir az do ta ghabli ---> sefid ---> 1-numbers(int,float,complex) 2-string 3-boolian
 4-iterable(multi value in one variable)
esme zarf(variable) = meghdar(value)

variable
1-nabayad esme zarf az keyword ha ya python built in function ha bashad
2-faghat az charector _ mishavad estefade kard
3-az adad dar ebteday esme zarf nemishe estefade kard
4-case sensetive

dakhele zarf chiya mitoonim berizim:

3-1-numbers
operation( + , - , * , ** , / , = ) ---> dastor mide
4//6 ---> 0   4/6 ---> 0.6666
() > ** > *,/ > +,-   olaviat
comparition( < , > , =< , >= , == , != ) ---> soal miporse

3-2-string
listi az charactor ha
dakhele "",'' neshan dade mishavad
"ali"  "5"  ":"
'in the name of "god"'
str changable nist
name[index] ---> 0
name[start:end] ---> end exclude
tavabe string khoroji midan va emal nemikonan ---> upper(),lower(),capitale(),title(),strip() 
name.upper() ---> new_zarf = zarf.function()

se daste mishan tavabe string
3-2-1-convert ---> taghiri ijad mikonan ---> upper() , lower()
3-2-2- khoroji behet adad midan ---> count() , find()
3-2-3- is ---> yechizio check mikone behet true va false mide  ---> isalpha() , isdigit()

str methods

bytes and bytearray methods

Formatting

str.format()

str.format_map()

f-strings

printf-style String Formatting

printf-style Bytes Formatting


Searching and Replacing

str.find()  ---> peida kardan ---> indexesho neshoon mide ---> .find(a)  ---> adad pas mide ---> peida nakone adad -1 neshoon mide

str.rfind()

bytes.find()

bytes.rfind()

str.index()

str.rindex()

bytes.index()

bytes.rindex()

str.startswith()

bytes.startswith()

str.endswith()

bytes.endswith()

str.count() ---> beshmor a ro masalan ---> .count(a) ---> adad pas mide

bytes.count()

str.replace()  ---> jagozari mikone , vorodi migire , (old,new)  (" " , "") ---> vase hazf fasele bein ebarat ham b kar mire

bytes.replace()


Splitting and Joining

str.split() ---> y jomle darim listi az kalamat b ma tahvil midahad ---> barasas space masalan

str.rsplit()

bytes.split()

bytes.rsplit()

str.splitlines()

bytes.splitlines()

str.partition()

bytes.partition()

str.rpartition()

bytes.rpartition()

str.join()

bytes.join()


String Classification

str.isalpha() ---> horoof

bytes.isalpha()

str.isdecimal()

str.isdigit() ---> adad

bytes.isdigit()

str.isnumeric()

str.isalnum() ---> ya hamash bayad adad bashe ya horoof

bytes.isalnum()

str.isidentifier()

str.islower() ---> hamash kochak hast ?

bytes.islower()

str.isupper() ---> hamash bozorg hast ?

bytes.isupper()

str.istitle() ---> horof aval bozorg hast ?

bytes.istitle()

str.isspace()

bytes.isspace()

str.isprintable()


Case Manipulation

str.lower() ---> kochak mikonad ---> save koni information moshtari hato ---> normalization

bytes.lower()

str.upper() ---> bozorg mikonad 

bytes.upper()

str.casefold()

str.capitalize()  ---> harfe aval bozorg mikonad --->  namayesh bedi esmesho(karbar) (ATM)

bytes.capitalize()

str.title()  ---> harf aval har kalame ra bozorg mikonad ---> namayesh bedi esmesho(karbar) (ATM)

bytes.title()

str.swapcase()

bytes.swapcase()


Padding and Stripping

str.ljust()

str.rjust()

bytes.ljust()

bytes.rjust()

str.center() ---> bayad behesh y adad bedim masalan 20 ---> miyad to 20 character str ro ja mide ---> banana.center(20)

bytes.center()

str.expandtabs()

bytes.expandtabs()

str.strip() ---> space rast va chap ro hazf mikone,space bein ro hazf nemikone ---> vaghti vorodi az karbar miad

bytes.strip()

str.lstrip() ---> faghat space chap hazf kon

str.rstrip() ---> faghat space rast hazf kon

bytes.lstrip()

bytes.rstrip()

str.removeprefix()

bytes.removeprefix()

str.removesuffix()

bytes.removesuffix()


Translation and Encoding

str.translate()

bytes.translate()

str.maketrans()

bytes.maketrans()

str.encode()  

bytes.decode()


f string 
number = 43
print('shomaraye shoma hast :' , number , 'mamnoon')
doree oon chizi ke manzooresh harf nis, balke esme zarfe va mikhahi man meghdaresho jay gozari konm {}
print(f'shomareye shoma hast : {number}  mamnoon')

asssignment ---> vaghti mikhay str besazi

indexing

tamam value haye sequence ---> indexing shoodan dar ram 
az 0 shoro mishavand 

b shomarei k b har onsor datatype iterable ekhtesas dade mishavd index migooyand

dastresi b tak tak anasoor 

string ---> s= "ali" ---> print(s[0]) ---> a ---> chon string ha ghabel shomaresh hastand 

list ---> s = ["y" , "ali", 8 , True , [2, "67"] , 85] ---> print(s[1]) ---> ali 
                                                       ---> print(s[1][2]) ---> i
                                                       ---> print(s[4][1][1]) ---> 7
                                                       85 choon int va string nist nemishavad b 5 an dastresi peida kard 
                                                       True ---> bool ham nemishe b tak tak anasooresh dastresi dasht

tuple ---> a = (10,20,30,40) ---> print(a[2]) ---> 30


slicing

yek slice az ye datatype iterable mikham
[start:stop:step]
s = "python language" ---> print(s[0:5:2]) ---> pto
khode space ham index darad
start az hamoon index shoro mikonim vali stop bayad index yehi bishtar bashad

compony = "fanavari"
new = company[1] + compony[4] + compony[5]
print(new)    ---> ava

compony[:6] --->  az ebteda ta 6   compony[3:] ---> az 3 ta enteha   [:] ---> az ebteda ta enteha

--------------------------------------------------------------------------------------------------------------------

3-3-boolian (case sensetive)
True ---> meghdar dorost
False ---> meghdar nadorost

---------------------------------------------------------------------------------------------------------------------

None ---> nabood meghdar ---> type(None) , None ast

---------------------------------------------------------------------------------------------------------------------

out ---> vaghti khoroji ba out ghermez neshoon dade mishavad 
aksare tabe ha khoroji daran ---> khoroji ro mitooni berizi dar tabe ---> age narizi b sorate out neshoon mide

----------------------------------------------------------------------------------------------------------------------

3-4-iterable

Chanta Value dashtim chetor?

number, bool ,str --> tak value boodan

agar ma chandin meghdar ro bekhaym dar yek zarf zakhire konim 

10 , 20 , 30

Iterables ---> dakheelsh iteration bezanin  [for ,....]

3-4-1-list ---> ordered (index) , changable, allow duplicated(ejaze mide tekrari benevisi)
 c=[10,10.233223 , 1j , True , 'Ali']  ,   d= [10 , 20 , [10,20,30]]

List functions ---> emal mishavad , khoroji nemidahad ---> zarf nemisazim barashoon

a = []

a= [10,20,True,'ali']
a[index]
a[start:end]
a[0] =10
                                    
a=[]
a.append('ali')
                        
print(a) ---> a=['ali']

append ---> Adds an element at the end of the list
clear---> Removes all the elements from the list ---> del ---> del miad khode zarfo ba jash hazf mikone
copy()---> Returns a copy of the list ---> khoroji mide
count ---> Returns the number of elements with the specified value ---> khoroji mide ,   adad 
extend ---> Add the elements of a list (or any iterable), to the end of the current list
index ---> Returns the index of the first element with the specified value
insert ---> Adds an element at the specified position ---> (index,element)
pop ---> Removes the element at the specified position ---> hem emal mishe ham khoroji ---> index midi va hazf mikone---> age index 
nadi yani ()khali ---> hazf akhari
remove ---> Removes the first item with the specified value ---> khode element hazf mikone
reverse ---> Reverses the order of the list
sort ---> Sorts the list

fargh extend , append , + ---> + hatman bayad dar yek zarf rikhte shavad ---> list3 = list1 + list2 --->  eshtebahe age vase extend o append 
zarf besazim ---> choon ina khoroji nemidan o emal mishan age too zarf berizim javab None b ma mide

tamame tavabei k emal mishan va khoroji nemidan ro nabayad dar zarf berizim

3-4-2-tuple ---> ordered (index) , unchangable , allow duplicated ---> too data base estefade mishe ---> nemikhan taghir kone ---> baray taghir tabdil konim b list
a2 = (10,20,30,40)
tuple tak elementi ---> a2 = (10,)
a[index] = new value ---> nemishe choon unchangable ---> casting

list ,  tuple

index    value
0       elm0
1       elm1
2       elm2
3       elm3
4       elm4
5       elm5


a  = (10,20,30)
a=(10,) ---> tuple
a=(10) ---> number
                    
a[index]
                    
a[index]=new_value ---> unchanagbale
                    
casting 
b = list(a)
b[index]=new_value
b = tuple(a)


yeki az ghabeliyat haye mohem tuple ---> unpacking 
person = ("ali" , 25 , "Iran")
name , age , country = person 
print(name)
print(age)
print(country)

va baray ja b jaii estefade mishavad
a = 10
b = 20
a , b = b , a


3-4-3-set ---> unordered (no index) , unchangable , No duplicated ---> majmoe haye riazi ya zamani k bekahhi tekrari haro hazf konim
a3 = {10,20,30,40}

set 
valu 
elm0
elm1
elm2
elm3
elm4

Method  Shortcut    Description
add() ---> Adds an element to the set
clear() ---> Removes all the elements from the set
copy() ---> Returns a copy of the set
difference() ---> Returns a set containing the difference between two or more sets ---> tafazool ---> -
difference_update() ---> Removes the items in this set that are also included in another, specified set
discard() ---> Remove the specified item
intersection() ---> Returns a set, that is the intersection of two other sets  ---> eshterak ---> &
intersection_update() ---> Removes the items in this set that are not present in other, specified set(s)
isdisjoint() ---> Returns whether two sets have a intersection or not
issubset() ---> Returns True if all items of this set is present in another set  , Returns True if all items of this set is present in another, larger set
issuperset() ---> Returns True if all items of another set is present in this set , Returns True if all items of another, smaller set is present in this set
pop() ---> Removes an element from the set
remove() ---> Removes the specified element
symmetric_difference() ---> Returns a set with the symmetric differences of two sets ---> anasoor gheir moshtarak ---> ^
symmetric_difference_update() ---> Inserts the symmetric differences from this set and another
union() ---> Return a set containing the union of sets ---> ejtema ---> |
update() ---> Update the set with the union of this set and others


3-4-4-dict (dictionary) ---> zakhire information(etelaat) ---> index ---> key
key      value
key1      value1
key2     value2
key3     value3
key4    value4

b jaye index value , key value darim

'''

b= {'name' : 'ali'  , 'sen' : 49 ,
    'meli' :'04402332231332',
    'phone': '09120000000',
    'ghad':180 ,
    'city':'tehran'}

'''

a=['ali',40 , 4000000,'Iran']
                    
a[3]
                                        
b={'name':'ali' , 'sen':30 , 'keshvar':'iran'}
b=['keshvar'] ---> iran
                         
Method  Description
clear() ---> Removes all the elements from the dictionary
copy() ---> Returns a copy of the dictionary
fromkeys() --->  Returns a dictionary with the specified keys and value
get() --->  Returns the value of the specified key
items() ---> Returns a list containing a tuple for each key value pair
keys() ---> Returns a list containing the dictionary's keys
pop() --->  Removes the element with the specified key ---> hazf
popitem() --->  Removes the last inserted key-value pair
setdefault() --->   Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update() ---> Updates the dictionary with the specified key-value pairs
values() ---> Returns a list of all the values in the dictionary

---------------------------------------------------------------------------------------------------------------------------

keywords:
gahi shoma mikhahid yek khat az code, ya yek ghesmat az codeton ro bebandid b yek sharti (shart) yani man migam nemikham hamishe
#print salam ejra bshe

logico bekham avaz konam az keyword estefade mikonam

keywords ---> if,elif,else

1-if
hamishe dastoor avalemoon if ast
age else dar akhar bezari dg badesh nemitooni elif bezari
akharin shart mitoone else ya elif bashe

shart ---> chizi hast k javabesh True,False
1- == , != , > => ,< =<
2- str function is ---> isdigit , ...
3- in , not in ---> true , False mide ---> too just if karboord dare

if body(badane shart) ---> bade if oon section ro mitonim shartish konim ---> ta madami k yek tab ya 4 space jolo hastim

just if ---> rahzan

if shart:
    dastoor


     if
    /  \
 True   False
  /      \
dastoor   \
  edame code
 
if else ---> do rahi

if shart:
    dastoor1
    
else:
    dastoor2


   if
 /    \
 True   False
 /        \
 dastoor1  dastoor2
    edame code


if elif else ---> chand rahi , do rahi haye too dar too ---> elif avali True bashe baghiye elif ha check nemishan ---> age jaye elif , if bezarim ---> cpu masraf
 mishe(eshtebah nis vali behine nis)

'''
i = int(input("enter number:"))
if i > 0:
    print("pos")
if i <= 0:
    print("neg")  # dar if hame shart haro check mikone ---> khoroji in code dar sorati k adad 0 ra bedahim ham neg ham zero 
if i == 0:                 
    print("zero")

'''
if shart:
    dastoor1
    
else:
    if shart:
        dastoor2
    else:
        dastoor3


    if
   /  \
 True  False
  /      \
dastor1   if
          / \
        T     F
        /      \
dastoor2       dastoor3
    edame code


karbord
1- erroro begirid
agar jaei error bood ---> shart bezarid
True ---> erroro begir

2-drahi baz koni

3- multiple selection ---> age chanta entekhab gosaste darid mese mashin hesab ---> if operation == "jam"

4- entekhab hae k range dare
range ---> age chanta entekhab bazei range darid 
------------------------------------------------------------------------------------------------------------------

keywords

or,and,not

and ---> va ---> joftesh ---> bayad
or ---> ya ---> yekodom ---> hadeaghal

7<9 ---> True
not(7<9) ---> False

if shart1 or shart2:
    dastoor

True or True ---> True
True or False ---> True
False or True ---> True
False or False ---> False

if shart1 and shart2:
    dastoor

True and True ---> True
True and False ---> False
False and True ---> False
False and False ---> False

---------------------------------------------------------------------------------------

keywords 
is,in,not in

is ---> barresi hoviat do shei na serfan barabar boodaneshan
a = [1,2]
b = [1,2]
print(a == b) ---> True
print(a is b) ---> False

in ---> barresi ozviyat
numbers = [10,20,30]
if 20 in numbers:
    print("yes")

not in 
if 40 not in numbers:
    print("Not found")

----------------------------------------------------------------------------------------------------------------

keywords

loop(halghe)

for/while(baraye/ta zamani k) 

do daste dastoorate tekrar ---> 1- mahdood o moshakhas (for, while) 2- mahdood o namoshakhas (while)

for ---> zamani k mikhahim b andaze moshakhas yek kari ro anjam dahim va zamani k mikhahim iteration anjam dahim
for shomarande in iterable ---> string , list, set, tuple ,dictionary

for i in [1,2,3,4,5]:
    print('salam')
    
be ezaye i hae k inja hast --> i=1 , i=2 , i=3 , i=4 , i=5 dastore zir ro ejra kon
range(start,end,step) ---> listi --> start , start+step , ..... , end - 1

karbord:
static repeat ---> ye tekrare sabet ---> y print sadas kari ba i ,j nadare 
dynamic repeat ---> ye tekrare gheire sabet ---> az shoamrande ham estefade mikone
iteration ---> varresi --->  for i in iterables ---> mitonam varede yek iterables besham
az contional statement (dastorate shaerti ) dakhele loop estefade konam --> iteration anajm midi 
len faghat baraye iterable ha estefade mishe

for shomarande in baze:
    dastoor

baze mitone adad bashe [0,1,2,3] ya  mitoone esm bashe [ali,vahid]
b ezaye shomarande k zarf hast ---> i,x,number ... ---> done done chizaii k into hast bezar va dastoor ro ejra kon

for i in range x: 
    print("i")

ya

for i in range(0,11):
    print("i")

range ye tabe dakheli k start,stop,step migire
0,11,2 ---> start,stop,step
mitonim 0 nazarim khodesh az sefr hesab mikone va step ham nadim 1 mizare vali payan hamishe bayad begim ---> akhari exclude mishe 
yeki bishtar bayad begim

'''

for i in [1,2,3,4]:
    print("salam")

'''

if dakhele iterable ---> dakhele list mishi ---> done done check mikoni(shart ro) ---> bade check shart yeki az karay zire
1- print koni
2- count koni
3- berizi ye liste dg

'''

my_users=['ali','reza','sara','mehdi']

for user in my_users: #iteration --->  varresi 
    #user[0]=='a'
    # user.startswith('a')
    #agar a dakhele useer bood , 
    if 'a' in user:  #access ---> dastresi peyda mikonm 
        print(user) #action ---> kari k mikham konm , dastresi  


my_users=['ali','reza','sara','mehdi']
count = 0 
for user in my_users: #iteration ---> varresi 
    #user[0]=='a'
    # user.startswith('a')
    #agar a dakhele useer bood , 
    if 'a' in user:  #access ---> dastresi peyda mikonm 
        #print(user) #action ---> kari k mikham konm , dastresi  
        count = count + 1 


my_users=['ali','reza','sara','mehdi']
new_list = []
for user in my_users: #iteration ---> varresi  
    if 'a' in user:  #access ---> dastresi peyda mikonm 
        #print(user) #action ---> kari k mikham konm , dastresi  
        #count = count + 1 
        new_list.append(user)


my_users = ['ali','reza','sara','mehdi','bardia']

for user in my_users:
    if 'b' in user:
        print(len(user))


my_users = ['ali','reza','sara','mehdi','bardia']
position = 0 
for user in my_users:
    position = position + 1 
    if 'b' in user:
        print(user) 
        print(position)



my_users = ['ali','reza','sara','mehdi','bardia']
for user in my_users:
    if 'b' in user:
        print(user)
        print(my_users.index(user)) #index
        #position my_users.index(user) + 1

#k ham indexe oon element ham khode element


my_users = ['ali','reza','sara','mehdi','bardia']
for user in my_users:
    print(user)

#do ta shomarande 

#hey khode value ro pas mdie ba corresponding index --> indexe motenazeresh
for i,user in enumerate(my_users):
    print(i)
    print(user)


my_users = ['ali','reza','sara','mehdi','bardia']
#ham psoition , ham element 
#dota shomarande, indexo , element 
for i,user in enumerate(my_users):
    if 'b' in user: 
        print(user)
        print(i)


my_users = ['ali','reza','sara','mehdi','bardia']
my_users_age = [20,20,30,30,40]

for user,age in zip(my_users,my_users_age):
    print(user)
    print(age)
  
'''

#tabe enumerate do ta migire ---> i,user ---> se ta error mide
for i,user,age in enumerate(my_users):
    print(i)

#ValueError: not enough values to unpack (expected 3, got 2)

#tabe enumerate yeki begirad masalan user_ ---> tuple pas midahad

for user_ in enumerate(my_users):
    print(user_)
    print(type(user_))

(0, 'ali')
<class 'tuple'>
(1, 'reza')
<class 'tuple'>
(2, 'sara')
<class 'tuple'>
(3, 'mehdi')
<class 'tuple'>
(4, 'bardia')
<class 'tuple'>

----------------------------------------------------------------------------------------------------------------

keywords
pass , continiue , break ---> 3 ta keyword

pass ---> vaghti nemikham code kamel konam pass mizaram error nade

'''

for i in range(0,10):
    pass 

'''

continue ---> halgharo edame nemide baray oon shomarande

'''

for i in range(0,10):
    print(i)
    if i==3:
        continue

'''  
     
i --> 0,1,2,3,4,5,6,7,8,9

'''

for i in range(0,10):
    if i==3:
        continue

    print(i)
    
'''    

0
1
2
4
5
6
7
8
9

break ---> halgharo ghat mikone vaghti b oon shomarande mirese

'''

for i in range(0,10):
    if i==3:
        break
    print(i)

'''
0
1
2
'''
for i in  range(0,10):
    
    print(i)
    if i==3:
        break
'''

0
1
2
3


while: 
    
shomarande nadare khodemoon bayad tarif konim

while shart:
    dastooor

while loop ---> yek shart bezarid begd ta zamani ke in shart true hast anjam bede

aval bayad shart True , biyad varede halghe beshe , vared k beshe , dastoor ejra mikone barmigarde sharto chek mikone -->True
shart chek --> False --> miad biroon --> ta abad in karo anjam mide

1---> sharte --> True false
2---> fghht oonaei k mikhahi catch koni true beshe (gireshon bendazi) ---> shoro halghe
3---> yek kari koni , k shart b payan berese ---> endless loop nashe ---> dakhele dastoor rahe farar bezari ---> break , i=i+1

endless loop ---> halgheye binahayat 

i=0 #start 
while i<10:
    print('salam')

shoam bayad kari konid k javab i<10 ---> false beshe 

i=0 
while i<10:
    print('salam')
    i = i + 1 #update 

in error mide o eshtebah choon i = 0 avalesh nazashtim yani nemidone i chiye

while i < 10:
    i = i + 1
    print(i)

bedone start ---> shart asan true nemishe k vared beshe

i=100 
while i<10:
    print('salam')
    i = i + 1 #update 

moghayese for va while:

for i in range(0,10,1):  ---> 0 start , 10 , stop end  , 1 shomarande
    print("i")

i=0    ---> 0 start
while i<10: ---> 10 stop end
    i=i+1  ---> shomarande
    print("i")

while True
hamishe True has , hamishe yek kari ro anjam mide ,hame ro catch mikone 

'''

while True:
    password = input('password ro vared konid')

    if len(password) > 8:
        if not password.isdigit() and not password.isalpha():
            if not password.islower() and not password.isupper():
                break

            else:
                print('password nemitone faghat kochik bashe ya faghat bozorg bashe')

        else:
            print('passworde shoma ham bayad digit dahste bashe ham horof')

    else: 
        print('password zire 8 rgham nabashad')

    

print('passworde shoam ba moafaghiat sabt shod')

'''
---------------------------------------------------------------------------------------------------------------------------
unpacking:
    
tuple

'''
mylist = [ ('ali',10) , ('vahid',20) , ('reza',30)]

#yek list ---> 3 ta element dare  ---> har elemente ---> tuple --> 2 ta element

for i in mylist:
    print(i)

'''
('ali', 10)
('vahid', 20)
('reza', 30)
'''

for i in mylist:
    print(i[0])

'''
ali
vahi    
reza


list

'''

my_list = [("ali", 10),("vahid", 20),("reza", 30)]
for name,number in my_list:
    print(name)
    print(number)


#set

c = {10,20,30,40,50}
for i in c :
    print(i)

'''

javab mishe 30,20,10,40,50 ---> nokte ine k har seri taghir mide va in adad nazm nadaran choon set index nadarad va bi order zakhiras

dictionary

mohem tarin
website(frontend) ---> chizaii k ersal mikonim bishtar halate dictionary dare
frontend <---> backend

'''

products={'code':'z13' ,'brand':'zara' ,'price':10000 ,'user':'user10'}

products['brand']

for i in products:
    print(i)
    
'''
nokte ---> keys ro nazadi joloy products ---> i khali zadi ---> keys b ma mide  

code
brand
price
user


se ta tabe dakhli darim:
1-keys
2-values
3-items

'''

for i in products.keys():
    print(i)
    
'''

code
brand
price
user

'''

for i in products.values():
    print(i)

'''

z13
zara
10000
user10

'''

for i in products.items():
    print(i)

'''

('code', 'z13')
('brand', 'zara')
('price', 10000)
('user', 'user10')

-------------------------------------------------------------------------------------------------------------------------------------------

keywords

def , return

Tavabe baraye in omadan ---> yek code tekrari ro ya yek kar ---> function ---> amalkardi ro ---> shoma yek bar benvisi
yek esm bzari roosh, har dafe bejay neveshtan chandin khat code ---> sedash koni

sakhtare tabe:
1-define ---> besazid
2-call () ---> sedda konid

shart dashtim baraye esm gozarie moteghayer , baraye tabe ha ham hamoon shorot darim

tabe ha ---> esm daran 
1-ba adad shoro nashe
2-hich characteri joz _ nemishe
3-case sensetive 
4-esme tabe haye dakheli ya keyword haro nemitonid bezarid
    
input(vorodi) -------> [BOx] ----> Khoroji (output) begiri

def name(vorodi1) ---> agar yek voroodi darad

def name(vorodi1,vorodi2 ,vorodi3,vordoi4,....):  ---> agar chandta voroodi darad
    harcheghadr inja code bezani moratbeet ba tabe

tabe ham mitone khorooji dashte bashe ham nadashte bashe

'''  

def jam(numb1 , numb2):
    javab = numb1 + numb2
    print(javab)

'''
agar kamtar ya bishtar bedim error mide
jam(numb1=10 , numb2=20)  --> not define --> aval fucntion ro bayad run bzni
jam(numb1=10 , numb2=20, num3=1000) TypeError: jam() got an unexpected keyword argument 'num3'
jam(numb1=10 ) #TypeError: jam() missing 1 required positional argument: 'numb2'
jam(numb1=10 , numb2=20) #30

4 noe tabe darim
1-vorodi dashte bashe, khoroji nadashte bashe
2-vorodi dashte bashe, khoroji dashte bashe
3-voirodi nadashte bashe , khorojhi dashte bashe
4-na vorodi , na khoorji 

'''

def jamm(numb1 , numb2):
    javab = numb1 + numb2
    print(javab)
    
#30

d = jamm(10,20)
        
print(d) #None

'''
Mohemtarin nokte --> print khoroji nist 
print --> namayesh
khoroji yani --> yehcizi pas bede man betonam berizam to zarf

'''

def jam_(numb1 , numb2):
    javab = numb1 + numb2
    #print(javab)
    return javab

jam_(10,20)

'''
return --> bargardoon --> jaei k sedat zadan
ziresh yek zarf bzrm 

age zarf bezarim b ma javabo neshoon mide , age zarf nazarim joloye out ghermez b ma javab neshoon mide
    
print(zarf) #30

hame tabe ha return none taheshoon hast mage in ke benevisim return

4 no tabe darim

1- NA vorodi , na khoroji

'''

def welcome():
    print('=================')
    print('Khosh amadid hamegi')
    print('=================')
    
welcome()
    
'''

2-  vorodi dare ,  khoroji nadare

'''

def jaam(a,b):
    c = a + b
    print(c)
    # return None
        
jaam(30,40)

zarf = jam(30,40)

#print(zarf)---> zarf ->None

'''

3(KAMEL TARN)-  vorodi dare ,  khoroji dare

'''

def jam(a,b):
    c = a + b
    return c

zarf = jam(30,40)

def jam(a,b):
    c = a + b
    print(c)
    return c

zarf = jam(30,40)

'''
4- vorodi nadare , khoroji dare
in tabe ha shoodani vali karboordi nist

'''

def pi():
    return 3.14

a = pi()


def jam(numb1,numb2):#numb1 , numb2 ---> parametr
    javab = numb1 + numb2
    
    return javab


zarf = jam(10,20)#10 , 20 ---> argument

zarf = jam(numb1=10 , numb2=20)


'''

default saazi parametr ---> vaghti k masalan number2 = 10 gharar midahim yani agar b ma meghdar nadad baraye number2 ,10 bezar

tavabe vaghty yedone khoroji mide ---> zarfi ke mizarim jolosh baste be oon khroji, int, float, complex, str, bool, list ,...

zamani chandin khoroji (bish az 1 khoroji) outpu1 , outpu2 ,... ---> hamro mziare tooye yek tuple va pas mide,
 ye khoroji pas mide tabe ama khorje tuple 
 
unpacking ---> anjam bedi agar bedonam dota zarf pas midde

bjaye inke yek zarf bezarim va oon zarf beshe tupel --> [index] azash khroji begiri
zarf = jam_tafright(numb1=10,numb2=20)

chon tabe dota khoroji dare ma mitonim jolosh dota zarf bezarim

zarf1 , zarf2 = jam_tafright(numb1=10,numb2=20)

print(zarf1) #30
print(zarf2) #-10
 
'''
def jam_tafright(numb1,numb2=10):
    result_jam = numb1 + numb2
    result_tafrigh = numb1 - numb2

    return result_jam ,result_tafrigh
'''
mohemtarin notke --> parametr haye gheyre default bayad aval tarif shan badesh parametr haye default

def name(non-defaultparametrs ,....., default_paramets):
    
'''

def calculator(numb1,numb2,operation):
    if operation=='jam':
        javab = numb1 + numb2
        return javab
    elif operation=='tafrigh':
        javab = numb1 - numb2
        return javab
    else:
        raise ValueError('fght ba tafrigh jam javab dahid')

zarf = calculator(10,20,'zarb')

'''
vaghti if o elif dari hatman to else jaye inke return none bezari raise valueerror bezar k error bede vaghti karbar eshtebah zad

return ro mitooni dakhele har if bezani ya inke dar akhar bezari return (halat aval behtare)

injoori ham mishe nevesht:

'''    
def calculator(numb1,numb2,operation):
    return numb1 + numb2 if operation == "jam" else numb1 - numb2

'''
--------------------------------------------------------------------------------------------------------------------------------
ziba nevisi code va esm gozari dorost tabe va ... ---> esme tabe, esme variable ha hamechi ro ziba benevsiid, mafhoom dashte
bashe , esme tabe , esme zarf va hame kasani ke codeton ro mikhonan motvaje beshan ,khodetoon behtar mifhmidesh ,debuging peyda
kardane bug rahat tare , vaghty yek fard (shekrat) , review kone, confirm kone , resume ro
dar asre agentice emrozi --> codeton tamiz bashe --> agent ha ham behtar mifahman

ba negah be esme tabe --> kole karesh malom she
ba negah b esme vorodi befshmim vorodi chi mikhad
va tamame zarf haye dakhel
type hint --> hata begim che typi ro ma entezar darim
docstring benevisid ---> se ta qutation k bezani mitooni tozihat tabe ro benevisi

'''
#hint ---> hamin float k joloy number gozashtim y hint y komake

def jam(number1 : float , number2 : float):
    result = number1 + number2
    return result

def apply_discount_on_products(products : list,discount : float):
    '''
    
    in tabe baraye discount hast 
    baraye inke yek listi az price ha begire yek discount ro ..
    
    ....
    ...
    
    
    '''
    price_list=[]
    for price in products:
        new_price = price - (discount/100) * price
        price_list.append(new_price)
        
    return price_list

apply_discount_on_products()
#edameye code dige ejra nmsihe vaghty tabe be return mirese

def calculator(numb1,numb2,operator):
    if operator=='jam':
        result = numb1 + numb2
        return result
        A = 10 
        b = A+40
        
    elif operator =='tafrigh':
        result = numb1 - numb2
        return result
        

'''
keyword arguments
jam_tafright(numb1=10,numb2=20) #Out[17]: (30, -10)

positional arguments
jam_tafright(10,20) #Out[18]: (30, -10)

amalkard keyword argument va positional argument yeksane

'''
#har parametri bad az * --> keyword arguments

def jam(*,numb1,numb2):
    result = numb1 + numb2
    return result

jam(10,20) #TypeError: jam() takes 0 positional arguments but 2 were given
jam(numb1=10,numb2=20) #Out[34]: 30

#harchi ghabl az / biad ---> faghat positional
def jam(numb1,numb2,/):
    result = numb1 + numb2
    return result

jam(10,20) #Out[35]: 30
jam(numb1=10,numb2=20) #TypeError: jam() got some positional-only arguments passed as keyword arguments: 'numb1, numb2'

#tabe ha mitoonam vorodi list tuple set dictionary begiran
'''
man mitonam kari konam ke tabe am binahyat adad begire ,positonal argument begire
meghdar haro --> toye yek tuple mirize (zarf)
mitonm azash estefade konm
'''
def my_sum(*numbs):
    total = 0
    for numb in numbs:
        total = total + numb
        
    return total
        
#binahayat keyword begire tabam
#keywordi
#**kwarg

def information_processor(**my_dict):
    new_age = my_dict['sen'] + 40
    return new_age

information_processor(name='ali',sen=30,phone='0199',city='tehran',country='iran')


def information_processor(name,sen,**my_dict):
    new_age = my_dict['sen'] + 40
    return new_age

#vorodi (dictionary) --:> BOX --> 2 khorji ,list1 ,list2

#list1 --> esme onaei hast k available
#list2 -->esme onaei hast k unavailabele


inventory = {
    "apple": 20,
    "banana": 5,
    "orange": 0,
    "milk": 12,
    "bread": 0
}


def availabilities_in_inventory(products):
    available_list=[]
    unavailable_list=[]
    
    for product,stock in products.items():
        if stock==0:
            unavailable_list.append(product)
            
        else:
            available_list.append(product)
    
    return available_list , unavailable_list
            
availabilities_in_inventory(inventory)

'''
-----------------------------------------------------------------------------------------------------------------------------

keywords
global
nonlocal

'''

def jam(a,b):
    c = a + b 
    return c

d = jam(10,20)

print(a) #NameError: name 'a' is not defined
print(c)  #NameError: name 'c' is not defined

a=10
b=20
c= 10 + 20 
#return c 
'''
d --> 30

local --> dar tabe har zarfi sakhte mishe --> movaghat hast va bironesh tarif shod nist
global --> ooanei k brion az tabe hastan hame ja tarif shodan

python miad functione shomaro ejra kone ---> zarf hae ke misaze ro ---> movaghati misaze va pak mikone ---> local

agar zarf vojod nadashte bashe ---> movaghati misaze , return pak mikone zarfo


'''

a=50
def jam(a,b):
    c = a + b 
    return c

d = jam(a=10,b=20)

print(a) #50

print(c) #NameError: name 'c' is not defined

'''
c o hamzaman k tabe run mishe , biron az tabeha ham beshnase adade movaghat nabashe
local ---> glocal 
'''
def jam(a,b):
    global c #c ro movaghati nasaz  ---> ro ram misaze roo cash nemisaze
    c = a + b 
    return c
'''
tavabe rooye cash sakhte mishe  hamoon lahze khali mishe vali kool emal ha roo ram hast
'''
d = jam(a=10,b=20)
print(c) #30

'''
--------------------------------------------------------------------------------------------------------------------------------------

keywords
import , from  , as

Python modules and Packages 

be .py file ha migam ---> module 
yek app,... --> 180 k khat code dare --> .py neveshte nashode too chandind .py neevshte mishe --> chandin madules kenare ham migan ---> package 

shoma vaghty chanta file darid , har file havie tavabe hast

import yek bar lazeme va balaye codet

tarighe haye mokhtalefe import

from file import function
from file import function1,function2,...
import file.function
from file import * ---> SHODANI vali PROFESSIONAL nist
from file import function as f

too file i k shoma run mikonid --> l1.py ,.. main.py  ---> bayad ba esm import konid

main.py
config.py

az config chizi biari to main
from config import function

main.py
/folder1
    config.py
    
from folder1.config import function

from folder1.folder_dKheli.........config import function

baraye function haye doro baresh chejori import konan az ham??

aaz yek file e hamonja import koni

main.py ---> in run mishe (ghavaninehso bala goftm)
config.py
test.py

tooye config az test.py chizi vrdari
from .test import function

main.py 
config.py
accounts/
    test.py

from accounts.test import function

inja --> main.py ham hast --> folderam mishanse

main.py
accounts/
    test.py
    config.py
    
from .test import felano


main.py 
birooni.py
accounts/
    test.py
    config.py

dakhele config az bironi yechi vardaram

from birooni import function

ghanone mohem dare --> agar .. zadi bargashti b pakcage asli (madar) ---> az hamonja address bde

3 no chizi import mikonim dar python

1---> funciton haro az koja ---> az file haye khodemon 
2---> python standard libraries ---> ketabkhone haye standarde python
3---> external libraries

har file .py --> __name__

khode file ro run mikone __name__ == '__main__'

------------------------------------------------------------------------------------------------------------------------------------

keywords

try , except , finally , else

try except ---> shoma aksaran dar file main.py ---> vaghti filei hast k bayad roo run bashe  nabayad intrupt beshe (motevaghef beshe) 
try va except ---> error handling mikonid

Try ---> mizarid , except ham ejbarie
else , finally ---> optional
else ---> age doros ejra shod inam ejra kon
finally ---> ch doros ch ghalat --> in ro ejra kon

'''
try:
    meghdar = float(input('meghdare bardasht ro hesab konid:'))

    mojodi = 100000

    new_mojodi = bardasht(mojodi,meghdar)

except ValueError:
    print('meghdar sahih nemibashad')
except TypeError:
    print('meghdar motabar nemibashad')
except Exception:
    print('amaliat moafagh nabood') 

else:
    print('ba moafaghiat anajm shod')
    print('mojodie alan : ',new_mojodi)
    
finally:
    print('sepas gozaram')


'''
------------------------------------------------------------------------------------------

keywords 
raise , assert

'''
def withdraw(balance,amount):
    
    if balance<0:
        raise ValueError('Balance nemitavanad manfi')
    
    if amount<0:
        raise ValueError('Amount nemitavand manfi bashad')
        
    if balance < amount : 
        raise ValueError('mojodi hesab kafi nist')
    
    balance = balance - amount
    
    return balance

#withdraw(200,10)

#in do halat yeki hastan che raise bezarim che assert fargheshoon ine k raise baray user mizaran assert baray develaper mizaran
#if balance<0:
    #raise ValueError('Balance nemitavanad manfi')

#assert balance<0 , 'Balance is negative'

#assert ro baray dibuging mizaran

'''
----------------------------------------------------------------------------------------------
File and extensions & keyword with

'''
file = open(r'C:\Users\Hadis\Desktop\users.txt')

print(file) 

'''
r --> read
w --> write
a --> append
b --> binary
+ --> read and write
'''
#read
file = open(r'C:\Users\Hadis\Desktop\users.txt','r')
#mode --> halate khondan baz mikone
zarf = file.read()
#hamaro pas midad besorate str
zarf = file.read(3) #character ro bekhone
print(zarf)

file.close()

file = open(r'C:\Users\Hadis\Desktop\users.txt','r')

file.readline() #Out[193]: 'In the name of god\n'
#yk khat ro besorate str pas mide 

file.readline() #Out[194]: 'Hello everyone\n'

file.readline() #Out[195]: 'goodbye'

file.readline() #Out[196]: ''

file = open(r'C:\Users\Hadis\Desktop\users.txt','r')

#kole khat haro bsorate yek listi az khatt ha mide
file.readlines()

#Out[198]: ['In the name of god\n', 'Hello everyone\n', 'goodbye']

file.close()

with open(r'C:\Users\Hadis\Desktop\users.txt','r') as file:
    
    text = file.read()
    print(text)
    

#read
with open(r'C:\Users\Hadis\Desktop\users.txt','r') as file:
    
    text_list = file.readlines()
    count = 0 
    for line in text_list:
        if 'a' in line:
            count = count + 1 
            
    print(count)
            
#Write 
#overwrite
with open(r'C:\Users\Hadis\Desktop\users.txt','w') as file:
    file.write('salam\n')
    file.write('khoobi')  
    
    
with open(r'C:\Users\Hadis\Desktop\users.txt','w') as file:
    names=['ali\n','vahid\n','reza']
    file.write('salam\n')
    file.writelines(names)  
     
#farsi
with open(r'C:\Users\Hadis\Desktop\users.txt','w',encoding='utf-8') as file:
    file.write('سلام')
    
with open(r'C:\Users\Hadis\Desktop\users.txt','r',encoding='utf-8') as file:
    file.read()
     
#ezafe --->append
with open(r'C:\Users\Hadis\Desktop\users.txt','a') as file:
    file.write('salam')
    
 
#append --> ezafe kon
#hamchin fili vojod nadare
with open(r'C:\Users\Hadis\Desktop\users.txt','w') as file:
    file.write('salam')
    
#w ---> age file nabashe ham ---> misaze minevise
# age bashe --> pakesh mikone --> rosh minevisde
with open(r'C:\Users\Hadis\Desktop\users.txt','x') as file:
    file.write('salam')
    
'''
-----------------------------------------------------------------------------------------------------------------------------------
iter, next, yield
'''
a = [10,20,30,40]
print(a) #[10, 20, 30, 40]

#list,tuple,set,dictionary ---> Iterable ---> man ghabeliate iteration daronam daram 
#iter()
b = iter(a)
print(type(b)) #<class 'list_iterator'>

#ye chizi has k e iteration mikone
#roye ki ? rooye iterable (a)

print(b) #<list_iterator object at 0x1222cf0a0>
next(b) #Out[42]: 10
next(b)  #--->20
next(b)  #---> 30

zarf = next(b)

print(zarf) #40

next(b) #StopIteration



def my_something(my_list):
    for number in my_list:
        yield number
    
#return --> Yield

zarf = my_something([10,20,30,40])

print(zarf) #<generator object my_something at 0x12238d2a0>
print(type(zarf)) #<class 'generator'>

#agr variablei bezarid joloye tabe ei k yield dare --> generator tahvil mihgirid

'''
---------------------------------------------------------------------------------------------------------------------

b 3 ravesh code mizani:

1 - Monolothic structure ---> yek code yekparche ---> .py ---> local (laptob) , server --> python file.py
1 bar ejra mishan ---> az bala b paein mikhone, ejra mishe ---> script 
sherkat yekseri data ---> yek code benevisid ---> tamiz sazi kone
dar balash ---> file migire ---> kara anajm mishe ---> khoroji save mikone

2- Function based --> app shoma misazid, narm afzar
main.py --> file e appeton --> asli
folder darid , function haro to folder haye mojaza mizarid
100 file --> 99 file --> havie functione , runable nist ,zakhireye tabe ha hast onja
main.py --> az bala be paein azashon estefade miokonid

main.py
/folder
/folder
/folder 

import bayad konid hame ro dar main.py
import ha , try except 

main.py --> koli function hastan in fucntion ha vaslan b yek endpoint k vorodi az useer az frontend miad
run koni javab bgiri
yek file python main.py --> hamihse rune roo serve

3 - Object oriented programming (OOP)
class va object 
class ---> yek chizi hast ke shamele tavabe va moteghayer ha mishe

class 
    |
    function
    function2
    function3
    variabl1
    variable2
    
object


class, function --> mitone import beshe

A- ma khodemon tabe neveshitm ,class neveshtim --> import --> packags and modules

B- standard python libraries --> ketabkhone vojod dare , python hamzaman k isntall mikoni ketabkhane ha ham install mishe
ketabkjone.function()    ketabkhone.class() estefade konim

C- External libraries --> ketabkhone hastan , sherkate python , sherkat ha , danehsgah ha , developer --> tose e dadan
aval download badesh nasbeshon konim badesh estefade konim

---------------------------------------------------------------------------------------------------------------------

def  class

vaghti man yekseri afradi daram shabihe haman , name, sen ,moshkele aval inke  mjborm koli zarf dashte basham sakhtan dictionaray baraye har fard
moshkelel dovom ine k man yekseri tavabe daram k in tavabe ye man mikham beham dige vasl bashan va maghadir ro baraye har chiz negah dare
masalan baraye bank mikham in tavabe show_balance() bardasht() variz() be ham vasl bashan

'''

def bardasht(balance,amount):
    balance = balance - amount 
    return balance

bardasht(100,5) #Out[105]: 95

ali_customer = {'name':'ali','sen':40 , 'balance':2000}
ali_customer['balance'] = bardasht(ali_customer['balance'],1000)

def variz(balance, amount):
    balance = balance + amount 
    return balance

ali_customer['balance'] = variz(ali_customer['balance'] , 10000)

#tedade ziadi az yek 'CHIZ' darid ke magahdire moshtara tavabe moshyatrak daran
    
#vaghty mikhahi az class object besazid yekseri information midi 

class Customer:
    
    def __init__(self,name,sen,balance):
        #too dele object .name 
        self.name = name 
        self.sen = sen
        self.balance = balance

obj1 = Customer(name='ali',sen=20,balance=20000000)

    
obj1 ={'name':'ali','age':20,'balance':20000}
obj1 = dict({'name':'ali','age':20,'balance':20000})
obj1['name']
    
print(type(obj1)) #<class 'dict'>
    

obj1 = Customer(esm='ali',sen=20,mojoodi=20000)
obj1.name

obj1 = Customer('ali',20,20000)
       
#classs --> yek chizi hast ke az roosh object misazid ke havie attributes va methode
#attributes --> self.sen self.name self.balance ---> vijegi k b yek shei ya class taalogh darad
#method --> __init__ ---> tabei k dar badane class tarif mishe

class Customer:
    
    def __init__(self,esm,sen,mojoodi):
        #tabeye __init__ moshakhas mikone ke dar lahzeye skahte object chegone user bayad object besaze
        #too dele object .name 
        self.name = esm 
        self.age = sen
        self.balance = mojoodi
        
    def welcome(self):
        print('salam customere aziz')
        print(self.name)
        
        
    def show_balance(self):
        print('mojodie shoma hast:', self.balance)
        
        
    def return_balance(self):
        return self.balance
        
        
    def bardasht(self,amount):
        
        self.balance = self.balance - amount 
        
        print('ba moafaghiat anjam shod')
        print('mojodie alane shoma:',self.balance)
        
   
    def variz(self,amount):
        self.balance = self.balance + amount
       
        print('ba moafaghiat anjam shod')
        print('mojodie alane shoma:',self.balance)



obj1 = Customer('ali',20,2000)

obj1.name #Out[151]: 'ali'

obj1.show_balance() #mojodie shoma hast: 2000

zarf = obj1.show_balance() #mojodie shoma hast: 2000
print(zarf) #None

zarf = obj1.return_balance()
print(zarf) #2000

'''
anvae attribute:
    
instance attribute ---> vijegi k b yek nemone moshakhas taaloogh darad

'''
class student:
    def __init__(self,name):
        self.name = name

student1 =student("sara")        

'''

class attribute ---> in vijegi mostaghiman dar badane khood class tarif mishavad 

'''
class students:
    school ="python_academy"
    def __init__(self,name):
        self.name = name
student3 = students("parisa")        

'''
se noe methood darim
instance method  ---> methode nemoone --> ba self kar mikonad ---> mitavanad vijegi haman nemone ra bekhanad ya taghir dahad
'''
class Person:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        return f"my name is {self.name}"
 
person = Person("saman")    
print(person.introduce())
    
'''
class method ---> baraye tarif methood class az decorator @classmethod estefade mikonim
bejaye self mamoolan parametri b name cls daryaft mikonad k b class marboot ast
'''

class student_:
    school ="python_academy"
    def __init__(self,name):
        self.name = name
        
    @classmethod
    def change_school(cls,new_school): 
        cls.school = new_school
        
student4 = student_("parisa")  
student.change_school("code academy")

'''
static method ---> na self daryaft mikonad na cls
'''
class calculator:
    @staticmethod
    def add (a,b):
        return a + b
    
    @staticmethod
    def multiply(a,b):
        return a * b
    
print(calculator.add(10,5))
print(calculator.multiply(2, 3))

'''

-------------------------------------------------------------------------------------------------------------------------------------

anvae error

type error 
value error ---> float("salam") ---> could not convert string to float: 'salam'
index error ---> s = "ali" ---> print(s[3]) ---> error mide ---> string index out of range
zero division error ---> vaghti adadi taghsim bar 0 mishavad
name error ---> name felan is not defined
attribute error ---> int chizi b name upper nadare ,  upper tabe string
UnboundLocalError ---> cannot access local variable 'bozorgtarin' where it is not associated with a value
ImportError ---> attempted relative import with no known parent package
Syntax errror --> if a>10     : ro yadet mire , : , 
Logic error --> zamani k manteghi eshtebah --> hesabe bankie y fard beshe manfi 
File notexist error

--------------------------------------------------------------------------------------------------------------------------------------
ketab khane (library)

python yekseri libraries darad ---> python standard libraries ---> python berizi ina ham rosh nasb mishe

python shenasagari dare k ketabkhone haro jashono mishnase

import ketabkhone

ketabkhone.function1()

ketabkhone.function2()

from ketABKHONE import function1,function2
function1()
function2()

from ketabkhone import function1 as f1
f1()

python standard libraries
1-math
2-random
3-datetime
4-time
5-os
6-subprocess
7-pathlib
8-argparse
9-json
10-csv
11-sys
12-collections
13-logging
14-regular expressions
15-itertools

-------------------------------------------------------------------------------------------------------------
ketabkhane math
'''
import math
#variable hastan

math.pi #Out[15]: 3.141592653589793
math.e #Out[16]: 2.718281828459045

zarf = math.sqrt(100)
print(zarf) #10.0

from math import sqrt 
zarf = sqrt(100)

zarf= math.pow(2,3)
print(zarf) #8.0

a = 10.1  #nazdik b 10 
b= 10.5  #vasate 10
c = 10.9  #nazdik b 11

math.floor(a) #Out[21]: 10  
math.floor(b) #10
math.floor(c) #10

math.ceil(a) #11
math.ceil(b) #11
math.ceil(c) #11

math.trunc(a) #10
math.trunc(b)  #10
math.trunc(c)  #10

math.fabs(-10) #Out[34]: 10.0

math.factorial(5) #Out[36]: 120

#B M M --> bozorgtarin maghsome moshatarak
math.gcd(10,40) #Out[37]: 10

#K M M --> kochiktrin moghasome msohatarak
math.lcm(10,40) #Out[39]: 40

#10 ** 2 = 100
#log100 bar paye 10 = 2
math.log(100,10) #Out[40]: 2.0

math.log(100,2) #Out[41]: 6.643856189774725

#yekseri --->  loge makhsos
#log bar paye 120 
math.log10(100) #2

#Tavabe mosalasati

zavie = math.radians(0)
math.sin(zavie) #Out[52]: 0.0
math.cos(zavie) #Out[53]: 1.0
math.tan(zavie)
math.sinh() #sinue hyperbolic
math.cosh()
math.tanh()

#fasleye beyne do ta noghte ---> oghlidosi dashtim
#a = (x1,y1)
#b = (x2,y2)
# radical( x1 -x2)**2  + (y2 - y1)**2
a = (10,20)
b = (30,15)
math.dist(a,b) #Out[54]: 20.615528128088304

my_list=[10,20,30,40,50,60]
sum(my_list) #Out[55]: 210
#product
math.prod(my_list) #Out[56]: 720000000

'''
--------------------------------------------------------------------------------------------------------------------
ketabkhane random

'''
import random 
#ye adade randomi beyne 0 ta 1 --> float
random.random() #Out[57]: 0.6920511169526059
random.random()  #Out[58]: 0.962586230939572

#yek adade randome int beyne a va b 
random.randint(10,20) #Out[59]: 12
random.randint(10,20)

for i in range(0,5):
    tas = random.randint(1,6)
    print(tas)
    if tas == 6:
        tas = random.randint(1,6)
        print(tas)
    
'''
6
5
2
3
1
3
'''
random.randrange(10,20,2) #10 yebar , 16 
#yek adade float beyne a ta b  be do soorat 
#1 ---> uniform ---> tamame adade floate beyne 10 ta 20 yek shans baraye bardashte shodan darand
random.uniform(10,20) #Out[94]: 18.48854196443792
#2 ---> gaussian (normal) ---> Mohandesi , ejtemaei ,...
#gaussian distribution, normal distribution 
random.gauss(50, 10)
#Out[95]: 38.56046253653365

random.gauss(50, 10)
#Out[96]: 66.0020577791648

my_list=[10,20,30,40]
my_list=['ali','vahid','hamid','reza']
random.choice(my_list) #Out[114]: 'vahid'
random.choices(my_list,k=2) #Out[116]: ['hamid', 'ali']
random.choices(my_list,k=2) #Out[117]: ['ali', 'reza']

#weight
prizes=['a','b','c']
random.choices(prizes,weight=[10,70,20],k=1)

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist) #['banana', 'cherry', 'apple']

random.uniform(10,20) #Out[124]: 13.691781444178304
random.uniform(10,20) #Out[125]: 16.24430096458077
random.seed(42)
random.uniform(10,20) #Out[126]: 16.39426798457884

'''
-------------------------------------------------------------------------------------------------------------
ketabkhane datetime
'''
import datetime
zarf = datetime.datetime.now()
print(zarf) #2026-10-02 17:33:31.162810
zarf.year #Out[131]: 2026
zarf.month  #10
zarf.day #Out[133]: 2
zarf.hour #Out[134]: 17
zarf.minute #Out[135]: 33
zarf.second #Out[136]: 31

#custom besazi
birthday = '1999/10/15'
print(type(birthday)) #<class 'str'>

birthday = datetime.date(1999,10,15)
print(type(birthday)) #<class 'datetime.date'>
birthday.year #Out[141]: 1999
 
#emrooz --> zamano dar bairim
today = datetime.date.today()
zarf = today - birthday
print(zarf) #9849 days, 0:00:00

today = datetime.date.today()
#expiration subscribe ---> 30 ro 
expiration_date = today + datetime.timedelta(days=31)
print(expiration_date) #2026-11-02

expiration_date.strftime('%Y-%m-%d') #Out[150]: '2026-11-02'
expiration_date.strftime('%Y/%m/%d') #Out[151]: '2026/11/02'

#Y --> year
#m --> month
#d --> day
#H --> hours
#M --> minute
#S --> second

#% adadesho inja bzar

expiration_date.strftime('%Y|||%m|||%d')  #Out[152]: '2026|||11|||02'

'''
-----------------------------------------------------------------------------------------------------------------
ketabkhane time
'''

import time

print('salam')
time.sleep(5)
print('khodafez')

for i in range(0,100):
    #request
    time.sleep(2)
    

import random 

for i in range(0,100):
    #request
    my_random = random.gauss(2,0.5)  #1.1 , 1.5 , 2 , 2,6
    time.sleep( my_random)
    
# mikhahid yek fasele zmanai ro besanjid

zarf = time.perf_counter()
print(zarf) #175777.537054166
print('salam')

a= 10
b= 30
c = a + b
print(c)
zarf2 = time.perf_counter()

print('time e barnamt')
print(zarf2 - zarf) #0.0004349169903434813

'''
-----------------------------------------------------------------------------------------------------------------
ketabkhane os
'''
#OS kar ba file ha ast

import os 

os.getcwd() #Out[158]: 'C:\\Users\\Hadis'

os.chdir('C:\\Users\\Hadis\\desktop') #cd 

os.getcwd() #Out[161]:'C:\\Users\\Hadis\\desktop'

zarf = os.listdir()
print(zarf)

os.mkdir('Data')

zarf = os.listdir()
print(zarf)
#['.DS_Store', 'folder2', 'folder3', 'folder1', 'Data']

os.path.exists('Data') #Out[168]: True

if os.path.exists('Data2'):
    os.chdir('Data2')
else:
    os.mkdir('Data2')

#yekchizi bebini fiel ya directory
os.path.isfile('main.py') #true --> file 
os.path.isdir('Data2')

Base_path = 'C:\\Users\\'
name=input("name folderetono bedid") 
name_path =name +'\\'
desktop_path = 'desktop\\'
test_path = 'test\\' 

main_path = os.path.join(Base_path,name_path,desktop_path,test_path) 
print(main_path) #C:\Users\Hadis\desktop\test\
    
if os.path.exists(main_path):  
    os.chdir(main_path)
else:
    os.mkdir(main_path)
    os.chdir(main_path)

os.rename('old.txt','new.txt')
os.remove('Data')

#ramz haei k darid toye .py nemizarid dakhele .env misazid

'''
----------------------------------------------------------------------------------------------------------------------------
ketabkhane subprocess ---> ejraye barname ha o dastoorate system amel az dakhele python

subprocess yek tabe dare bename run ke toosh list migire yani dastoori ke mikhay ro bayad be soorate ozv haye yek list benevisi
masalan agar bekhay versoin git ro begiri dar terminal bayad bezani --> git --version
khob in dastoor az do bakhsh sakhte shodee    1-git    2- --version
kafie shabihe yek listesh koni ['git','--version'] va bezarish dakhele tabeye .run az subprocess
miad yek process jadid misaze va vaymise payan miabe va natijaro mesle yek khoroji mide --> shoma mitonid natije ro berizid tooye yek zarf
'''

import subprocess
result = subprocess.run(['git','--version'] , capture_output=True, text=True)

#parameter capture_output --> yani khoroji ro zakhire kon
#parametere text --> yani khoroji besoorate str bashe
#hamchnin yek parametr darim bename cwd = ke mitoni jolosh masiri ke mikhahi in dastoor ejra beshe ro bezari

print(result.stdout)
print(result.returncode)


'''
----------------------------------------------------------------------------------------------------------------------------
ketabkhane sys --> ertebat ba mohite ejraye khode python
sys be manaye system hast
bar khalafe subprocess ke ba farayandaye dige kar mikone , sys omdatan darbareye processe felie python hast

'''
import subprocess
import sys

subprocess.run(
    [sys.executable, "worker.py"],
    check=True
)

#gahan shoma nemikhay montazer bemoni ta oon dastoor ejrsa beshe yani .run() montazer mishe ta process payan yabad
#agar bekhay yek process rah andazi koni va badan contorlesh koni mitoni az tabeye Popen() estefade koni

process = subprocess.Popen(
    [sys.executable, "worker.py"]
)

print("Worker started")
print(process.pid)

# karaye dige

process.wait()
print("Worker finished")


import sys
print(sys.argv)

#agar shoma bejaye python main.py benevisi python main.py Ali 25 , sys.arg miad behet yek list mide 
#["main.py", "Ali", "25"]
#yani harchizi bade python omde ro behet mide ama baraye barnameye vaghei ketabkhoneye 'argparse' monaseb tare

#sys.exit() yani age in etefagh oftad miad b barname payan mide

import sys
age = -5
if age < 0:
    print("Invalid age")
    sys.exit(1)

print("Continue")


#masire mofasere python
import sys
print(sys.executable)

#/home/user/project/.venv/bin/python
#yani pythonet dare inja ejra mishe


#masire jostojoye module ha
import sys

for path in sys.path:
    print(path)


#gereftane etelaat
import sys

print(sys.version) #noskheye python
print(sys.platform) #shenase platforme system amel


'''
----------------------------------------------------------------------------------------------------------------
ketabkhane pathlib --> modiriate masire file ha va pooshe ha
shoma vaght ba folder ha file ha kar mikoni mitoni az ketabkhoneye OS estefade koni ama hamchnin pathlib ham darim

fek kon hamchin porozhey dari
project/
├── main.py
├── data/
│   ├── file1.csv
│   └── file2.csv
└── results/

'''
#masalan dar main.py mikhay adrss bdi be file1
from pathlib import Path

file = Path("data\file1.csv")

#mitoni masir ro ba amalgare \ besazi

from pathlib import Path

folder = Path("data")

file = folder "\ file1.csv"

print(file) #data\file1.csv


#vizhegie moheme Path ,vaghty shoma yek PATH misazi , khorojisho mirizi dar yek file ,in file dar asl yek object hast ,in object yekseri method dare
file = Path("data/file1.csv")
print(file.exists()) #vojode masir ro barresi mikone (true,false)
print(file.is_file()) #barresi mikone masir yek file hast ya na (true,false)
print(file.is_dir()) #barresi mikone masir yek pooshe hast ya na (true,false)

#baraye skahte pooshe (folder)
folder = Path("outputs/reports")
folder.mkdir(
    parents=True, #agar pooshe valed vojod nadashte bashe
    exist_ok=True #age vojod dashte bashe khata nemide
)

#haat dige mitonid bejaye open o .write mostaghim bekhonido benevisid

file = Path("notes.txt")

file.write_text(
    "Hello Python!",
    encoding="utf-8"
)

content = file.read_text(
    encoding="utf-8"
)

print(content)


#Hamchenin mitoni etealaate yek file ro injori begirid
file = Path("data/report.pdf")
print(file.name) #esme file -> report.pdf
print(file.stem) #esme file bedone format -> report
print(file.suffix) #esme format --> .pdf
print(file.parent) #masire madar --> data

#peyda kardane file ha ba glob() ---> farz kon yek poshe dari shamele koli file ke 100 ta aozna pdfe age bekhay fght file haye pdf onn ro peyda koni :

folder = Path("pdfs") #yani too foldere pdfs/
for file in folder.glob("*.pdf"):
    print(file.name)

#in *.pdf yani harchi k tahesh ba .pdf tamom shod
#agar hata file haye zir pooshe ham bekhay begarde bejaye glob() az rglob() estefade kon
for file in folder.rglob("*.pdf"):
    print(file)

#taghire name
file = Path("old.txt")
file.rename("new.txt")

#hazf
file = Path("new.txt")
file.unlink()

#gereftane masire kamel
file = Path("data/file.csv")
print(file.resolve()) #/home/ali/project/data/file.csv

#create folder
Path("data").mkdir()
#nested folders
Path("data/users/images").mkdir(
    parents=True
)

#age bekhay masire poshe ei ke file e pythone feli dakhhelesh hast az vizhegie __file__ estefade mikoni
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
data_dir = BASE_DIR / "data"

'''
------------------------------------------------------------------------------------------------------------------------
ketabkhane argparse --> daryaft o etebar sanjie vorodii haye khate farman

shoma baraye ejraye barname haye python kafie benevsiid
python main.py 

vaghty yek script minevisi , hamishe codet yeksan nist mikhay ejaze bedi dar halat haye mokhtalef ejra she
bedone inke varede khode code beshio taghir bedi

masalan yek barname dari ke pdf ro b yek excell tabdil mikone ,esme file hast convert.py ya main.py ya ...
shoma mikhahi ke user betone , poshe vorodi , poshe khorji va kheyi chizaro betone moshakhas kone bedone inke bere too code taghir bede

yani bejaye
python convert.py 

benevisde
python convert.py --input ./pdfs --outputs ./results

yani code convert.py ro run kon be soorati ke input = .(haminja) /foldere pdfs begard pdf haro
--output --> khoroji ro zakhire kon dar .(haminja) /results

'''
import argparse

parser = argparse.ArgumentParser(
    description="My first CLI program"
)

parser.add_argument("--name")
args = parser.parse_args()
print(args.name)
'''
aval yek parser misazi va yek description mizari
.add_argument yani ch chizaei bade python file.py taraf mitone bezane
.parse_args() mire mikhone chia dadi
baraye run krde barname bejaye python main.py shoma bayad bezani python main.py --name felan
Paramter haye add_argument ---> shoma mitonid type e vorodi ro begid chie
'''
parser.add_argument(
    "--age",
    type=int
)

#bayad python main.py --age 25 run beshe
#in argument ha k add mikonid optionalle , yani age taraf nazane None mishe va okeye
#ama age bekhayd yek chizii ro ejbari konid -->
parser.add_argument(
    "--input",
    required=True
)

#age bejaye None bekhahid pish farz dashte bashe
parser.add_argument(
    "--format",
    default="csv"
)

#age bekahhid entekhab haro mahdod konid
parser.add_argument(
    "--format",
    choices=["csv", "json", "txt"]
)

#yechizi darim bename action='store_true'
parser.add_argument(
    "--verbose",
    action="store_true"
)


#yani age user benvisde python main.py --verbose
#args.verbose ro True dar nazar migire, age nanvise False
#pas niazi be neevshtne --verbose True nist

#Ma do no argument darim
#1---> positional argument
parser.add_argument("filename")
#dastoor -> python main.py report.pdf

#2---> keyword arguments
parser.add_argument("--filename")
#yani bayad injori run bshe
#python main.py --filename report.pdf


#yeki az mohemtarin vizhegi in hast ke rahnamaye khodkar bename --help misaze
parser = argparse.ArgumentParser(
    description="Process PDF documents"
)

parser.add_argument(
    "--input",
    required=True,
    help="Input PDF directory"
)

parser.add_argument(
    "--output",
    default="results",
    help="Output directory"
)

args = parser.parse_args()

#karbar age bezane python main.py --help onmoghe hame argument haro ba tozihatesh o minevisde

'''
-------------------------------------------------------------------------------------------------------------------------------------
ketabkhane json

ma ta alan file e txt ro midonestim ke az open() estefade mikrdi hala baraye file e jpg/png, pdf, zip az chi estefade konim???

Part A - Binary Files
Part B - Json files
part c - CSV Files

binary
Tasvir, video, pdf, file hame ina dade haye binary hastand
pas vaghty az open() estefade mikonim, age bekhayim reead konim az r va baraye write az w estefade mikrdim
in dar soorati bood ke filemoon .txt bashe , age filemomnn binary bashe
yani image, pdf, zip ,.. bashe --> badesh b mizarim

'''

with open("image.jpg", "rb") as file:
    data = file.read()

print(type(data))
print(len(data))
print(data[:20])

'''
khorji -->
<class 'bytes'>
245760
b'\xff\xd8\xff\xe0\x00\x10JFIF...'

'''
#copy kardan
with open("image.jpg", "rb") as file:
    data = file.read()

with open("copy.jpg", "wb") as file:
    file.write(data)


'''

JSON mokkhafafe JavaScript Object Notation hast ke yek formate matni hast baraye zakhiro tabadole dade haye skahtar yafte (structured)
vaghty frontend o backend ertebat daran, dar besiari az API ha in shekle json hast
json shabihe dictionary hast va yekchizi mesle
{
  "name": "Ali",
  "age": 25,
  "city": "Tehran",
  "is_active": true,
  "skills": ["Python", "AI", "FastAPI"]
}


khob age ma yek dictionary dashte bashim , behtare bejaye inke ba open() tabdilesh konim be yek file e .txt mostagim tabdil konim b file .json
ya inke age file .json darim ono bekhonim

'''
#json.dump()
import json

user = {
    "name": "Ali",
    "age": 25,
    "city": "Tehran"
}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file)


#bejaye inke file.write() bezanim az json.dump() , ham file ro dadim ham dictionary ro
#.dump() oon ro tabdil krde be user.json
#ensure_ascii --> ejaze mide character haye gheyre ASCII mesle farsi mostaghim neveshte she
#in 4 ta indent mizare fasele tooraftegi mizare ke khandanesh rahat tar she
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(
        user,
        file,
        ensure_ascii=False,
        indent=4
    )


#json.load()
import json
with open("user.json", "r", encoding="utf-8") as file:
    user = json.load(file)

print(user)
print(user["name"])

# user yek dictionary hast
#yani yek file darim bename user.json va badesh dictionary

#json.dumps()
#in tabe tahesh 's' dare be manaye string yani miad yek dictionary ro tabidl mikone be str

import json

user = {
    "name": "Ali",
    "age": 25
}

text = json.dumps(user)

print(text) #'{'name':'ali','age':25}'
print(type(text)) #<class 'str'>

#json.loads()
#in tabe tahesh s dare be manaye str
#in miad va yek reshte JSON ro tabdil mikone be dictionary 

import json

text = '{"name": "Ali", "age": 25}'

data = json.loads(text)

print(data["name"]) #Ali
print(type(data)) #<class 'dict'>


'''
--------------------------------------------------------------------------------------------------------------------------------------
ketabkhane csv

csv yani Comma-seperated Values yani etelaat dar file e matni besoorate satro sotoon zakhire shode va soton ha joda has

masalan dar users.csv ma darim
name,age,city
Ali,25,Tehran
Sara,22,Shiraz
Reza,30,Tabriz

in file shabihe excel hast ama formate besiar sade tar

'''

import csv

with open("users.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


#bejaye file.read() omadim az reader() e csv estefae krdim
#reader dar asl yek listi az list ha hast

#Khoroji :
'''

['name', 'age', 'city']
['Ali', '25', 'Tehran']
['Sara', '22', 'Shiraz']
['Reza', '30', 'Tabriz']
'''

#hata mitonim bsorate dict bargardone

import csv

with open("users.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

'''
{'name': 'Ali', 'age': '25', 'city': 'Tehran'}
{'name': 'Sara', 'age': '22', 'city': 'Shiraz'}
{'name': 'Reza', 'age': '30', 'city': 'Tabriz'}


'''

#neveshtane CSV
import csv

with open("users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age"])
    writer.writerow(["Ali", 25])
    writer.writerow(["Sara", 22])

#yek file msiaze bename user.csv ke injorie
'''
name,age
Ali,25
Sara,22

'''

#writerow() yek radif minevise, age bekahim chand radif benevisim
rows = [
    ["Ali", 25],
    ["Sara", 22],
    ["Reza", 30]
]

with open("users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age"])
    writer.writerows(rows)

#nevshtane ba dictwrite
import csv

users = [
    {"name": "Ali", "age": 25},
    {"name": "Sara", "age": 22}
]

with open("users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "age"]
    )

    writer.writeheader()
    writer.writerows(users)


'''
----------------------------------------------------------------------------------------------------------------------------
ketabkhane collection

majmoei eei az iterables ha(chandin meghdar dakhele yek zarf) dakhele yek standard library hastan bename collection

Counter --> shomareshe tedade tekrare anaser
defaultdict --> dictionary ba meghdare psihfarz baraye kilidhy jadid
deque --> afoozadno hazfe sari az ebteda o entehaye yek donabel
namedtuple --> sakhte recordhae ba field haye namdar

'''

# counter

from collections import Counter

words = ["python", "java", "python", "go", "python", "java"]
counts = Counter(words)
print(counts["python"])       # 3
print(counts.most_common(2))  # [('python', 3), ('java', 2)]

#str
letters = Counter("banana")
print(letters)
# Counter({'a': 3, 'n': 2, 'b': 1})

#shomarseh kalamat
text = "python is easy python is useful"
words = text.split()
counts = Counter(words)
print(counts)
# Counter({'python': 2, 'is': 2, 'easy': 1, 'useful': 1})

#  defaultdict
#mikhahim afrad ro bar asase shahr gorohbandi konim
from collections import defaultdict

people = [
    ("Ali", "Tehran"),
    ("Sara", "Shiraz"),
    ("Reza", "Tehran"),
    ("Mina", "Shiraz"),
]

groups = defaultdict(list)

for name, city in people:
    groups[city].append(name)

print(dict(groups))
# {'Tehran': ['Ali', 'Reza'], 'Shiraz': ['Sara', 'Mina']}


#  deque

from collections import deque

numbers = deque([10, 20, 30])
print(numbers)
# deque([10, 20, 30])

#4 amaliat
#append ---> enteha
#appendleft --->ebteda
#hazfo bargardandane enteha ---> pop()
#haazfo bargardanadnae ebtedaei ---> popleft()

numbers = deque([10, 20, 30])
numbers.append(40)
numbers.appendleft(5)
print(numbers)
# deque([5, 10, 20, 30, 40])

last = numbers.pop()
first = numbers.popleft()
print(last)     # 40
print(first)    # 5
print(numbers)  # deque([10, 20, 30])


#	namedtuple

from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grade"])

student = Student(name="Ali", age=22, grade=18.5)

print(student.name)   # Ali
print(student.age)    # 22
print(student.grade)  # 18.5

#shabihe tupel hanoz
print(students[0][0])  # Ali

student = Student("Ali", 22, 18.5)
student.grade = 20  # AttributeError

'''
---------------------------------------------------------------------------------------------------------------------------------

external library --> python ya laptabet shoma by default nadarateshon
download, install krd

terminal
pip --version
pip --> abzare --> komak mikone shoma ketabkhone haye ezxternal ro download konid

1-numpy
2-scipy
3-sympy
4-pandas  
5-matplotlib 
6-seaborn 
7-sklearn (scikit-learn)
8-Pytorch 
9-Tensorflow 
10-Django 
11-fastapi
12-keras
13-requests
14-flask
15-pillow
16-opencv
17-pygame
18-plotly
19-sqlalchemy
20-pydantic


'''