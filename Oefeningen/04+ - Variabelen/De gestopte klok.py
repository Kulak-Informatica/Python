#invoer
vertrek_thuis_u = float(input('Tijd dat je thuis vertrekt(uur): '))
vertrek_thuis_m = float(input('Tijd dat je thuis vertrekt(minuten): '))
aankomst_vriendin_u = float(input('Tijd dat je aankwam bij de persoon in kwestie(uren): '))
aankomst_vriendin_m = float(input('Tijd dat je aankwam bij de persoon in kwestie(minuten): '))
vertrek_vriendin_u = float(input('Tijd dat je vertrok bij de persoon in kwestie(uren): '))
vertrek_vriendin_m = float(input('Tijd dat je vertrok bij de persoon in kwestie(minuten): '))
aankomst_thuis_u = float(input('Tijd dat je thuis aankwam(uren): '))
aankomst_thuis_m = float(input('Tijd dat je thuis aankwam(minuten): '))

#verfijnde tijdduur
vertrek_thuis = (vertrek_thuis_u * 60) + vertrek_thuis_m
aankomst_vriendin = (aankomst_vriendin_u * 60) + aankomst_vriendin_m
vertrek_vriendin = (vertrek_vriendin_u * 60) + vertrek_vriendin_m
aankomst_thuis = (aankomst_thuis_u * 60) + aankomst_thuis_m

#formule
Reistijd_enkel = (((aankomst_thuis - vertrek_thuis + 1440) - (vertrek_vriendin - aankomst_vriendin + 1440)) % 1440) / 2
Uur_correct = (vertrek_vriendin + Reistijd_enkel)
Uur_correct_u = (Uur_correct // 60) % 24
Uur_correct_m = Uur_correct % 60

#uitvoer
print(int(Uur_correct_u))
print(int(Uur_correct_m))