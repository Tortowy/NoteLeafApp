# NoteLeafApp

Aplikacja webowa NoteLeafApp napisana w frameworku django(4.1) służy do gromadzenia notatek na indywidualnych kontach
(notatki są zapisywane w bazie danych). Z poziomu aplikacji możliwe jest zarejestrowanie się z 
koniecznością potwierdzenia autentyczności maila(na podany adres email jest wysyłany link aktywacyjny).

![RegisterView](https://user-images.githubusercontent.com/69354928/223404811-6397c58b-69a5-4ea1-a8c0-fe902ef2188b.png)

![registrationMail](https://user-images.githubusercontent.com/69354928/223405288-522a6f84-3add-4631-9772-5d86ea1dbd94.png)


Po zalogowaniu użytkownik może dodawać,edytować i usuwać swoje notatki.

![LoginView](https://user-images.githubusercontent.com/69354928/223404534-64b3f578-73c6-4344-8de3-015b29fd2374.png)


![AddingNote](https://user-images.githubusercontent.com/69354928/223404681-74efb65a-2d85-408d-b979-58a66a78bbfe.png)


Hasła w do indywidualnych kont użytkowników przechowywane są w bazie danych w postaci hashy(SHA-256).
W sytuacji gdy użytkownik zapomni swojego hasła możliwe jest jego odzyskanie(poprzez wysłanie linku na podany mail).

![resetPasswordInApp](https://user-images.githubusercontent.com/69354928/223405629-e4f34887-fd83-4267-a594-3298d9cee8c1.png)

![resetPassword](https://user-images.githubusercontent.com/69354928/223406026-72d838c9-1ccb-4489-915d-de4134d0b15c.png)



Atrybuty klasy Notatka(Note) to:
	-Tytuł,
	-Konent,
	-Kategoria,
	-Data utworzenia,
	-Data wykonania(planowana),
	-Priorytet(low,medium,high),
	
	
Użytkownik ponad to może wyświetlać oraz na bieżąco edytować informacje związane z jego kontem.
Atrybuty klasy Użytkownik(User):
	-Email,
	-Username,
	-Imię,
	-Nazwisko,
	-Data dołączenia,
	-Data ostatniego zalogowania,
	-Flag admin,
	-Flaga active(symbolizuje aktywność konta),
	-Flaga staff,
	-Flaga superuser,
	
	
![AccountDetailEdit](https://user-images.githubusercontent.com/69354928/223406521-7dbc0825-8edf-415c-91f7-63c29db703c8.png)
	
