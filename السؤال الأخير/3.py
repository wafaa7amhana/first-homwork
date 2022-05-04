# import Random module
import random
print("\nAn cellular Quize: ")
print("Please enter your name and ID number   : \n")
name=input("name: ")
ID=input("ID: ")
print("choose the correct answer (a) or (b) :")
#oppening the answers' file
#saving the answers in a list 

f3 = open('answers.txt' , 'r' )
m = 0
answerarray =  list()
hole_txt =  f3.read ()
for n in range ( int ( len ( hole_txt ) / 2 ) )  :
               
        answerarray.append ( hole_txt [ m ] )
        m +=2      
f3.close()
# opening the file that contain the  Questions

f = open('Questions.txt' , 'r' )

#creating an empty list to fill it with lines from the  Questions' file

l1=list()
for line in f :
        l1.append( line )
#Aggregating each 3  lines to make the quistion and making a list from them
        
l2 = list()
index1 = 0
for index2 in range ( int( ( len( l1 ) /3 ) ) ) :
        l2.append(  l1[  index1 :  index1 + 3 ]  )
        index1  += 3
#we could use the folowing syntax but we will be constrained   to only 7 questions from the file     
#l2=[ l1[0:3] , l1[3 :6] , l1[6 :9] , l1[9: 12] ,l1[12:15] , l1[15 :18] , l1[18 :21] ]
correct = 0
old_i = list ()
i = random.randint ( 0, len( l2 ) -1 )
#displaying 3 random qauestions from the questions' Bank file

for c in range(3) :
        
        print("******************************************************************")      
        print("Q{} : ".format ( c+1 ) )
    
        for j in range(3) :   
            print(  l2[i][j] , end =' ' )
            
        answer = input ()
        if  answer == answerarray[ i ] :
                correct += 1
               
        old_i.append( i )
        while(i in old_i ) :
                i= random.randint( 0, len( l2 ) -1 )
 #calculating the result
                
avg = correct /3 *100
if avg < 25 :
        result = "very Bad"
elif avg < 50 :
        result = "Bad"
elif avg < 75 :
        result = "Good"
else :
        result = "Excellent"
        
print("\n your result  is :  " , result  )
f.close()
#saving the result for each student in a Separated file

f1 = open ( 'results.txt' , 'a' )
f1.write ( " \n name :  {} ".format ( name )  )
f1.write ( " \n   ID :  {} ".format( ID )  )
f1.write ( " \n Score :{}  % \n ---------------------------------------------- ".format( avg )  )

f1.close()

                
        
