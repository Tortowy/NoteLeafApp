# NoteLeafApp

Aplikacja webowa NoteLeafApp służy do gromadzenia notatek na indywidualnych kontach
(notatki są zapisywane w bazie danych). Z poziomu aplikacji możliwe jest zarejestrowanie się z 
koniecznością potwierdzenia autentyczności maila(na podany adres email jest wysyłany link aktywacyjny).
Po zalogowaniu użytkownik może dodawać,edytować i usuwać swoje notatki.
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