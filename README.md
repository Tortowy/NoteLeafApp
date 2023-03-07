# NoteLeafApp

Aplikacja webowa NoteLeafApp napisana w frameworku django(4.1) służy do gromadzenia notatek na indywidualnych kontach
(notatki są zapisywane w bazie danych). Z poziomu aplikacji możliwe jest zarejestrowanie się z 
koniecznością potwierdzenia autentyczności maila(na podany adres email jest wysyłany link aktywacyjny).
Po zalogowaniu użytkownik może dodawać,edytować i usuwać swoje notatki.

![LoginView](https://user-images.githubusercontent.com/69354928/223404534-64b3f578-73c6-4344-8de3-015b29fd2374.png)


Hasła w do indywidualnych kont użytkowników przechowywane są w bazie danych w postaci hashy(SHA-256).
W sytuacji gdy użytkownik zapomni swojego hasła możliwe jest jego odzyskanie(poprzez wysłanie linku na podany mail).

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
