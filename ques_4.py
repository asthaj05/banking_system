company = {
    "Project Managers": {
        "Robert Downey": {"Role": "Project Manager",
            "Team Leads": {
                "Mark": {"Role": "Team Lead","Experience": "8 years",
                    "Mentors": {
                        "Leonardo": {"Role": "Junior Developer","Experience": "1 year"},
                        "Alexandra": {"Role": "Junior Developer","Experience": "1 year"}
                    }
                },
                "Samuel": {"Role": "Team Lead","Experience": "8 years"},
                "Paul": {"Role": "Team Lead","Experience": "8 years",
                    "Mentors": {
                        "Fergal": {"Role": "Senior Developer","Experience": "4.5 years"}
                    }
                },
                "Tom": {"Role": "Team Lead","Experience": "8 years",
                    "Mentors": {
                        "Jerry": {"Role": "Junior Developer","Experience": "1.5 years"},
                        "John": {"Role": "Junior Developer","Experience": "1.6 years"}
                    }
                }
            }
        },
        "Anne Hathaway": {"Role": "Project Manager",
            "Team Leads": {
                "Chris": {"Role": "Team Lead","Experience": "5 years",
                    "Team": {
                        "James": {"Role": "Team Lead",
                            "Mentors": {
                                "Jennifer": {"Role": "Senior Developer","Experience": "3.8 years"},
                                "Scott": {"Role": "Senior Developer","Experience": "3.8 years"},
                                "Sophie": {"Role": "Senior Developer","Experience": "3.8 years"}
                            }
                        }
                    }
                },
                "Pratt": {"Role": "Team Lead","Experience": "5 years"},
                "Emma": {"Role": "Team Lead","Experience": "5 years"},
                "Will": {"Role": "Team Lead","Experience": "5 years",
                    "Mentors": {
                        "Edge": {"Role": "Senior Developer","Experience": "3 years"},
                        "Ryan": {"Role": "Senior Developer","Experience": "3.5 years"}
                    }
                },
                "Smith": {"Role": "Team Lead","Experience": "5 years",
                    "Mentors": {
                        "Walker": {"Role": "Senior Developer","Experience": "2.7 years"},
                        "Diana": {"Role": "Senior Developer","Experience": "2.7 years"}
                    }
                }
            }
        }
    }
}

# a. Display all employees names for the given project manager name.
def get_employees_by_manager(manager_name, company_dict):
    employees = []
    
    if manager_name in company_dict["Project Managers"]:
        manager_info = company_dict["Project Managers"][manager_name]
        for tl_name, tl_info in manager_info["Team Leads"].items():
            employees.append(tl_name)
            if "Mentors" in tl_info:
                for mentor_name in tl_info["Mentors"]:
                    employees.append(mentor_name)
            if "Team" in tl_info:
                for team_lead_name, team_lead_info in tl_info["Team"].items():
                    employees.append(team_lead_name)
                    if "Mentors" in team_lead_info:
                        for mentor_name in team_lead_info["Mentors"]:
                            employees.append(mentor_name)
    return employees

employees_under_robert = get_employees_by_manager("Robert Downey", company)
employees_under_anne = get_employees_by_manager("Anne Hathaway", company)

print("\n ----Displaying all the employees----")
print("\nEmployees under Robert Downey:", employees_under_robert)
print("\nEmployees under Anne Hathaway:", employees_under_anne)


# b. Display names of only those employees whose experience is more than 4 years.
def display_exp_employees(manager_name,company_dict, experience_threshold=4):
    experienced_employees = []

    if manager_name in company_dict["Project Managers"]:
        manager_info = company_dict["Project Managers"][manager_name]
        for tl_name, tl_info in manager_info["Team Leads"].items():
            
            if "Experience" in tl_info and float(tl_info["Experience"].split()[0]) > experience_threshold:
                experienced_employees.append(tl_name)
            
            if "Mentors" in tl_info:
                for mentor_name, mentor_info in tl_info["Mentors"].items():
                    if "Experience" in mentor_info and float(mentor_info["Experience"].split()[0]) > experience_threshold:
                        experienced_employees.append(mentor_name)
            
            if "Team" in tl_info:
                for team_lead_name, team_lead_info in tl_info["Team"].items():
                    if "Experience" in team_lead_info and float(team_lead_info["Experience"].split()[0]) > experience_threshold:
                        experienced_employees.append(team_lead_name)
                    
                    if "Mentors" in team_lead_info:
                        for mentor_name, mentor_info in team_lead_info["Mentors"].items():
                            if "Experience" in mentor_info and float(mentor_info["Experience"].split()[0]) > experience_threshold:
                                experienced_employees.append(mentor_name)
    return experienced_employees

experienced_employees_robert = display_exp_employees("Robert Downey", company)
experienced_employees_anne = display_exp_employees("Anne Hathaway", company)

print("\n-----Displaying experience employees----")
print("\nExperienced employees more than 4 years under Robert Downey:", experienced_employees_robert)
print("\nExperienced employees more than 4 years under Anne Hathaway:", experienced_employees_anne)


# c. Update years of experience with 4.6 whose experience is greater than 3.5 and less than 4.5 years
def updated_exp(min_experience = 3.5, max_experience = 4.6, new_experience = 4.5):
    for pm_name, pm_info in company["Project Managers"].items():
        for tl_name, tl_info in pm_info["Team Leads"].items():
            if "Experience" in tl_info and isinstance(tl_info["Experience"], str):
                try:
                    experience = float(tl_info["Experience"].split()[0])
                
                    if min_experience < experience < max_experience:
                        tl_info["Experience"] = f"{new_experience} years"
                except ValueError:
                    print("Experience must be in a float.")
                    continue
                    
            if "Mentors" in tl_info:
                for metor_name, mentor_info in tl_info["Mentors"].items():
                    if "Experience" in mentor_info and isinstance(mentor_info["Experience"], str):
                        try:
                            experience = float(mentor_info["Experience"].split()[0])
                            if min_experience < experience < max_experience:
                                mentor_info["Experience"] = f"{new_experience} years"
                        except ValueError:
                            print("Experience must be in a float.")
                            continue
                                    
            if "Team" in tl_info:
                for team_lead_name, team_lead_info in tl_info["Team"].items():
                    if "Experience" in team_lead_info and isinstance(team_lead_info["Experience"], str):
                        try:
                            experience = float(team_lead_info["Experience"].split()[0])
                            if min_experience < experience < max_experience:
                                team_lead_info["Experience"] = f"{new_experience} years"
                        except ValueError:
                            print("Experience must be in a float.")
                            continue    
                            
                if "Mentors" in team_lead_info:
                    for mentor_name, mentor_info in team_lead_info["Mentors"].items():
                        if "Experience" in mentor_info and isinstance(mentor_info["Experience"], str):
                            try:
                                experience = float(mentor_info["Experience"].split()[0])
                        
                                if min_experience < experience < max_experience:
                                    mentor_info["Experience"] = f"{new_experience} years"
                            except ValueError:
                                print("Experience must be in a float.")
                                continue
updated_exp()

print("\n-------The Updated Dictionary is----- ")
print("\n",company)

#d. Display TL with their year of experience, if has no experience then display N/A.

def display_tl_with_experience():
    for pm_name, pm_info in company["Project Managers"].items():
        print(f"\nProject Manger: {pm_name}")
        for tl_name, tl_info in pm_info["Team Leads"].items():
            if "Experience" in tl_info:
                print(f"\nTeam Leaders: {tl_name} - Experience:{tl_info["Experience"]}")
            else:
                print(f"\nTeam Leaders:{tl_name} - Experience: N/A")
            if "Team" in tl_info:
                for team_lead_name, team_lead_info in tl_info["Team"] .items():
                    if "Experience" in team_lead_info:
                        print(f"\nTeam Leaders: {team_lead_name} - Experience:{team_lead_info["Experience"]}")
                    else:
                        print(f"\nTeam Leaders:{team_lead_name} - Experience: N/A")
                
        
                       
display_tl_with_experience()

#e. Smith left the company and all his members were assigned to Ryan.

def reassign_member():
    smith_team = None
    for tl_name, tl_info in company["Project Managers"]["Anne Hathaway"]["Team Leads"].items():
        if tl_name == "Smith":
            smith_team = tl_info["Mentors"]
            break
    
    if smith_team:
        for tl_name, tl_info in company["Project Managers"]["Anne Hathaway"]["Team Leads"].items():
            if tl_name == "Will":
                if "Mentors" in tl_info and "Ryan" in tl_info["Mentors"]:
                    ryan_info = tl_info["Mentors"]["Ryan"]
                    if "Mentors" not in ryan_info:
                        ryan_info["Mentors"] = {}
                    ryan_info["Mentors"].update(smith_team)
                    break
                
    if "Smith" in company["Project Managers"]["Anne Hathaway"]["Team Leads"]:
        del company["Project Managers"]["Anne Hathaway"]["Team Leads"]["Smith"]     
        
reassign_member()

print("\n-----Reassingning Team-----")
print("\nAnne Hathaway: ",company["Project Managers"]["Anne Hathaway"])

#f. Check company has any employee who has less than 2 years of experience.

def check_employees_exp_less_than_two():
    for pm_name, pm_info in company["Project Managers"].items():
        if "Experience" in pm_info and isinstance(pm_info["Experience"], str):
            experience = float(pm_info["Experience"].split()[0])
            if experience < 2:
                return True
            
        for tl_name, tl_info in pm_info["Team Leads"].items():
            if "Experience" in tl_info and isinstance(tl_info["Experience"],str):
                experience = float(tl_info["Experience"].split()[0])
                if experience < 2:
                    return True
                
            if "Mentors" in tl_info:
                for mentor_name, mentor_info in tl_info["Mentors"].items():
                    if "Experience" in mentor_info and isinstance(mentor_info["Experience"], str):
                        experience = float(mentor_info["Experience"].split()[0])
                        if experience < 2:
                            return True
                        
            if "Team" in tl_info:
                for team_lead_name, team_lead_info in tl_info["Team"].items():
                    if "Experience" in team_lead_info and isinstance(team_lead_info["Experience"], str):
                        experience = float(team_lead_info["Experience"].split()[0])
                        if experience < 2:
                            return True
                        
                if "Mentors" in team_lead_info:
                    for mentor_name, mentor_info in team_lead_info["Mentors"]:
                        if "Experience" in mentor_info and isinstance(mentor_info["Experience"], str):
                            experience = float(mentor_info["Experience"].split()[0])
                            if experience < 2:
                                return True
                            
    return False

print("\n----Checking Employees which have experience less than two-----")
if check_employees_exp_less_than_two():
    print("\nYes there is/are employees with less than 2 years of experience.")
else:
    print("\n No, there is/are no employees with less than 2 years") 
    
#g. Check whether Edge is TL or not if not make him TL.
def make_edge_tl_if_not():
    edge_as_tl = "Edge" in company["Project Managers"]["Anne Hathaway"]["Team Leads"].values()
    print(edge_as_tl)
    
    if not edge_as_tl:
        company["Project Managers"]["Anne Hathaway"]["Team Leads"]["Edge"] = {
            "Role" : "Team Lead",
            "Experience" : "3 years",
            "Mentors" : {}
        }
        print("\n----Displaying Edge Role")
        print("\n Edge has been made a Team Lead uner Anne Hathaway.")
    else:
        print("Edge is already a team Lead")
        
make_edge_tl_if_not() 
