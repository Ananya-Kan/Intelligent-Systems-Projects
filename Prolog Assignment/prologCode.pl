suggestcareer(X):- X>=8,
           write("what is your priority-financial,startup or higher studies(f/s/h)?"),
           read(Choice1),subchoice(Choice1).

suggestcareer(X):- X<8,
            write("what is your priority-financial or startup(f/s)?"),
            read(Choice1),subchoice(Choice1).

subchoice(A):-A=='f',write("Do you want to do a tech job(y/n)?"),read(X),job(X).
subchoice(A):-A=='s',write("Did you do any projects in college(y/n)?"),read(X),((X=='y',write("You should go for a start up"));(X=='n',write("You should go for more experience in this field and then try for a start up.As a backup plan sit for placements."))).
subchoice(A):-A=='h',write("Have you done any research projects in college?"),read(X),((X=='y',write("You should apply for student loans and financial aid and try to pursue your studies outside India."));(X=='n',write("You should apply for higher studies but also have a backup option, you should sit for placements and gain experience in the field."))).
job(X):-X=='y',write("you can go for jobs in the field of cybersecurity, AI scientist, software developer or a computer engineer and definately prepare well for the placements and interview rounds.").
job(X):-X=='n',write("you have the option of jobs in the marketing and sales sector,analysts or as consultants, try sitting for non-tech companies").
getcareer():-
    write("what is your gpa in college"),
    read(X),nl,
    suggestcareer(X).
