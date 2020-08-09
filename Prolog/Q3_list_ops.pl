
%Check Memebership
member(X,[X|_]).
member(X,[_|Z]):-member(X,Z).

%Concatenation
conc([],L1,L1).
conc([X|L1],L2,[X|L3]):-conc(L1,L2,L3).

%Deletion of an item from list.
delete(_, [], []).
delete(X, [X|T], L):- delete(X, T, L), !.
delete(X, [H|T], [H|L]):- delete(X, T, L ).

