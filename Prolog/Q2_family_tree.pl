/*  Jon Snow's Family Tree (GOT) - along with Indian Kinship terms*/
% Spoilers ahead.

%%--Facts--%%
%Gender
male(jon_snow).
male(rheagar_targaryen).
male(rickard_stark).
male(edwyle_stark).
male(eddard_stark).
male(benjen_stark).
male(robb_stark).
male(brandon_stark).
male(rickon_stark).
male(aerys_targaryen).
male(duncan_targaryen).
male(aegon_V_targaryen).
male(viserys_targaryen).
male(roose_bolton).
male(ramsay_bolton).
male(khal_drogo).
male(rhaego).

female(lyanna_stark).
female(lyarra_stark).
female(marna_locke).
female(arya_stark).
female(sansa_stark).
female(talisa_stark).
female(catelyn_stark).
female(rhaelle_targaryen).
female(daenerys_targaryen).


%Relations - parentage
father(rheagar_targaryen,jon_snow).
father(aerys_targaryen,rheagar_targaryen).
father(aerys_targaryen,daenerys_targaryen).
father(aerys_targaryen,viserys_targaryen).
father(aegon_V_targaryen,rhaelle_targaryen).
father(aegon_V_targaryen,aerys_targaryen).
father(aegon_V_targaryen,duncan_targaryen).
father(khal_drogo, rhaego).
father(rickard_stark,lyanna_stark).
father(rickard_stark,eddard_stark).
father(rickard_stark,benjen_stark).
father(edwyle_stark,rickard_stark).
father(eddard_stark,robb_stark).
father(eddard_stark, sansa_stark).
father(eddard_stark,arya_stark).
father(eddard_stark,brandon_stark).
father(eddard_stark,rickon_stark).
father(roose_bolton,ramsay_bolton).

mother(rhaelle_targaryen,rheagar_targaryen).
mother(rhaelle_targaryen,daenerys_targaryen).
mother(rhaelle_targaryen,viserys_targaryen).
mother(daenerys_targaryen,rhaego).
mother(lyanna_stark,jon_snow).
mother(lyarra_stark,lyanna_stark).
mother(lyarra_stark,eddard_stark).
mother(lyarra_stark,benjen_stark).
mother(marna_locke,rickard_stark).
mother(catelyn_stark,robb_stark).
mother(catelyn_stark, sansa_stark).
mother(catelyn_stark,arya_stark).
mother(catelyn_stark,brandon_stark).
mother(catelyn_stark,rickon_stark).

% - spouses
spouse_data(aerys_targaryen, rhaelle_targaryen).
spouse_data(rheagar_targaryen, lyanna_stark).
spouse_data(khal_drogo, daenerys_targaryen).
spouse_data(edwyle_stark,marna_locke).
spouse_data(rickard_stark,lyarra_stark).
spouse_data(eddard_stark,catelyn_stark).
spouse_data(robb_stark,talisa_stark).
spouse_data(sansa_stark,ramsay_bolton).
spouse(X, Y) :-
    spouse_data(X, Y).
spouse(X, Y) :-
    spouse_data(Y, X).


% - elders (siblings)
elder_data(eddard_stark,benjen_stark).
elder_data(robb_stark,sansa_stark).
elder_data(sansa_stark,arya_stark).
elder_data(arya_stark,brandon_stark).
elder_data(brandon_stark,rickon_stark).
elder_data(rheagar_targaryen,viserys_targaryen).
elder(viserys_targaryen,daenerys_targaryen).
elder(X,Y):-
	elder_data(X,Y).
elder(X,Y):-
	elder_data(X,Z),
	elder(Z,Y).
younger(X,Y):-
	elder(Y,X).

% Rules for Generic Relations
different(X,Y):-
	dif(X,Y).

parent(X,Y):-
	father(X,Y);
	mother(X,Y).

son(X,Y):- 
	parent(Y,X),
	male(X).

daughter(X,Y):-
	parent(Y,X),
	female(X).

sibling(X,Y):-
	father(Z,X),
	father(Z,Y),
	different(X,Y).

brother(X,Y):-
	sibling(X,Y),
	male(X).

sister(X,Y):-
	sibling(X,Y),
	female(X).

wife(X,Y):-
	female(Y),
	spouse(X,Y).

husband(X,Y):-
	male(Y),
	spouse(X,Y).

paternal_uncle(X,Y):-
	male(X),
	father(Z,Y),
	sibling(X,Z).

maternal_uncle(X,Y):-
	male(X),
	mother(Z,Y),
	sibling(X,Z).

paternal_aunt(X,Y):-
	female(X),
	father(Z,Y),
	sibling(X,Z).

maternal_aunt(X,Y):-
	female(X),
	mother(Z,Y),
	sibling(X,Z).

paternal_cousin(X,Y):-
	parent(Z,X),
	father(W,Y),
	sibling(Z,W),
	different(X,Y).

maternal_cousin(X,Y):-
	parent(Z,X),
	mother(W,Y),
	sibling(Z,W),
	different(X,Y).

nephew(X,Y):- 
	parent(Z,X),
	sibling(Z,Y),
	male(X).

neice(X,Y):- 
	parent(Z,X),
	sibling(Z,Y),
	female(X).

grandparent(X,Y):-
	parent(X,Z),
	parent(Z,Y).

grand_father(X,Y):-
	grandparent(X,Y),
	male(X).

grand_mother(X,Y):-
	grandparent(X,Y),
	female(X).

grandchild(X,Y):-
	grandparent(Y,X).

grand_son(X,Y):-
	grandchild(X,Y),
	male(X).

grand_daughter(X,Y):-
	grandchild(X,Y),
	female(X).

great_grandparent(X,Y):- 
	parent(X,Z),
	parent(Z,W),
	parent(W,Y).

great_grand_father(X,Y):-
	great_grandparent(X,Y),
	male(X).

great_grand_mother(X,Y):-
	great_grandparent(X,Y),
	female(X).

great_grandchild(X,Y):- 
	great_grandparent(Y,X).

great_grand_son(X,Y):-
	great_grandchild(X,Y),
	male(X).

great_grand_daughter(X,Y):-
	great_grandchild(X,Y),
	female(X).

mother_in_law(X,Y):-
	daughter(Z,X),
	spouse(Z,Y),
	female(X).

father_in_law(X,Y):-
	daughter(Z,X),
	spouse(Z,Y),
	male(X).

% Rules for Indian Relations.
papa(X,Y):-
	father(X,Y).

mummy(X,Y):-
	mother(X,Y).

saga_bhai(X,Y):-
	brother(X,Y).

sagi_behen(X,Y):-
	sister(X,Y).

tau(X,Y):- 
	paternal_uncle(X,Y),
	father(Z,Y),
	elder(X,Z).

taayi(X,Y):- 
	tau(Z,Y),
	spouse(Z,X).

chacha(X,Y):- 
	paternal_uncle(X,Y),
	father(Z,Y),
	younger(X,Z).

chachi(X,Y):- 
	chachi(Z,Y),
	spouse(Z,X).

bhua(X,Y):-
	paternal_aunt(X,Y).

fufa(X,Y):-
	bhua(Z,Y),
	spouse(Z,X).

mama(X,Y):- 
	maternal_uncle(X,Y).

mami(X,Y):-
	mami(Z,Y),
	spouse(Z,X).

mausi(X,Y):-
	maternal_aunt(X,Y).

mausa(X,Y):-
	mausa(Z,Y),
	spouse(Z,X).

bhanja(X,Y):-
	nephew(X,Y),
	mother(Z,X),
	sister(Z,Y).

bhanji(X,Y):-
	neice(X,Y),
	mother(Z,X),
	sister(Z,Y).

bhateeja(X,Y):-
	nephew(X,Y),
	father(Z,X),
	brother(Z,Y).

bhateeji(X,Y):-
	neice(X,Y),
	father(Z,X),
	brother(Z,Y).

beta(X,Y):-
	son(X,Y).

bahu(X,Y):-
	son(Z,Y),
	spouse(Z,X).

beti(X,Y):-
	daughter(X,Y).

damaad(X,Y):-
	daughter(Z,Y),
	spouse(Z,X).

potha(X,Y):-
	grand_son(X,Y),
	father(Z,X),
	son(Z,Y).

pothi(X,Y):-
	grand_son(X,Y),
	father(Z,X),
	daughter(Z,Y).
	

nathi(X,Y):-
	grand_son(X,Y),
	mother(Z,X),
	son(Z,Y).

nathini(X,Y):-
	grand_son(X,Y),
	mother(Z,X),
	daughter(Z,Y).

chachera_bhai(X,Y):-
	paternal_cousin(X,Y),
	maternal_cousin(X,Y),
	male(X).

chachari_behen(X,Y):-
	paternal_cousin(X,Y),
	maternal_cousin(X,Y),
	female(X).

saala(X,Y):-
	sister(Z,X),
	spouse(Z,Y),
	male(X).

saali(X,Y):-
	saala(Z,Y),
	spouse(Z,X).

saas(X,Y):-
	mother_in_law(X,Y).

sasur(X,Y):-
	father_in_law(X,Y).

jeth(X,Y):-
	husband(Z,Y),
	brother(X,Z),
	elder(X,Z).

jethani(X,Y):-
	jeth(Z,Y),
	spouse(X,Z).

devar(X,Y):-
	husband(Z,Y),
	brother(X,Z),
	younger(X,Z).

devar(X,Y):-
	devar(Z,Y),
	spouse(X,Z).

nand(X,Y):-
	husband(Z,Y),
	sister(X,Z).

nandoi(X,Y):-
	nand(Z,Y),
	spouse(X,Z).

jeeja(X,Y):-
	sister(Z,Y),
	spouse(X,Z).

behenoi(X,Y):-
	jeeja(X,Y).

nana(X,Y):-
	grand_father(X,Y),
	daughter(Z,X),
	mother(Z,Y).

nani(X,Y):-
	grand_mother(X,Y),
	daughter(Z,X),
	mother(Z,Y).

dada(X,Y):-
	grand_father(X,Y),
	father(Z,X),
	son(Z,Y).

dadi(X,Y):-
	grand_mother(X,Y),
	father(Z,X),
	son(Z,Y).

parnana(X,Y):-
	father(X,Z),
	nana(Z,Y).

parnani(X,Y):-
	mother(X,Z),
	nana(Z,Y).

pardada(X,Y):-
	father(X,Z),
	dada(Z,Y).

pardadi(X,Y):-
	mother(X,Z),
	dada(Z,Y).


% Alias
couple(X,Y):- spouse(X,Y).
